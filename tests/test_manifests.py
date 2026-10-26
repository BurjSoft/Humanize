"""Consistency checks for the plugin manifests and the skill frontmatter."""
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = ["plugin.json", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json"]
SKILL = ROOT / "skills/humanize/SKILL.md"


def load(relative):
    with open(ROOT / relative, encoding="utf-8") as f:
        return json.load(f)


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return None
    fields = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


class ManifestTests(unittest.TestCase):
    def test_versions_and_names_match(self):
        marketplace = load(".claude-plugin/marketplace.json")
        entry = next(p for p in marketplace["plugins"] if p["name"] == "humanize")
        versions = {path: load(path)["version"] for path in MANIFESTS}
        versions["marketplace entry"] = entry["version"]
        self.assertEqual(len(set(versions.values())), 1, versions)
        for path in MANIFESTS:
            self.assertEqual(load(path)["name"], "humanize", path)

    def test_descriptions_and_keywords_match(self):
        marketplace = load(".claude-plugin/marketplace.json")
        entry = next(p for p in marketplace["plugins"] if p["name"] == "humanize")
        descriptions = {path: load(path)["description"] for path in MANIFESTS}
        descriptions["marketplace entry"] = entry["description"]
        self.assertEqual(len(set(descriptions.values())), 1, descriptions)
        keywords = {path: tuple(load(path)["keywords"]) for path in MANIFESTS}
        self.assertEqual(len(set(keywords.values())), 1, keywords)

    def test_codex_skills_path_resolves_from_plugin_root(self):
        skills = load(".codex-plugin/plugin.json")["skills"]
        self.assertTrue((ROOT / skills / "humanize/SKILL.md").is_file(), skills)

    def test_marketplace_source_resolves(self):
        marketplace = load(".claude-plugin/marketplace.json")
        for plugin in marketplace["plugins"]:
            self.assertTrue((ROOT / plugin["source"] / ".claude-plugin/plugin.json").is_file())

    def test_skill_frontmatter(self):
        fields = frontmatter(SKILL)
        self.assertIsNotNone(fields, "SKILL.md must start with --- frontmatter")
        self.assertEqual(fields.get("name"), "humanize")
        self.assertTrue(fields.get("description"))
        self.assertLessEqual(len(fields["description"]), 1024)

    def test_files_referenced_by_skill_exist(self):
        text = SKILL.read_text(encoding="utf-8")
        for ref in set(re.findall(r"(?:references|scripts)/[\w.-]+\.(?:md|py)", text)):
            self.assertTrue((SKILL.parent / ref).is_file(), ref)


if __name__ == "__main__":
    unittest.main()
