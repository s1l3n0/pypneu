import unittest
from ASPProgramLoader import parse_string


class PropLanguageTestCase(unittest.TestCase):

    def test_parsing_1(self):
        rule_list = parse_string("b :- a.").rule_list
        assert len(rule_list) == 1

    def test_parsing_2(self):
        rule_list = parse_string("b :- not a. b :- -c.").rule_list
        assert len(rule_list) == 2
        assert rule_list[0].is_norm_rule()
        assert rule_list[0].head.input_terms[0].naf is False
        assert rule_list[0].body.input_formulas[0].input_terms[0].naf is True
        assert rule_list[1].is_norm_rule()
        assert rule_list[1].head.input_terms[0].literal.neg is False
        assert rule_list[1].body.input_formulas[0].input_terms[0].literal.neg is True

    def test_parsing_3(self):
        rule_list = parse_string("b :- a. b :- d. e.").rule_list
        assert len(rule_list) == 3
        assert rule_list[0].is_norm_rule()
        assert not rule_list[0].is_fact()
        assert not rule_list[0].is_constraint()
        assert rule_list[1].is_norm_rule()
        assert not rule_list[2].is_norm_rule()
        assert rule_list[2].is_fact()
        assert not rule_list[2].is_constraint()

    def test_parsing_4(self):
        rule_list = parse_string("b :- a. :- d. e.").rule_list
        assert len(rule_list) == 3
        assert not rule_list[1].is_norm_rule()
        assert not rule_list[1].is_fact()
        assert rule_list[1].is_constraint()

    def test_extract_literals(self):
        rule_list = parse_string("b :- not a.").rule_list

        rule = rule_list[0]
        assert len(rule.extract_literals()) == 2

        rule_list = parse_string("b :- a, b, c, -d, -e, not f.").rule_list
        rule = rule_list[0]
        formula = rule.body
        assert len(formula.extract_literals()) == 6
        assert len(formula.extract_asserted_literals()) == 5
        assert len(formula.extract_naf_literals()) == 1

        rule_list = parse_string("b :- a. c :- -a. d :- not a.").rule_list

        rule = rule_list[0]
        assert rule.is_norm_rule()
        assert len(rule.extract_literals()) == 2
        assert len(rule.extract_asserted_literals()) == 2
        assert len(rule.extract_naf_literals()) == 0

        rule = rule_list[1]
        assert rule.is_norm_rule()
        assert len(rule.extract_literals()) == 2
        assert len(rule.extract_asserted_literals()) == 2
        assert len(rule.extract_naf_literals()) == 0

        rule = rule_list[2]
        assert rule.is_norm_rule()
        assert len(rule.extract_literals()) == 2
        assert len(rule.extract_asserted_literals()) == 1
        assert len(rule.extract_naf_literals()) == 1


if __name__ == '__main__':
    unittest.main()