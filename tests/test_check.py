"""Regression checks for the optional pattern sweep, not writing quality."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "skills/humanize/scripts/check.py"
SPEC = importlib.util.spec_from_file_location("humanize_check", SCRIPT)
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class CheckTests(unittest.TestCase):
    def test_short_screening_answer_does_not_get_rhythm_advice(self):
        text = "I use Node.js. I build workers. I use PostgreSQL. I maintain queues."
        report = "\n".join(checker.check(text))
        self.assertNotIn("sentences:", report)
        self.assertNotIn("openers:", report)
        self.assertIn("words:", report)

    def test_long_passage_still_gets_descriptive_rhythm(self):
        text = " ".join([
            "The worker reads each queued job and writes its processing state to the database before acknowledging the message.",
            "The retry policy leaves failed messages available for inspection so that operators can distinguish malformed input from temporary service failures.",
            "The deployment documentation explains which settings control timeouts and how to pause consumers while investigating a recurring processing error.",
            "The logs include the job identifier and attempt number so that support staff can trace a report without searching unrelated requests across all of the other production services.",
        ])
        report = "\n".join(checker.check(text))
        self.assertIn("sentences: 4", report)
        self.assertNotIn("probability", report)

    def test_short_text_still_reports_invisible_character(self):
        report = "\n".join(checker.check("A hidden\u200b character."))
        self.assertIn("invisible characters: 1", report)

    def test_flags_tool_residue(self):
        text = ("Hi [Client Name], see https://example.com/doc?utm_source=chatgpt.com "
                "for details. contentReference[oaicite:0]")
        report = "\n".join(checker.check(text))
        self.assertIn("unfilled placeholders", report)
        self.assertIn("AI referrer URL parameters", report)
        self.assertIn("chat citation leaks", report)

    def test_unicode_warnings_identify_characters_without_changing_input(self):
        text = "Keep\u00a0this\u202fspacing and 👨‍👩‍👧. Hidden\u200bword."
        before = text.encode("utf-8")
        report = "\n".join(checker.check(text))
        self.assertIn("U+00A0 NO-BREAK SPACE x1", report)
        self.assertIn("U+202F NARROW NO-BREAK SPACE x1", report)
        self.assertIn("U+200D ZERO WIDTH JOINER x2", report)
        self.assertIn("U+200B ZERO WIDTH SPACE x1", report)
        self.assertIn("may be legitimate", report)
        self.assertEqual(text.encode("utf-8"), before)

    def test_cli_ignores_leading_byte_order_mark(self):
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "bom.md"
            source.write_text("A plain sentence.\n", encoding="utf-8-sig")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(source)],
                capture_output=True, encoding="utf-8", check=True,
            )
            self.assertNotIn("invisible", result.stdout)
            self.assertNotIn("FEFF", result.stdout)

            piped = subprocess.run(
                [sys.executable, str(SCRIPT), "-"], input="﻿A plain sentence.\n",
                capture_output=True, encoding="utf-8", check=True,
            )
            self.assertNotIn("FEFF", piped.stdout)

    def test_flags_published_detector_patterns(self):
        text = ("Experts agree this serves as a model. Featured in Forbes and trusted by leading "
                "brands. Results may vary.")
        report = "\n".join(checker.check(text))
        self.assertIn("vague authority", report)
        self.assertIn("dressed-up verbs", report)
        self.assertIn("name dropping", report)
        self.assertIn("unnecessary caveats", report)

    def test_plain_project_facts_are_not_name_dropping(self):
        report = "\n".join(checker.check("I built the Stripe billing flow for a telecom platform."))
        self.assertNotIn("name dropping", report)
        self.assertNotIn("vague authority", report)

    def test_plain_links_and_brackets_are_not_residue(self):
        report = "\n".join(checker.check("See [the docs](https://example.com/?page=2) for setup."))
        self.assertNotIn("placeholders", report)
        self.assertNotIn("referrer", report)

    def test_cli_preserves_unicode_file_and_reads_utf8(self):
        import tempfile

        original = "Set α to 0.05. The name is Ирина. Keep 👨‍👩‍👧.\n"
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "draft.md"
            source.write_text(original, encoding="utf-8")
            before = source.read_bytes()
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(source)],
                capture_output=True, encoding="utf-8", check=True,
            )
            self.assertEqual(source.read_bytes(), before)
            self.assertIn("words:", result.stdout)
            self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
