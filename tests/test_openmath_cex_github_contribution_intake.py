import unittest

from ci.openmath_cex_github_contribution_intake import IntakeError, parse_result_comment


VALID = """GCL-CONTRIBUTION-RESULT/1
dispatch_id: OM26-H1-H1-12-IA-001
agent_ref: INDEPENDENT-AGENT-001
assignment: OM26-H1-H1-12
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

A precise bounded statement.

## Derivation

A complete bounded derivation.

## Assumptions beyond bootstrap

NONE

## Verification / falsification hooks

Replay the finite argument independently.

## Claim boundary

This does not prove global optimality.

## Next residual

The remaining q>=6 cases remain open.
"""


class OpenMathCEXGitHubContributionIntakeTest(unittest.TestCase):
    def test_valid_result_parses(self):
        parsed = parse_result_comment(VALID)
        self.assertEqual(parsed["preamble"]["dispatch_id"], "OM26-H1-H1-12-IA-001")
        self.assertEqual(parsed["preamble"]["agent_ref"], "INDEPENDENT-AGENT-001")
        self.assertEqual(parsed["preamble"]["disposition"], "PROVED_REDUCTION")

    def test_wrong_agent_rejected_by_dispatch_layer_not_parser(self):
        body = VALID.replace("INDEPENDENT-AGENT-001", "OTHER-AGENT")
        parsed = parse_result_comment(body)
        self.assertEqual(parsed["preamble"]["agent_ref"], "OTHER-AGENT")

    def test_url_in_result_rejected(self):
        body = VALID.replace("A complete bounded derivation.", "See https://example.com")
        with self.assertRaises(IntakeError):
            parse_result_comment(body)

    def test_missing_section_rejected(self):
        body = VALID.replace("## Claim boundary\n\nThis does not prove global optimality.\n\n", "")
        with self.assertRaises(IntakeError):
            parse_result_comment(body)

    def test_invalid_disposition_rejected(self):
        body = VALID.replace("PROVED_REDUCTION", "OPTIMAL")
        with self.assertRaises(IntakeError):
            parse_result_comment(body)


if __name__ == "__main__":
    unittest.main()
