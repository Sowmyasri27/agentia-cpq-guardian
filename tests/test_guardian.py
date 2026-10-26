import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from guardian import validate, load_json


class GuardianTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_json(ROOT / "sample_data" / "catalog.json")

    def test_flags_missing_required_product(self):
        change = {"target_bundle_id": "HOME_STARTER",
                  "proposed_product_ids": ["HOME_STARTER"]}
        report = validate(self.catalog, change)
        self.assertEqual(report["status"], "FAIL")
        self.assertIn("MISSING_REQUIRED_PRODUCT", {f["rule_id"] for f in report["findings"]})

    def test_flags_incompatible_products(self):
        change = {"target_bundle_id": "HOME_STARTER",
                  "proposed_product_ids": ["HOME_STARTER", "BROADBAND_MODEM",
                                           "BASIC_VIDEO", "PREMIUM_VIDEO"]}
        report = validate(self.catalog, change)
        self.assertIn("INCOMPATIBLE_PRODUCTS", {f["rule_id"] for f in report["findings"]})

    def test_flags_unknown_product(self):
        change = {"target_bundle_id": "HOME_STARTER",
                  "proposed_product_ids": ["HOME_STARTER", "BROADBAND_MODEM", "NO_SUCH_PRODUCT"]}
        report = validate(self.catalog, change)
        self.assertIn("UNKNOWN_PRODUCT_REFERENCE", {f["rule_id"] for f in report["findings"]})

    def test_valid_configuration_passes(self):
        change = {"target_bundle_id": "HOME_STARTER",
                  "proposed_product_ids": ["HOME_STARTER", "BROADBAND_MODEM", "VOICE_ADDON"]}
        report = validate(self.catalog, change)
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["finding_count"], 0)

    def test_unknown_target_is_critical(self):
        change = {"target_bundle_id": "MISSING_BUNDLE",
                  "proposed_product_ids": ["MISSING_BUNDLE"]}
        report = validate(self.catalog, change)
        self.assertEqual(report["status"], "FAIL")
        self.assertEqual(report["findings"][0]["rule_id"], "UNKNOWN_TARGET_BUNDLE")


if __name__ == "__main__":
    unittest.main()
