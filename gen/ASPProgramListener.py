# Generated from /Users/giovanni/dev/pypneu/grammars/ASPProgram.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ASPProgramParser import ASPProgramParser
else:
    from ASPProgramParser import ASPProgramParser

# This class defines a complete listener for a parse tree produced by ASPProgramParser.
class ASPProgramListener(ParseTreeListener):

    # Enter a parse tree produced by ASPProgramParser#program.
    def enterProgram(self, ctx:ASPProgramParser.ProgramContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#program.
    def exitProgram(self, ctx:ASPProgramParser.ProgramContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#directive.
    def enterDirective(self, ctx:ASPProgramParser.DirectiveContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#directive.
    def exitDirective(self, ctx:ASPProgramParser.DirectiveContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#asprule.
    def enterAsprule(self, ctx:ASPProgramParser.AspruleContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#asprule.
    def exitAsprule(self, ctx:ASPProgramParser.AspruleContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#aspfact.
    def enterAspfact(self, ctx:ASPProgramParser.AspfactContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#aspfact.
    def exitAspfact(self, ctx:ASPProgramParser.AspfactContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#rangedef.
    def enterRangedef(self, ctx:ASPProgramParser.RangedefContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#rangedef.
    def exitRangedef(self, ctx:ASPProgramParser.RangedefContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#normrule.
    def enterNormrule(self, ctx:ASPProgramParser.NormruleContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#normrule.
    def exitNormrule(self, ctx:ASPProgramParser.NormruleContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#constraint.
    def enterConstraint(self, ctx:ASPProgramParser.ConstraintContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#constraint.
    def exitConstraint(self, ctx:ASPProgramParser.ConstraintContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#choice.
    def enterChoice(self, ctx:ASPProgramParser.ChoiceContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#choice.
    def exitChoice(self, ctx:ASPProgramParser.ChoiceContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#head.
    def enterHead(self, ctx:ASPProgramParser.HeadContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#head.
    def exitHead(self, ctx:ASPProgramParser.HeadContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#body.
    def enterBody(self, ctx:ASPProgramParser.BodyContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#body.
    def exitBody(self, ctx:ASPProgramParser.BodyContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#list_literals.
    def enterList_literals(self, ctx:ASPProgramParser.List_literalsContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#list_literals.
    def exitList_literals(self, ctx:ASPProgramParser.List_literalsContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#list_ext_literals_expressions.
    def enterList_ext_literals_expressions(self, ctx:ASPProgramParser.List_ext_literals_expressionsContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#list_ext_literals_expressions.
    def exitList_ext_literals_expressions(self, ctx:ASPProgramParser.List_ext_literals_expressionsContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#expression.
    def enterExpression(self, ctx:ASPProgramParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#expression.
    def exitExpression(self, ctx:ASPProgramParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#num_expression.
    def enterNum_expression(self, ctx:ASPProgramParser.Num_expressionContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#num_expression.
    def exitNum_expression(self, ctx:ASPProgramParser.Num_expressionContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#ext_literal.
    def enterExt_literal(self, ctx:ASPProgramParser.Ext_literalContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#ext_literal.
    def exitExt_literal(self, ctx:ASPProgramParser.Ext_literalContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#literal.
    def enterLiteral(self, ctx:ASPProgramParser.LiteralContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#literal.
    def exitLiteral(self, ctx:ASPProgramParser.LiteralContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#pos_literal.
    def enterPos_literal(self, ctx:ASPProgramParser.Pos_literalContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#pos_literal.
    def exitPos_literal(self, ctx:ASPProgramParser.Pos_literalContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#list_parameters.
    def enterList_parameters(self, ctx:ASPProgramParser.List_parametersContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#list_parameters.
    def exitList_parameters(self, ctx:ASPProgramParser.List_parametersContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#predicate.
    def enterPredicate(self, ctx:ASPProgramParser.PredicateContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#predicate.
    def exitPredicate(self, ctx:ASPProgramParser.PredicateContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#identifier.
    def enterIdentifier(self, ctx:ASPProgramParser.IdentifierContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#identifier.
    def exitIdentifier(self, ctx:ASPProgramParser.IdentifierContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#constant.
    def enterConstant(self, ctx:ASPProgramParser.ConstantContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#constant.
    def exitConstant(self, ctx:ASPProgramParser.ConstantContext):
        pass


    # Enter a parse tree produced by ASPProgramParser#variable.
    def enterVariable(self, ctx:ASPProgramParser.VariableContext):
        pass

    # Exit a parse tree produced by ASPProgramParser#variable.
    def exitVariable(self, ctx:ASPProgramParser.VariableContext):
        pass



del ASPProgramParser