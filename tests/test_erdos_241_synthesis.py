import copy
import json
import unittest

from ci.validate_erdos_241_synthesis import (
    ADJUDICATION,
    CLOSURE,
    REPLAY,
    SUCCESSOR,
    SYNTHESIS,
    validate,
    validate_objects,
)


class Erdos241SynthesisTests(unittest.TestCase):
    def test_live_candidate_artifacts_validate(self):
        self.assertEqual(validate(), [])

    def test_parent_problem_authority_inflation_is_rejected(self):
        closure = json.loads(CLOSURE.read_text(encoding="utf-8"))
        replay = json.loads(REPLAY.read_text(encoding="utf-8"))
        adjudication = json.loads(ADJUDICATION.read_text(encoding="utf-8"))
        mutated = copy.deepcopy(adjudication)
        mutated["effects"]["parent_erdos_problem_effect"] = True
        errors = validate_objects(
            closure,
            replay,
            mutated,
            SYNTHESIS.read_text(encoding="utf-8"),
            SUCCESSOR.read_text(encoding="utf-8"),
        )
        self.assertIn("authority inflation: parent_erdos_problem_effect", errors)

    def test_source_gate_cannot_be_fabricated(self):
        closure = json.loads(CLOSURE.read_text(encoding="utf-8"))
        replay = json.loads(REPLAY.read_text(encoding="utf-8"))
        adjudication = json.loads(ADJUDICATION.read_text(encoding="utf-8"))
        mutated = copy.deepcopy(adjudication)
        mutated["source_lane"]["literature_dependent_promotion_gate_satisfied"] = True
        errors = validate_objects(
            closure,
            replay,
            mutated,
            SYNTHESIS.read_text(encoding="utf-8"),
            SUCCESSOR.read_text(encoding="utf-8"),
        )
        self.assertIn("literature-dependent source gate incorrectly satisfied", errors)


if __name__ == "__main__":
    unittest.main()
