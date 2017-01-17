import unittest
import proplanguage as pl
from ASPProgramLoader import parse_string

class PropLanguageTestCase(unittest.TestCase):

    def test_eq_atom(self):
        a1 = pl.Atom("a")
        a2 = pl.Atom("a")
        self.assertEqual(a1, a2)

    def test_eq_literal(self):
        a1 = pl.Literal(pl.Atom("a"), False)
        a2 = pl.Literal(pl.Atom("a"), False)
        self.assertEqual(a1, a2)

        a1 = pl.Literal(pl.Atom("a"), False)
        a2 = pl.Literal(pl.Atom("a"), True)
        self.assertNotEqual(a1, a2)

        a1 = pl.Literal(pl.Atom("a"), False)
        a2 = pl.Literal(pl.Atom("b"), False)
        self.assertNotEqual(a1, a2)

        a1 = pl.ExtLiteral(pl.Literal(pl.Atom("a"), False))
        a2 = pl.ExtLiteral(pl.Literal(pl.Atom("a"), False))
        self.assertEqual(a1, a2)

        a1 = pl.ExtLiteral(pl.Literal(pl.Atom("a"), False))
        a2 = pl.ExtLiteral(pl.Literal(pl.Atom("a"), True))
        self.assertNotEqual(a1, a2)

        a1 = pl.ExtLiteral(pl.Literal(pl.Atom("a"), False))
        a2 = pl.ExtLiteral(pl.Literal(pl.Atom("b"), True))
        self.assertNotEqual(a1, a2)

    def test_to_ASP(self):
        program = parse_string("b :- a, d. c :- a.")
        assert program.to_ASP() == "b :- a, d.\nc :- a.\n"

    def test_solve(self):
        program = parse_string("b :- not a. -c :- a. a.")
        answer_sets = program.solve()
        assert len(answer_sets) == 1
        assert len(answer_sets[0]) == 2
        assert answer_sets[0][0] == pl.Literal(pl.Atom("a"), False)
        assert answer_sets[0][1] == pl.Literal(pl.Atom("c"), True)

if __name__ == '__main__':
    unittest.main()