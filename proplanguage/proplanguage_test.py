import unittest
from proplanguage import Atom, Literal, ExtLiteral
from ASPProgramLoader import parse_string

class PropLanguageTestCase(unittest.TestCase):

    def test_eq_atom(self):
        a1 = Atom("a")
        a2 = Atom("a")
        self.assertEqual(a1, a2)

    def test_eq_literal(self):
        a1 = Literal(Atom("a"), False)
        a2 = Literal(Atom("a"), False)
        self.assertEqual(a1, a2)

        a1 = Literal(Atom("a"), False)
        a2 = Literal(Atom("a"), True)
        self.assertNotEqual(a1, a2)

        a1 = Literal(Atom("a"), False)
        a2 = Literal(Atom("b"), False)
        self.assertNotEqual(a1, a2)

    def test_eq_ext_literal(self):
        a1 = ExtLiteral(Literal(Atom("a"), False))
        a2 = ExtLiteral(Literal(Atom("a"), False))
        self.assertEqual(a1, a2)

        a1 = ExtLiteral(Literal(Atom("a"), False))
        a2 = ExtLiteral(Literal(Atom("a"), True))
        self.assertNotEqual(a1, a2)

        a1 = ExtLiteral(Literal(Atom("a"), False))
        a2 = ExtLiteral(Literal(Atom("b"), True))
        self.assertNotEqual(a1, a2)

    def test_to_ASP(self):
        program = parse_string("b :- a, d. c :- a.")
        assert program.to_ASP() == "b :- a, d.\nc :- a.\n"

    def test_solve(self):
        program = parse_string("b :- not a. -c :- a. a.")
        answer_sets = program.solve()
        assert len(answer_sets) == 1
        assert len(answer_sets[0]) == 2
        assert answer_sets[0][0] == Literal(Atom("a"), False)
        assert answer_sets[0][1] == Literal(Atom("c"), True)

if __name__ == '__main__':
    unittest.main()