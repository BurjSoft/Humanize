"""Regression checks for the before/after fact check and the Upwork preview check."""
import importlib.util
from pathlib import Path
import unittest
import subprocess
import sys
import tempfile


SCRIPTS = Path(__file__).resolve().parents[1] / "skills/humanize/scripts"


def load(name):
    spec = importlib.util.spec_from_file_location("humanize_" + name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


compare = load("compare")
preview = load("preview")


class CompareTests(unittest.TestCase):
    ORIGINAL = ("I helped build the Angular 18 upgrade for MotoMate123, a CRM used by more than "
                "400 dealerships. I have not used Pinecone. See https://example.com/case.")

    def test_identical_text_passes(self):
        report, missing = compare.compare(self.ORIGINAL, self.ORIGINAL)
        self.assertFalse(missing)
        self.assertIn("no missing facts", report[0])

    def test_reports_dropped_facts_and_weakened_certainty(self):
        rewrite = ("I built the Angular upgrade for MotoMate123, a CRM used by all 400 dealerships. "
                   "I have used Pinecone extensively with AWS Lambda.")
        report, missing = compare.compare(self.ORIGINAL, rewrite)
        text = "\n".join(report)
        self.assertTrue(missing)
        self.assertIn("number: 18", text)
        self.assertIn("url: https://example.com/case", text)
        self.assertIn("'not'", text)
        self.assertIn("'helped'", text)
        self.assertIn("'more than'", text)
        self.assertIn("'all'", text)
        self.assertIn("term: AWS", text)
        self.assertIn("name: Lambda", text)

    def test_moved_facts_are_not_missing(self):
        rewrite = ("See https://example.com/case. MotoMate123 is a CRM used by more than 400 "
                   "dealerships, and I helped build its Angular 18 upgrade. I have not used Pinecone.")
        _, missing = compare.compare(self.ORIGINAL, rewrite)
        self.assertFalse(missing)

    def test_changed_values_do_not_pass_as_substrings(self):
        cases = [
            ("Processed 18 requests.", "Processed 180 requests.", "number: 18"),
            ("I use React.", "I use Reactive.", "name: React"),
            ("See https://example.com/case", "See https://example.com/case-study",
             "url: https://example.com/case"),
        ]
        for original, rewrite, fact in cases:
            with self.subTest(fact=fact):
                report, missing = compare.compare(original, rewrite)
                self.assertTrue(missing)
                self.assertIn("  " + fact, report)

    def test_known_limit_swapped_ownership_is_not_detected(self):
        # Documented limit: same tokens, reversed roles. The read-through has to catch this.
        _, missing = compare.compare("I helped build the API and led the frontend.",
                                     "I led the API and helped build the frontend.")
        self.assertFalse(missing)

    def test_sentence_start_name_is_reported_and_fails_only_in_strict(self):
        original, rewrite = "Stripe handles payments. I led the API.", "I led the API."
        report, failed = compare.compare(original, rewrite)
        self.assertFalse(failed)
        self.assertIn("  name: Stripe", report)
        self.assertTrue(compare.compare(original, rewrite, strict=True)[1])

    def test_name_confirmed_elsewhere_fails_when_dropped(self):
        # Capitalized mid-sentence too, so it is a confirmed name.
        report, failed = compare.compare("Stripe handles payments. I set up Stripe webhooks.",
                                         "I set up payment webhooks.")
        self.assertTrue(failed)
        self.assertIn("missing from rewrite:", report)

    def test_changed_sentence_openers_do_not_fail(self):
        _, failed = compare.compare("Weekly reports go out every Monday. Deployment happens on Friday.",
                                    "We send reports every Monday and deploy on Friday.")
        self.assertFalse(failed)

    def test_common_sentence_openers_are_not_names(self):
        _, failed = compare.compare("After launch we fixed the API. Today it is stable.",
                                    "We fixed the API after launch and it is stable now.")
        self.assertFalse(failed)

    def test_added_absolute_fails(self):
        report, failed = compare.compare("I can help investigate the issue.",
                                         "I guarantee I can investigate the issue.")
        self.assertTrue(failed)
        self.assertIn("'guarantee'", "\n".join(report))

    def test_new_terms_fail_only_in_strict_mode(self):
        original, rewrite = "I build React forms.", "I build React forms on AWS."
        self.assertFalse(compare.compare(original, rewrite)[1])
        self.assertTrue(compare.compare(original, rewrite, strict=True)[1])
        with tempfile.TemporaryDirectory() as directory:
            source, revised = Path(directory) / "a.txt", Path(directory) / "b.txt"
            source.write_text(original, encoding="utf-8")
            revised.write_text(rewrite, encoding="utf-8")
            script = [sys.executable, str(SCRIPTS / "compare.py")]
            plain = subprocess.run(script + [str(source), str(revised)], capture_output=True)
            strict = subprocess.run(script + ["--strict", str(source), str(revised)],
                                    capture_output=True)
            self.assertEqual(plain.returncode, 0)
            self.assertEqual(strict.returncode, 1)

    def test_reports_strengthened_certainty(self):
        report, missing = compare.compare("The cache could reduce retries.",
                                          "The cache will eliminate retries.")
        self.assertTrue(missing)
        self.assertIn("'could'", "\n".join(report))

    def test_reports_dropped_v_prefixed_version(self):
        report, missing = compare.compare("Upgraded the SDK to v2.4.", "Upgraded the SDK.")
        self.assertTrue(missing)
        self.assertIn("  number: v2.4", report)

    def test_number_formatting_and_moved_name_are_preserved(self):
        _, missing = compare.compare("I use React for 1,000 forms.",
                                     "React powers 1000 forms.")
        self.assertFalse(missing)

    def test_new_shorter_value_is_reported(self):
        report, _ = compare.compare("Processed 180 requests.", "Processed 18 requests.")
        self.assertIn("  number: 18", report)

    def test_cli_fails_for_lost_negation_or_qualifier(self):
        for original, rewrite, lost in [
            ("I have not used React.", "I have used React.", "negations"),
            ("I helped build React forms.", "I built React forms.", "qualifiers"),
        ]:
            with self.subTest(lost=lost), tempfile.TemporaryDirectory() as directory:
                source = Path(directory) / "original.txt"
                revised = Path(directory) / "rewrite.txt"
                source.write_text(original, encoding="utf-8")
                revised.write_text(rewrite, encoding="utf-8")
                result = subprocess.run(
                    [sys.executable, str(SCRIPTS / "compare.py"), str(source), str(revised)],
                    capture_output=True, encoding="utf-8",
                )
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertIn("fewer " + lost, result.stdout)


class PreviewTests(unittest.TestCase):
    JOB = "About 70% of tickets are repeat questions. We want pgvector RAG with human handoff."

    def test_flags_generic_opening(self):
        text = ("Hi there! My name is Hamza and I am a developer with 8 years of experience. "
                "I have read your job post and you are looking for a RAG assistant.")
        report = "\n".join(preview.preview(text, self.JOB))
        for label in ("greeting", "self-introduction", "years-of-experience opener",
                      "says they read the post", "restates the job post"):
            self.assertIn(label, report)

    def test_specific_opening_has_no_tells_and_matches_job_terms(self):
        text = ("If 70% of your tickets are already answered in the help docs, the assistant "
                "mostly needs to find the right article. I'd build the handoff path first.")
        report = "\n".join(preview.preview(text, self.JOB))
        self.assertNotIn("opening tells", report)
        self.assertIn("70%", report)
        self.assertIn("handoff", report)

    def test_short_acronyms_count_as_job_terms(self):
        report = "\n".join(preview.preview("I build AI and UI features.",
                                           "Need AI chatbot and UI work, QA too."))
        self.assertIn("'AI'", report)
        self.assertIn("'UI'", report)

    def test_job_post_can_come_from_stdin(self):
        with tempfile.TemporaryDirectory() as directory:
            proposal = Path(directory) / "proposal.txt"
            proposal.write_text("I build AI features.", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "preview.py"), str(proposal), "--job", "-"],
                input="Need AI chatbot work.", capture_output=True, encoding="utf-8",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("'AI'", result.stdout)

    def test_preview_runs_paragraphs_together(self):
        head = preview.preview("First paragraph.\r\n\r\nSecond paragraph.")[0]
        self.assertTrue(head.endswith("First paragraph. Second paragraph."))

    def test_missing_files_exit_cleanly(self):
        missing = str(SCRIPTS / "no-such-file.txt")
        for args in (["check.py", missing], ["compare.py", missing, missing],
                     ["preview.py", missing]):
            with self.subTest(script=args[0]):
                result = subprocess.run([sys.executable, str(SCRIPTS / args[0])] + args[1:],
                                        capture_output=True, encoding="utf-8")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("cannot read", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_preview_is_cut_at_a_word_boundary(self):
        text = "word " * 100
        head = preview.preview(text)[0]
        self.assertLessEqual(len(head.split(": ", 1)[1]), preview.PREVIEW_CHARS)
        self.assertTrue(head.endswith("word"))

    def test_flags_wall_of_text(self):
        report = "\n".join(preview.preview("token " * 90))
        self.assertIn("long paragraph", report)


if __name__ == "__main__":
    unittest.main()
