import antlr4
import logging
import proplanguage as lp

from gen.ASPProgramLexer import ASPProgramLexer
from gen.ASPProgramListener import ASPProgramListener
from gen.ASPProgramParser import ASPProgramParser

logging.basicConfig(filename='ASPProgramLoaderListener.log', filemode='w', level=logging.INFO)


class ASPProgramLoaderListener(ASPProgramListener):
    def __init__(self):
        self.decorations = {}
        self.rule_list = []

    def exitPos_literal(self, ctx):
        if ctx.predicate().IDENTIFIER():
            atom = lp.Atom(name=ctx.predicate().IDENTIFIER().getText())
            self.decorations[ctx] = atom
            logging.info("captured pos literal: " + str(atom))
        else:
            raise ValueError("Unexpected element in " + ctx.getText())

    def exitLiteral(self, ctx):
        atom = self.decorations[ctx.pos_literal()]

        if ctx.MINUS():
            neg = True
        else:
            neg = False

        literal = lp.Literal(
            atom=atom,
            neg=neg
        )
        self.decorations[ctx] = literal
        logging.info("captured literal: " + str(literal))

    def exitExt_literal(self, ctx):
        literal = self.decorations[ctx.literal()]

        if ctx.NOT():
            naf = True
        else:
            naf = False

        ext_literal = lp.ExtLiteral(
            literal=literal,
            naf=naf
        )
        self.decorations[ctx] = ext_literal
        logging.info("captured ext literal: " + str(ext_literal))

    def exitList_literals(self, ctx):
        literal_list = []

        if ctx.literal():
            # for generality, we store ExtLiterals in the list, rather than Literals
            literal = lp.ExtLiteral(
                literal=self.decorations[ctx.literal()],
                naf=False
            )
        else:
            raise ValueError("Unexpected element in " + ctx.getText())

        literal_list.append(literal)

        if ctx.list_literals():
            literal_list = literal_list + self.decorations[ctx.list_literals()]

        self.decorations[ctx] = literal_list
        logging.info("captured (ext) literal list: " + str(literal_list))

    def exitList_ext_literals_expressions(self, ctx):
        formula_list = []

        if ctx.ext_literal():
            ext_literal = self.decorations[ctx.ext_literal()]
            formula = lp.Formula(
                operator=lp.Operator.NONE,
                input_terms=[ext_literal]
            )
            formula_list.append(formula)
        else:
            raise ValueError("Unexpected element in " + ctx.getText())

        if ctx.list_ext_literals_expressions():
            formula_list = formula_list + self.decorations[ctx.list_ext_literals_expressions()]

        self.decorations[ctx] = formula_list
        logging.info("captured (ext literal list) formula list: " + str(formula_list))

    def exitChoice(self, ctx):
        literal_list = self.decorations[ctx.list_literals]
        if not ctx.minchoice:
            l = ctx.minchoice.getText()
        else:
            l = 0

        if not ctx.maxchoice:
            r = ctx.maxchoice.getText()
        else:
            r = len(literal_list)

        if l == len(literal_list) and l == r:
            operator = lp.Operator.AND
        elif l == 1 and r == len(literal_list):
            operator = lp.Operator.OR
        elif l == 1 and r == 1:
            operator = lp.Operator.XOR
        else:
            operator = lp.Operator.CHOICE

        formula = lp.Formula(
            operator=operator,
            input_terms=literal_list  # should be ExtLiterals !!!
        )

        self.decorations[ctx] = formula
        logging.info("captured choice formula: " + str(formula))

    def exitHead(self, ctx):
        if ctx.literal():
            ext_literal = lp.ExtLiteral(
                literal=self.decorations[ctx.literal()],
                naf=False
            )
            formula = lp.Formula(
                operator=lp.Operator.NONE,
                input_terms=[ext_literal]
            )
        elif ctx.choice():
            formula = self.decorations[ctx.choice()]
        else:
            raise ValueError("Unexpected element in " + ctx.getText())

        self.decorations[ctx] = formula
        logging.info("captured head formula: " + str(formula))

    def exitBody(self, ctx):
        if ctx.list_ext_literals_expressions():
            formula_list = self.decorations[ctx.list_ext_literals_expressions()]
            formula = lp.Formula(
                operator=lp.Operator.AND,
                input_formulas=formula_list
            )
        elif ctx.choice():
            formula = self.decorations[ctx.choice()]
        else:
            raise ValueError("Unexpected element in " + ctx.getText())

        self.decorations[ctx] = formula
        logging.info("captured body formula: " + str(formula))

    def exitConstraint(self, ctx):
        if ctx.body():
            body = self.decorations[ctx.body()]
        else:
            raise ValueError("Unexpected element in " + ctx.getText())

        rule = lp.Rule(body=body)

        self.decorations[ctx] = rule
        logging.info("captured constraint: :- " + str(rule))

    def exitNormrule(self, ctx):
        if ctx.head():
            head = self.decorations[ctx.head()]
        else:
            raise ValueError("Unexpected element in " + ctx.getText())

        if ctx.body():
            body = self.decorations[ctx.body()]
        else:
            raise ValueError("Unexpected element in " + ctx.getText())

        logging.info("captured normal rule: " + str(head) + ":-" + str(body))
        self.decorations[ctx] = lp.Rule(head=head, body=body)

    def exitAsprule(self, ctx):
        if ctx.constraint():
            rule = self.decorations[ctx.constraint()]
        elif ctx.normrule():
            rule = self.decorations[ctx.normrule()]
        else:
            raise ValueError("Unexpected element in " + ctx.getText())

        logging.info("captured asp rule: " + str(rule))
        self.decorations[ctx] = rule
        self.rule_list.append(rule)

    def exitAspfact(self, ctx):
        if ctx.head():
            head = self.decorations[ctx.head()]
        else:
            raise ValueError("Unexpected element in " + ctx.getText())

        rule = lp.Rule(head=head)

        logging.info("captured asp fact: " + str(rule))
        self.decorations[ctx] = rule
        self.rule_list.append(rule)


def parse_literal(code):
    # return parse(antlr4.InputStream(code)+".") ## Highly inefficient
    if code[0] is "-":
        neg = True
        code = code[1:]
    else:
        neg = False

    for char in code:
        if not char.isalpha():
            raise ValueError("Unexpected element in " + code)

    return lp.Literal(atom=lp.Atom(code), neg=neg)


def parse_string(code):
    return parse(antlr4.InputStream(code))


def parse(input_stream):
    lexer = ASPProgramLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = ASPProgramParser(stream)
    tree = parser.program()
    loader = ASPProgramLoaderListener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(loader, tree)
    return lp.Program(rule_list=loader.rule_list)


if __name__ == '__main__':
    program = parse_string("b :- not a. -c :- a. a.")
    answer_sets = program.solve()
