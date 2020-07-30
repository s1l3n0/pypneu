# Generated from /Users/giovanni/dev/pypneu/grammars/ASPProgram.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("\u00b9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\3\2\7")
        buf.write("\2\62\n\2\f\2\16\2\65\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3?\n\3\3\3\5\3B\n\3\3\4\3\4\5\4F\n\4\3\5\3\5\5")
        buf.write("\5J\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\5\t_\n\t\3\t\3\t\3\t\3")
        buf.write("\t\5\te\n\t\3\n\3\n\5\ni\n\n\3\13\3\13\5\13m\n\13\3\f")
        buf.write("\3\f\3\f\5\fr\n\f\3\r\3\r\5\rv\n\r\3\r\3\r\5\rz\n\r\3")
        buf.write("\16\3\16\3\16\3\16\5\16\u0080\n\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u0087\n\16\3\17\3\17\5\17\u008b\n\17\3\17\3")
        buf.write("\17\3\17\5\17\u0090\n\17\3\20\5\20\u0093\n\20\3\20\3\20")
        buf.write("\3\21\5\21\u0098\n\21\3\21\3\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\5\22\u00a1\n\22\3\23\3\23\3\23\5\23\u00a6\n\23\3\23")
        buf.write("\3\23\3\23\5\23\u00ab\n\23\3\23\3\23\5\23\u00af\n\23\3")
        buf.write("\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\27\2\2\30\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,\2\5\3\2\3")
        buf.write("\4\3\2\r\22\3\2\24\25\2\u00c1\2\63\3\2\2\2\4A\3\2\2\2")
        buf.write("\6E\3\2\2\2\bI\3\2\2\2\nM\3\2\2\2\fT\3\2\2\2\16Y\3\2\2")
        buf.write("\2\20^\3\2\2\2\22h\3\2\2\2\24l\3\2\2\2\26n\3\2\2\2\30")
        buf.write("u\3\2\2\2\32\177\3\2\2\2\34\u008a\3\2\2\2\36\u0092\3\2")
        buf.write("\2\2 \u0097\3\2\2\2\"\u009b\3\2\2\2$\u00aa\3\2\2\2&\u00b0")
        buf.write("\3\2\2\2(\u00b2\3\2\2\2*\u00b4\3\2\2\2,\u00b6\3\2\2\2")
        buf.write(".\62\5\4\3\2/\62\5\b\5\2\60\62\5\6\4\2\61.\3\2\2\2\61")
        buf.write("/\3\2\2\2\61\60\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63")
        buf.write("\64\3\2\2\2\64\66\3\2\2\2\65\63\3\2\2\2\66\67\7\2\2\3")
        buf.write("\67\3\3\2\2\289\7\27\2\29:\5\26\f\2:;\7\7\2\2;B\3\2\2")
        buf.write("\2<>\t\2\2\2=?\5\26\f\2>=\3\2\2\2>?\3\2\2\2?@\3\2\2\2")
        buf.write("@B\7\7\2\2A8\3\2\2\2A<\3\2\2\2B\5\3\2\2\2CF\5\f\7\2DF")
        buf.write("\5\16\b\2EC\3\2\2\2ED\3\2\2\2F\7\3\2\2\2GJ\5\22\n\2HJ")
        buf.write("\5\n\6\2IG\3\2\2\2IH\3\2\2\2JK\3\2\2\2KL\7\7\2\2L\t\3")
        buf.write("\2\2\2MN\5(\25\2NO\7\t\2\2OP\7\31\2\2PQ\7\30\2\2QR\7\31")
        buf.write("\2\2RS\7\n\2\2S\13\3\2\2\2TU\5\22\n\2UV\7\6\2\2VW\5\24")
        buf.write("\13\2WX\7\7\2\2X\r\3\2\2\2YZ\7\6\2\2Z[\5\24\13\2[\\\7")
        buf.write("\7\2\2\\\17\3\2\2\2]_\7\31\2\2^]\3\2\2\2^_\3\2\2\2_`\3")
        buf.write("\2\2\2`a\7\13\2\2ab\5\26\f\2bd\7\f\2\2ce\7\31\2\2dc\3")
        buf.write("\2\2\2de\3\2\2\2e\21\3\2\2\2fi\5 \21\2gi\5\20\t\2hf\3")
        buf.write("\2\2\2hg\3\2\2\2i\23\3\2\2\2jm\5\30\r\2km\5\20\t\2lj\3")
        buf.write("\2\2\2lk\3\2\2\2m\25\3\2\2\2nq\5 \21\2op\7\b\2\2pr\5\26")
        buf.write("\f\2qo\3\2\2\2qr\3\2\2\2r\27\3\2\2\2sv\5\36\20\2tv\5\32")
        buf.write("\16\2us\3\2\2\2ut\3\2\2\2vy\3\2\2\2wx\7\b\2\2xz\5\30\r")
        buf.write("\2yw\3\2\2\2yz\3\2\2\2z\31\3\2\2\2{\u0080\5(\25\2|\u0080")
        buf.write("\5,\27\2}\u0080\7\31\2\2~\u0080\5\34\17\2\177{\3\2\2\2")
        buf.write("\177|\3\2\2\2\177}\3\2\2\2\177~\3\2\2\2\u0080\u0081\3")
        buf.write("\2\2\2\u0081\u0086\t\3\2\2\u0082\u0087\7\32\2\2\u0083")
        buf.write("\u0087\7\33\2\2\u0084\u0087\7\31\2\2\u0085\u0087\5\34")
        buf.write("\17\2\u0086\u0082\3\2\2\2\u0086\u0083\3\2\2\2\u0086\u0084")
        buf.write("\3\2\2\2\u0086\u0085\3\2\2\2\u0087\33\3\2\2\2\u0088\u008b")
        buf.write("\5,\27\2\u0089\u008b\7\31\2\2\u008a\u0088\3\2\2\2\u008a")
        buf.write("\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008f\t\4\2\2")
        buf.write("\u008d\u0090\5,\27\2\u008e\u0090\7\31\2\2\u008f\u008d")
        buf.write("\3\2\2\2\u008f\u008e\3\2\2\2\u0090\35\3\2\2\2\u0091\u0093")
        buf.write("\7\23\2\2\u0092\u0091\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write("\u0094\3\2\2\2\u0094\u0095\5 \21\2\u0095\37\3\2\2\2\u0096")
        buf.write("\u0098\7\25\2\2\u0097\u0096\3\2\2\2\u0097\u0098\3\2\2")
        buf.write("\2\u0098\u0099\3\2\2\2\u0099\u009a\5\"\22\2\u009a!\3\2")
        buf.write("\2\2\u009b\u00a0\5&\24\2\u009c\u009d\7\t\2\2\u009d\u009e")
        buf.write("\5$\23\2\u009e\u009f\7\n\2\2\u009f\u00a1\3\2\2\2\u00a0")
        buf.write("\u009c\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1#\3\2\2\2\u00a2")
        buf.write("\u00ab\5(\25\2\u00a3\u00ab\5,\27\2\u00a4\u00a6\7\25\2")
        buf.write("\2\u00a5\u00a4\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7")
        buf.write("\3\2\2\2\u00a7\u00ab\5*\26\2\u00a8\u00ab\5\"\22\2\u00a9")
        buf.write("\u00ab\5\34\17\2\u00aa\u00a2\3\2\2\2\u00aa\u00a3\3\2\2")
        buf.write("\2\u00aa\u00a5\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00a9")
        buf.write("\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00ad\7\b\2\2\u00ad")
        buf.write("\u00af\5$\23\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2")
        buf.write("\u00af%\3\2\2\2\u00b0\u00b1\7\32\2\2\u00b1\'\3\2\2\2\u00b2")
        buf.write("\u00b3\7\32\2\2\u00b3)\3\2\2\2\u00b4\u00b5\7\31\2\2\u00b5")
        buf.write("+\3\2\2\2\u00b6\u00b7\7\33\2\2\u00b7-\3\2\2\2\31\61\63")
        buf.write(">AEI^dhlquy\177\u0086\u008a\u008f\u0092\u0097\u00a0\u00a5")
        buf.write("\u00aa\u00ae")
        return buf.getvalue()


class ASPProgramParser ( Parser ):

    grammarFileName = "ASPProgram.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'hide'", "'show'", "<INVALID>", "':-'", 
                     "'.'", "','", "'('", "')'", "'{'", "'}'", "'='", "'!='", 
                     "'>'", "'<'", "'>='", "'<='", "'not'", "'+'", "'-'", 
                     "'_'", "'#domain'", "'..'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "WS", "ENTAILS", 
                      "DOT", "COMMA", "LPAR", "RPAR", "LACC", "RACC", "EQ", 
                      "NEQ", "GT", "LT", "GE", "LE", "NOT", "PLUS", "MINUS", 
                      "UNDERSCORE", "DOMAIN", "RANGELEX", "INTEGER", "IDENTIFIER", 
                      "VARIABLE", "SINGLE_LINE_COMMENT", "MULTILINE_COMMENT" ]

    RULE_program = 0
    RULE_directive = 1
    RULE_asprule = 2
    RULE_aspfact = 3
    RULE_rangedef = 4
    RULE_normrule = 5
    RULE_constraint = 6
    RULE_choice = 7
    RULE_head = 8
    RULE_body = 9
    RULE_list_literals = 10
    RULE_list_ext_literals_expressions = 11
    RULE_expression = 12
    RULE_num_expression = 13
    RULE_ext_literal = 14
    RULE_literal = 15
    RULE_pos_literal = 16
    RULE_list_parameters = 17
    RULE_predicate = 18
    RULE_identifier = 19
    RULE_constant = 20
    RULE_variable = 21

    ruleNames =  [ "program", "directive", "asprule", "aspfact", "rangedef", 
                   "normrule", "constraint", "choice", "head", "body", "list_literals", 
                   "list_ext_literals_expressions", "expression", "num_expression", 
                   "ext_literal", "literal", "pos_literal", "list_parameters", 
                   "predicate", "identifier", "constant", "variable" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    WS=3
    ENTAILS=4
    DOT=5
    COMMA=6
    LPAR=7
    RPAR=8
    LACC=9
    RACC=10
    EQ=11
    NEQ=12
    GT=13
    LT=14
    GE=15
    LE=16
    NOT=17
    PLUS=18
    MINUS=19
    UNDERSCORE=20
    DOMAIN=21
    RANGELEX=22
    INTEGER=23
    IDENTIFIER=24
    VARIABLE=25
    SINGLE_LINE_COMMENT=26
    MULTILINE_COMMENT=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ASPProgramParser.EOF, 0)

        def directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASPProgramParser.DirectiveContext)
            else:
                return self.getTypedRuleContext(ASPProgramParser.DirectiveContext,i)


        def aspfact(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASPProgramParser.AspfactContext)
            else:
                return self.getTypedRuleContext(ASPProgramParser.AspfactContext,i)


        def asprule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASPProgramParser.AspruleContext)
            else:
                return self.getTypedRuleContext(ASPProgramParser.AspruleContext,i)


        def getRuleIndex(self):
            return ASPProgramParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ASPProgramParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ASPProgramParser.T__0) | (1 << ASPProgramParser.T__1) | (1 << ASPProgramParser.ENTAILS) | (1 << ASPProgramParser.LACC) | (1 << ASPProgramParser.MINUS) | (1 << ASPProgramParser.DOMAIN) | (1 << ASPProgramParser.INTEGER) | (1 << ASPProgramParser.IDENTIFIER))) != 0):
                self.state = 47
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 44
                    self.directive()
                    pass

                elif la_ == 2:
                    self.state = 45
                    self.aspfact()
                    pass

                elif la_ == 3:
                    self.state = 46
                    self.asprule()
                    pass


                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(ASPProgramParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOMAIN(self):
            return self.getToken(ASPProgramParser.DOMAIN, 0)

        def list_literals(self):
            return self.getTypedRuleContext(ASPProgramParser.List_literalsContext,0)


        def DOT(self):
            return self.getToken(ASPProgramParser.DOT, 0)

        def getRuleIndex(self):
            return ASPProgramParser.RULE_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirective" ):
                listener.enterDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirective" ):
                listener.exitDirective(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirective" ):
                return visitor.visitDirective(self)
            else:
                return visitor.visitChildren(self)




    def directive(self):

        localctx = ASPProgramParser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_directive)
        self._la = 0 # Token type
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ASPProgramParser.DOMAIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(ASPProgramParser.DOMAIN)
                self.state = 55
                self.list_literals()
                self.state = 56
                self.match(ASPProgramParser.DOT)
                pass
            elif token in [ASPProgramParser.T__0, ASPProgramParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                _la = self._input.LA(1)
                if not(_la==ASPProgramParser.T__0 or _la==ASPProgramParser.T__1):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ASPProgramParser.MINUS or _la==ASPProgramParser.IDENTIFIER:
                    self.state = 59
                    self.list_literals()


                self.state = 62
                self.match(ASPProgramParser.DOT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AspruleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normrule(self):
            return self.getTypedRuleContext(ASPProgramParser.NormruleContext,0)


        def constraint(self):
            return self.getTypedRuleContext(ASPProgramParser.ConstraintContext,0)


        def getRuleIndex(self):
            return ASPProgramParser.RULE_asprule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsprule" ):
                listener.enterAsprule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsprule" ):
                listener.exitAsprule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsprule" ):
                return visitor.visitAsprule(self)
            else:
                return visitor.visitChildren(self)




    def asprule(self):

        localctx = ASPProgramParser.AspruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_asprule)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ASPProgramParser.LACC, ASPProgramParser.MINUS, ASPProgramParser.INTEGER, ASPProgramParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.normrule()
                pass
            elif token in [ASPProgramParser.ENTAILS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.constraint()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AspfactContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(ASPProgramParser.DOT, 0)

        def head(self):
            return self.getTypedRuleContext(ASPProgramParser.HeadContext,0)


        def rangedef(self):
            return self.getTypedRuleContext(ASPProgramParser.RangedefContext,0)


        def getRuleIndex(self):
            return ASPProgramParser.RULE_aspfact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAspfact" ):
                listener.enterAspfact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAspfact" ):
                listener.exitAspfact(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAspfact" ):
                return visitor.visitAspfact(self)
            else:
                return visitor.visitChildren(self)




    def aspfact(self):

        localctx = ASPProgramParser.AspfactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_aspfact)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 69
                self.head()
                pass

            elif la_ == 2:
                self.state = 70
                self.rangedef()
                pass


            self.state = 73
            self.match(ASPProgramParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangedefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.rangemin = None # Token
            self.rangemax = None # Token

        def identifier(self):
            return self.getTypedRuleContext(ASPProgramParser.IdentifierContext,0)


        def LPAR(self):
            return self.getToken(ASPProgramParser.LPAR, 0)

        def RANGELEX(self):
            return self.getToken(ASPProgramParser.RANGELEX, 0)

        def RPAR(self):
            return self.getToken(ASPProgramParser.RPAR, 0)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(ASPProgramParser.INTEGER)
            else:
                return self.getToken(ASPProgramParser.INTEGER, i)

        def getRuleIndex(self):
            return ASPProgramParser.RULE_rangedef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRangedef" ):
                listener.enterRangedef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRangedef" ):
                listener.exitRangedef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRangedef" ):
                return visitor.visitRangedef(self)
            else:
                return visitor.visitChildren(self)




    def rangedef(self):

        localctx = ASPProgramParser.RangedefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_rangedef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.identifier()
            self.state = 76
            self.match(ASPProgramParser.LPAR)
            self.state = 77
            localctx.rangemin = self.match(ASPProgramParser.INTEGER)
            self.state = 78
            self.match(ASPProgramParser.RANGELEX)
            self.state = 79
            localctx.rangemax = self.match(ASPProgramParser.INTEGER)
            self.state = 80
            self.match(ASPProgramParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormruleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def head(self):
            return self.getTypedRuleContext(ASPProgramParser.HeadContext,0)


        def ENTAILS(self):
            return self.getToken(ASPProgramParser.ENTAILS, 0)

        def body(self):
            return self.getTypedRuleContext(ASPProgramParser.BodyContext,0)


        def DOT(self):
            return self.getToken(ASPProgramParser.DOT, 0)

        def getRuleIndex(self):
            return ASPProgramParser.RULE_normrule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormrule" ):
                listener.enterNormrule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormrule" ):
                listener.exitNormrule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormrule" ):
                return visitor.visitNormrule(self)
            else:
                return visitor.visitChildren(self)




    def normrule(self):

        localctx = ASPProgramParser.NormruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_normrule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.head()
            self.state = 83
            self.match(ASPProgramParser.ENTAILS)
            self.state = 84
            self.body()
            self.state = 85
            self.match(ASPProgramParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTAILS(self):
            return self.getToken(ASPProgramParser.ENTAILS, 0)

        def body(self):
            return self.getTypedRuleContext(ASPProgramParser.BodyContext,0)


        def DOT(self):
            return self.getToken(ASPProgramParser.DOT, 0)

        def getRuleIndex(self):
            return ASPProgramParser.RULE_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraint" ):
                listener.enterConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraint" ):
                listener.exitConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstraint" ):
                return visitor.visitConstraint(self)
            else:
                return visitor.visitChildren(self)




    def constraint(self):

        localctx = ASPProgramParser.ConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(ASPProgramParser.ENTAILS)
            self.state = 88
            self.body()
            self.state = 89
            self.match(ASPProgramParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChoiceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.choicemin = None # Token
            self.choicemax = None # Token

        def LACC(self):
            return self.getToken(ASPProgramParser.LACC, 0)

        def list_literals(self):
            return self.getTypedRuleContext(ASPProgramParser.List_literalsContext,0)


        def RACC(self):
            return self.getToken(ASPProgramParser.RACC, 0)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(ASPProgramParser.INTEGER)
            else:
                return self.getToken(ASPProgramParser.INTEGER, i)

        def getRuleIndex(self):
            return ASPProgramParser.RULE_choice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChoice" ):
                listener.enterChoice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChoice" ):
                listener.exitChoice(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChoice" ):
                return visitor.visitChoice(self)
            else:
                return visitor.visitChildren(self)




    def choice(self):

        localctx = ASPProgramParser.ChoiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_choice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ASPProgramParser.INTEGER:
                self.state = 91
                localctx.choicemin = self.match(ASPProgramParser.INTEGER)


            self.state = 94
            self.match(ASPProgramParser.LACC)
            self.state = 95
            self.list_literals()
            self.state = 96
            self.match(ASPProgramParser.RACC)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ASPProgramParser.INTEGER:
                self.state = 97
                localctx.choicemax = self.match(ASPProgramParser.INTEGER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeadContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ASPProgramParser.LiteralContext,0)


        def choice(self):
            return self.getTypedRuleContext(ASPProgramParser.ChoiceContext,0)


        def getRuleIndex(self):
            return ASPProgramParser.RULE_head

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHead" ):
                listener.enterHead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHead" ):
                listener.exitHead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHead" ):
                return visitor.visitHead(self)
            else:
                return visitor.visitChildren(self)




    def head(self):

        localctx = ASPProgramParser.HeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_head)
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ASPProgramParser.MINUS, ASPProgramParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.literal()
                pass
            elif token in [ASPProgramParser.LACC, ASPProgramParser.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.choice()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_ext_literals_expressions(self):
            return self.getTypedRuleContext(ASPProgramParser.List_ext_literals_expressionsContext,0)


        def choice(self):
            return self.getTypedRuleContext(ASPProgramParser.ChoiceContext,0)


        def getRuleIndex(self):
            return ASPProgramParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = ASPProgramParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_body)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.list_ext_literals_expressions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.choice()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literalsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ASPProgramParser.LiteralContext,0)


        def COMMA(self):
            return self.getToken(ASPProgramParser.COMMA, 0)

        def list_literals(self):
            return self.getTypedRuleContext(ASPProgramParser.List_literalsContext,0)


        def getRuleIndex(self):
            return ASPProgramParser.RULE_list_literals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_literals" ):
                listener.enterList_literals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_literals" ):
                listener.exitList_literals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literals" ):
                return visitor.visitList_literals(self)
            else:
                return visitor.visitChildren(self)




    def list_literals(self):

        localctx = ASPProgramParser.List_literalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.literal()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ASPProgramParser.COMMA:
                self.state = 109
                self.match(ASPProgramParser.COMMA)
                self.state = 110
                self.list_literals()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_ext_literals_expressionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ext_literal(self):
            return self.getTypedRuleContext(ASPProgramParser.Ext_literalContext,0)


        def expression(self):
            return self.getTypedRuleContext(ASPProgramParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ASPProgramParser.COMMA, 0)

        def list_ext_literals_expressions(self):
            return self.getTypedRuleContext(ASPProgramParser.List_ext_literals_expressionsContext,0)


        def getRuleIndex(self):
            return ASPProgramParser.RULE_list_ext_literals_expressions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_ext_literals_expressions" ):
                listener.enterList_ext_literals_expressions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_ext_literals_expressions" ):
                listener.exitList_ext_literals_expressions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_ext_literals_expressions" ):
                return visitor.visitList_ext_literals_expressions(self)
            else:
                return visitor.visitChildren(self)




    def list_ext_literals_expressions(self):

        localctx = ASPProgramParser.List_ext_literals_expressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_ext_literals_expressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 113
                self.ext_literal()
                pass

            elif la_ == 2:
                self.state = 114
                self.expression()
                pass


            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ASPProgramParser.COMMA:
                self.state = 117
                self.match(ASPProgramParser.COMMA)
                self.state = 118
                self.list_ext_literals_expressions()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(ASPProgramParser.EQ, 0)

        def NEQ(self):
            return self.getToken(ASPProgramParser.NEQ, 0)

        def LT(self):
            return self.getToken(ASPProgramParser.LT, 0)

        def LE(self):
            return self.getToken(ASPProgramParser.LE, 0)

        def GT(self):
            return self.getToken(ASPProgramParser.GT, 0)

        def GE(self):
            return self.getToken(ASPProgramParser.GE, 0)

        def identifier(self):
            return self.getTypedRuleContext(ASPProgramParser.IdentifierContext,0)


        def variable(self):
            return self.getTypedRuleContext(ASPProgramParser.VariableContext,0)


        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(ASPProgramParser.INTEGER)
            else:
                return self.getToken(ASPProgramParser.INTEGER, i)

        def num_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASPProgramParser.Num_expressionContext)
            else:
                return self.getTypedRuleContext(ASPProgramParser.Num_expressionContext,i)


        def IDENTIFIER(self):
            return self.getToken(ASPProgramParser.IDENTIFIER, 0)

        def VARIABLE(self):
            return self.getToken(ASPProgramParser.VARIABLE, 0)

        def getRuleIndex(self):
            return ASPProgramParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ASPProgramParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 121
                self.identifier()
                pass

            elif la_ == 2:
                self.state = 122
                self.variable()
                pass

            elif la_ == 3:
                self.state = 123
                self.match(ASPProgramParser.INTEGER)
                pass

            elif la_ == 4:
                self.state = 124
                self.num_expression()
                pass


            self.state = 127
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ASPProgramParser.EQ) | (1 << ASPProgramParser.NEQ) | (1 << ASPProgramParser.GT) | (1 << ASPProgramParser.LT) | (1 << ASPProgramParser.GE) | (1 << ASPProgramParser.LE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 128
                self.match(ASPProgramParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 129
                self.match(ASPProgramParser.VARIABLE)
                pass

            elif la_ == 3:
                self.state = 130
                self.match(ASPProgramParser.INTEGER)
                pass

            elif la_ == 4:
                self.state = 131
                self.num_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Num_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(ASPProgramParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ASPProgramParser.MINUS, 0)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASPProgramParser.VariableContext)
            else:
                return self.getTypedRuleContext(ASPProgramParser.VariableContext,i)


        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(ASPProgramParser.INTEGER)
            else:
                return self.getToken(ASPProgramParser.INTEGER, i)

        def getRuleIndex(self):
            return ASPProgramParser.RULE_num_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum_expression" ):
                listener.enterNum_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum_expression" ):
                listener.exitNum_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum_expression" ):
                return visitor.visitNum_expression(self)
            else:
                return visitor.visitChildren(self)




    def num_expression(self):

        localctx = ASPProgramParser.Num_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_num_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ASPProgramParser.VARIABLE]:
                self.state = 134
                self.variable()
                pass
            elif token in [ASPProgramParser.INTEGER]:
                self.state = 135
                self.match(ASPProgramParser.INTEGER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 138
            _la = self._input.LA(1)
            if not(_la==ASPProgramParser.PLUS or _la==ASPProgramParser.MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ASPProgramParser.VARIABLE]:
                self.state = 139
                self.variable()
                pass
            elif token in [ASPProgramParser.INTEGER]:
                self.state = 140
                self.match(ASPProgramParser.INTEGER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ext_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ASPProgramParser.LiteralContext,0)


        def NOT(self):
            return self.getToken(ASPProgramParser.NOT, 0)

        def getRuleIndex(self):
            return ASPProgramParser.RULE_ext_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExt_literal" ):
                listener.enterExt_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExt_literal" ):
                listener.exitExt_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExt_literal" ):
                return visitor.visitExt_literal(self)
            else:
                return visitor.visitChildren(self)




    def ext_literal(self):

        localctx = ASPProgramParser.Ext_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ext_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ASPProgramParser.NOT:
                self.state = 143
                self.match(ASPProgramParser.NOT)


            self.state = 146
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pos_literal(self):
            return self.getTypedRuleContext(ASPProgramParser.Pos_literalContext,0)


        def MINUS(self):
            return self.getToken(ASPProgramParser.MINUS, 0)

        def getRuleIndex(self):
            return ASPProgramParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ASPProgramParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ASPProgramParser.MINUS:
                self.state = 148
                self.match(ASPProgramParser.MINUS)


            self.state = 151
            self.pos_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pos_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate(self):
            return self.getTypedRuleContext(ASPProgramParser.PredicateContext,0)


        def LPAR(self):
            return self.getToken(ASPProgramParser.LPAR, 0)

        def list_parameters(self):
            return self.getTypedRuleContext(ASPProgramParser.List_parametersContext,0)


        def RPAR(self):
            return self.getToken(ASPProgramParser.RPAR, 0)

        def getRuleIndex(self):
            return ASPProgramParser.RULE_pos_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPos_literal" ):
                listener.enterPos_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPos_literal" ):
                listener.exitPos_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPos_literal" ):
                return visitor.visitPos_literal(self)
            else:
                return visitor.visitChildren(self)




    def pos_literal(self):

        localctx = ASPProgramParser.Pos_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_pos_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.predicate()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ASPProgramParser.LPAR:
                self.state = 154
                self.match(ASPProgramParser.LPAR)
                self.state = 155
                self.list_parameters()
                self.state = 156
                self.match(ASPProgramParser.RPAR)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_parametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ASPProgramParser.IdentifierContext,0)


        def variable(self):
            return self.getTypedRuleContext(ASPProgramParser.VariableContext,0)


        def constant(self):
            return self.getTypedRuleContext(ASPProgramParser.ConstantContext,0)


        def pos_literal(self):
            return self.getTypedRuleContext(ASPProgramParser.Pos_literalContext,0)


        def num_expression(self):
            return self.getTypedRuleContext(ASPProgramParser.Num_expressionContext,0)


        def COMMA(self):
            return self.getToken(ASPProgramParser.COMMA, 0)

        def list_parameters(self):
            return self.getTypedRuleContext(ASPProgramParser.List_parametersContext,0)


        def MINUS(self):
            return self.getToken(ASPProgramParser.MINUS, 0)

        def getRuleIndex(self):
            return ASPProgramParser.RULE_list_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_parameters" ):
                listener.enterList_parameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_parameters" ):
                listener.exitList_parameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_parameters" ):
                return visitor.visitList_parameters(self)
            else:
                return visitor.visitChildren(self)




    def list_parameters(self):

        localctx = ASPProgramParser.List_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_list_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 160
                self.identifier()
                pass

            elif la_ == 2:
                self.state = 161
                self.variable()
                pass

            elif la_ == 3:
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ASPProgramParser.MINUS:
                    self.state = 162
                    self.match(ASPProgramParser.MINUS)


                self.state = 165
                self.constant()
                pass

            elif la_ == 4:
                self.state = 166
                self.pos_literal()
                pass

            elif la_ == 5:
                self.state = 167
                self.num_expression()
                pass


            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ASPProgramParser.COMMA:
                self.state = 170
                self.match(ASPProgramParser.COMMA)
                self.state = 171
                self.list_parameters()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ASPProgramParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ASPProgramParser.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate" ):
                return visitor.visitPredicate(self)
            else:
                return visitor.visitChildren(self)




    def predicate(self):

        localctx = ASPProgramParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(ASPProgramParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ASPProgramParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ASPProgramParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = ASPProgramParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(ASPProgramParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(ASPProgramParser.INTEGER, 0)

        def getRuleIndex(self):
            return ASPProgramParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = ASPProgramParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(ASPProgramParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(ASPProgramParser.VARIABLE, 0)

        def getRuleIndex(self):
            return ASPProgramParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = ASPProgramParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(ASPProgramParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





