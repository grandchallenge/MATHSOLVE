from __future__ import annotations

import unittest

from ci.ym_mrs_github_contribution_intake import IntakeError, parse_result_comment


def valid_result(external_sources: str = "PROTECTED_PACKET_ONLY") -> str:
    return f"""GCL-CONTRIBUTION-RESULT/1
dispatch_id: YM-D003-MRS-R002-WP-C-IA-001
assignment: C
disposition: REDUCED
context_class: ZERO_CONTEXT
external_sources: {external_sources}
timebox_observed: YES

## Strongest exact statement

One exact missing criterion is identified.

## Derivation

The protected premises do not imply the stronger conclusion without an additional uniformity hypothesis.

## Assumptions beyond bootstrap

NONE

## Verification / falsification hooks

Attempt the limit passage with constants depending on the cutoff and observe that no uniform conclusion follows.

## Claim boundary

This does not establish or refute the source construction.

## Next residual

State and test the required uniformity hypothesis.
"""


class YmMrsContributionIntakeTest(unittest.TestCase):
    def test_valid_result_parses(self) -> None:
        parsed = parse_result_comment(valid_result())
        self.assertEqual(parsed["preamble"]["assignment"], "C")
        self.assertEqual(parsed["preamble"]["disposition"], "REDUCED")

    def test_url_is_rejected(self) -> None:
        with self.assertRaises(IntakeError):
            parse_result_comment(valid_result() + "\nhttps://example.com\n")

    def test_wrong_dispatch_is_rejected(self) -> None:
        with self.assertRaises(IntakeError):
            parse_result_comment(valid_result().replace("WP-C-IA-001", "WP-Z-IA-001"))

    def test_extra_heading_is_rejected(self) -> None:
        with self.assertRaises(IntakeError):
            parse_result_comment(valid_result() + "\n## Extra\nno\n")


if __name__ == "__main__":
    unittest.main()
