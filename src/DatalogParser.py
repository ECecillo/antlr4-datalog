# Generated from Datalog.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,165,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,3,2,
        56,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,
        5,1,5,1,5,3,5,75,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,9,1,9,
        1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        3,11,101,8,11,1,12,1,12,1,12,1,12,1,12,3,12,108,8,12,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,3,13,140,8,13,1,14,1,14,3,14,144,8,14,1,15,1,15,1,16,1,16,
        1,16,1,16,1,16,3,16,153,8,16,1,17,1,17,3,17,157,8,17,1,18,1,18,1,
        18,1,18,3,18,163,8,18,1,18,0,0,19,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,0,2,1,0,7,9,1,0,10,11,163,0,41,1,0,0,0,2,46,
        1,0,0,0,4,55,1,0,0,0,6,57,1,0,0,0,8,64,1,0,0,0,10,74,1,0,0,0,12,
        76,1,0,0,0,14,80,1,0,0,0,16,82,1,0,0,0,18,85,1,0,0,0,20,88,1,0,0,
        0,22,100,1,0,0,0,24,107,1,0,0,0,26,139,1,0,0,0,28,143,1,0,0,0,30,
        145,1,0,0,0,32,152,1,0,0,0,34,156,1,0,0,0,36,162,1,0,0,0,38,40,3,
        4,2,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,
        44,1,0,0,0,43,41,1,0,0,0,44,45,5,0,0,1,45,1,1,0,0,0,46,47,5,18,0,
        0,47,48,5,16,0,0,48,49,3,32,16,0,49,50,5,17,0,0,50,51,5,15,0,0,51,
        3,1,0,0,0,52,56,3,16,8,0,53,56,3,6,3,0,54,56,3,18,9,0,55,52,1,0,
        0,0,55,53,1,0,0,0,55,54,1,0,0,0,56,5,1,0,0,0,57,58,5,13,0,0,58,59,
        5,1,0,0,59,60,5,16,0,0,60,61,3,8,4,0,61,62,5,17,0,0,62,63,5,15,0,
        0,63,7,1,0,0,0,64,65,5,18,0,0,65,66,5,16,0,0,66,67,3,10,5,0,67,68,
        5,17,0,0,68,9,1,0,0,0,69,75,3,12,6,0,70,71,3,12,6,0,71,72,5,14,0,
        0,72,73,3,10,5,0,73,75,1,0,0,0,74,69,1,0,0,0,74,70,1,0,0,0,75,11,
        1,0,0,0,76,77,5,18,0,0,77,78,5,2,0,0,78,79,3,14,7,0,79,13,1,0,0,
        0,80,81,7,0,0,0,81,15,1,0,0,0,82,83,3,22,11,0,83,84,5,15,0,0,84,
        17,1,0,0,0,85,86,3,26,13,0,86,87,5,3,0,0,87,19,1,0,0,0,88,89,3,22,
        11,0,89,90,5,4,0,0,90,21,1,0,0,0,91,92,3,26,13,0,92,93,5,13,0,0,
        93,94,3,24,12,0,94,101,1,0,0,0,95,96,3,28,14,0,96,97,5,16,0,0,97,
        98,3,32,16,0,98,99,5,17,0,0,99,101,1,0,0,0,100,91,1,0,0,0,100,95,
        1,0,0,0,101,23,1,0,0,0,102,103,3,26,13,0,103,104,5,14,0,0,104,105,
        3,24,12,0,105,108,1,0,0,0,106,108,3,26,13,0,107,102,1,0,0,0,107,
        106,1,0,0,0,108,25,1,0,0,0,109,110,3,28,14,0,110,111,5,16,0,0,111,
        112,5,17,0,0,112,140,1,0,0,0,113,114,3,28,14,0,114,115,5,16,0,0,
        115,116,3,32,16,0,116,117,5,17,0,0,117,140,1,0,0,0,118,119,5,12,
        0,0,119,120,5,16,0,0,120,121,3,32,16,0,121,122,5,17,0,0,122,140,
        1,0,0,0,123,140,3,28,14,0,124,125,3,34,17,0,125,126,5,5,0,0,126,
        127,3,34,17,0,127,140,1,0,0,0,128,129,3,34,17,0,129,130,5,6,0,0,
        130,131,3,34,17,0,131,140,1,0,0,0,132,133,5,19,0,0,133,134,5,13,
        0,0,134,135,3,30,15,0,135,136,5,16,0,0,136,137,3,32,16,0,137,138,
        5,17,0,0,138,140,1,0,0,0,139,109,1,0,0,0,139,113,1,0,0,0,139,118,
        1,0,0,0,139,123,1,0,0,0,139,124,1,0,0,0,139,128,1,0,0,0,139,132,
        1,0,0,0,140,27,1,0,0,0,141,144,5,18,0,0,142,144,5,20,0,0,143,141,
        1,0,0,0,143,142,1,0,0,0,144,29,1,0,0,0,145,146,5,18,0,0,146,31,1,
        0,0,0,147,153,3,34,17,0,148,149,3,34,17,0,149,150,5,14,0,0,150,151,
        3,32,16,0,151,153,1,0,0,0,152,147,1,0,0,0,152,148,1,0,0,0,153,33,
        1,0,0,0,154,157,5,19,0,0,155,157,3,36,18,0,156,154,1,0,0,0,156,155,
        1,0,0,0,157,35,1,0,0,0,158,163,5,18,0,0,159,163,5,20,0,0,160,163,
        5,21,0,0,161,163,7,1,0,0,162,158,1,0,0,0,162,159,1,0,0,0,162,160,
        1,0,0,0,162,161,1,0,0,0,163,37,1,0,0,0,10,41,55,74,100,107,139,143,
        152,156,162
    ]

class DatalogParser ( Parser ):

    grammarFileName = "Datalog.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'type'", "':'", "'?'", "'~'", "'='", 
                     "'!='", "'int'", "'string'", "'bool'", "'true'", "'false'", 
                     "<INVALID>", "':-'", "','", "'.'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INTTYPE", 
                      "STRINGTYPE", "BOOLTYPE", "TRUE", "FALSE", "AGGREGATE", 
                      "ASSIGN", "COMA", "DOT", "LEFT_PAR", "RIGHT_PAR", 
                      "IDENTIFIER", "VARIABLE", "STRING", "INTEGER", "COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_fact = 1
    RULE_statement = 2
    RULE_edbTypeDeclaration = 3
    RULE_edbTypeDefinition = 4
    RULE_columnType_l = 5
    RULE_columnType = 6
    RULE_typee = 7
    RULE_assertion = 8
    RULE_query = 9
    RULE_retraction = 10
    RULE_clause = 11
    RULE_body = 12
    RULE_literal = 13
    RULE_predicate_sym = 14
    RULE_external_sym = 15
    RULE_terms_l = 16
    RULE_term = 17
    RULE_constant = 18

    ruleNames =  [ "program", "fact", "statement", "edbTypeDeclaration", 
                   "edbTypeDefinition", "columnType_l", "columnType", "typee", 
                   "assertion", "query", "retraction", "clause", "body", 
                   "literal", "predicate_sym", "external_sym", "terms_l", 
                   "term", "constant" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    INTTYPE=7
    STRINGTYPE=8
    BOOLTYPE=9
    TRUE=10
    FALSE=11
    AGGREGATE=12
    ASSIGN=13
    COMA=14
    DOT=15
    LEFT_PAR=16
    RIGHT_PAR=17
    IDENTIFIER=18
    VARIABLE=19
    STRING=20
    INTEGER=21
    COMMENT=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DatalogParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DatalogParser.StatementContext)
            else:
                return self.getTypedRuleContext(DatalogParser.StatementContext,i)


        def getRuleIndex(self):
            return DatalogParser.RULE_program

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

        localctx = DatalogParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3947520) != 0):
                self.state = 38
                self.statement()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(DatalogParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatalogParser.RULE_fact

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EdbInsertionContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(DatalogParser.IDENTIFIER, 0)
        def LEFT_PAR(self):
            return self.getToken(DatalogParser.LEFT_PAR, 0)
        def terms_l(self):
            return self.getTypedRuleContext(DatalogParser.Terms_lContext,0)

        def RIGHT_PAR(self):
            return self.getToken(DatalogParser.RIGHT_PAR, 0)
        def DOT(self):
            return self.getToken(DatalogParser.DOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdbInsertion" ):
                listener.enterEdbInsertion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdbInsertion" ):
                listener.exitEdbInsertion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdbInsertion" ):
                return visitor.visitEdbInsertion(self)
            else:
                return visitor.visitChildren(self)



    def fact(self):

        localctx = DatalogParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_fact)
        try:
            localctx = DatalogParser.EdbInsertionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(DatalogParser.IDENTIFIER)
            self.state = 47
            self.match(DatalogParser.LEFT_PAR)
            self.state = 48
            self.terms_l()
            self.state = 49
            self.match(DatalogParser.RIGHT_PAR)
            self.state = 50
            self.match(DatalogParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assertion(self):
            return self.getTypedRuleContext(DatalogParser.AssertionContext,0)


        def edbTypeDeclaration(self):
            return self.getTypedRuleContext(DatalogParser.EdbTypeDeclarationContext,0)


        def query(self):
            return self.getTypedRuleContext(DatalogParser.QueryContext,0)


        def getRuleIndex(self):
            return DatalogParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = DatalogParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.assertion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.edbTypeDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.query()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdbTypeDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(DatalogParser.ASSIGN, 0)

        def LEFT_PAR(self):
            return self.getToken(DatalogParser.LEFT_PAR, 0)

        def edbTypeDefinition(self):
            return self.getTypedRuleContext(DatalogParser.EdbTypeDefinitionContext,0)


        def RIGHT_PAR(self):
            return self.getToken(DatalogParser.RIGHT_PAR, 0)

        def DOT(self):
            return self.getToken(DatalogParser.DOT, 0)

        def getRuleIndex(self):
            return DatalogParser.RULE_edbTypeDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdbTypeDeclaration" ):
                listener.enterEdbTypeDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdbTypeDeclaration" ):
                listener.exitEdbTypeDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdbTypeDeclaration" ):
                return visitor.visitEdbTypeDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def edbTypeDeclaration(self):

        localctx = DatalogParser.EdbTypeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_edbTypeDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(DatalogParser.ASSIGN)
            self.state = 58
            self.match(DatalogParser.T__0)
            self.state = 59
            self.match(DatalogParser.LEFT_PAR)
            self.state = 60
            self.edbTypeDefinition()
            self.state = 61
            self.match(DatalogParser.RIGHT_PAR)
            self.state = 62
            self.match(DatalogParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdbTypeDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatalogParser.RULE_edbTypeDefinition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EdbTypeDefinitionBaseContext(EdbTypeDefinitionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.EdbTypeDefinitionContext
            super().__init__(parser)
            self.edb = None # Token
            self.copyFrom(ctx)

        def LEFT_PAR(self):
            return self.getToken(DatalogParser.LEFT_PAR, 0)
        def columnType_l(self):
            return self.getTypedRuleContext(DatalogParser.ColumnType_lContext,0)

        def RIGHT_PAR(self):
            return self.getToken(DatalogParser.RIGHT_PAR, 0)
        def IDENTIFIER(self):
            return self.getToken(DatalogParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdbTypeDefinitionBase" ):
                listener.enterEdbTypeDefinitionBase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdbTypeDefinitionBase" ):
                listener.exitEdbTypeDefinitionBase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdbTypeDefinitionBase" ):
                return visitor.visitEdbTypeDefinitionBase(self)
            else:
                return visitor.visitChildren(self)



    def edbTypeDefinition(self):

        localctx = DatalogParser.EdbTypeDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_edbTypeDefinition)
        try:
            localctx = DatalogParser.EdbTypeDefinitionBaseContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            localctx.edb = self.match(DatalogParser.IDENTIFIER)
            self.state = 65
            self.match(DatalogParser.LEFT_PAR)
            self.state = 66
            self.columnType_l()
            self.state = 67
            self.match(DatalogParser.RIGHT_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnType_lContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatalogParser.RULE_columnType_l

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ColumnTypeListBaseContext(ColumnType_lContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.ColumnType_lContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def columnType(self):
            return self.getTypedRuleContext(DatalogParser.ColumnTypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnTypeListBase" ):
                listener.enterColumnTypeListBase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnTypeListBase" ):
                listener.exitColumnTypeListBase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnTypeListBase" ):
                return visitor.visitColumnTypeListBase(self)
            else:
                return visitor.visitChildren(self)


    class ColumnTypeListContext(ColumnType_lContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.ColumnType_lContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def columnType(self):
            return self.getTypedRuleContext(DatalogParser.ColumnTypeContext,0)

        def COMA(self):
            return self.getToken(DatalogParser.COMA, 0)
        def columnType_l(self):
            return self.getTypedRuleContext(DatalogParser.ColumnType_lContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnTypeList" ):
                listener.enterColumnTypeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnTypeList" ):
                listener.exitColumnTypeList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnTypeList" ):
                return visitor.visitColumnTypeList(self)
            else:
                return visitor.visitChildren(self)



    def columnType_l(self):

        localctx = DatalogParser.ColumnType_lContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_columnType_l)
        try:
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = DatalogParser.ColumnTypeListBaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.columnType()
                pass

            elif la_ == 2:
                localctx = DatalogParser.ColumnTypeListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.columnType()
                self.state = 71
                self.match(DatalogParser.COMA)
                self.state = 72
                self.columnType_l()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatalogParser.RULE_columnType

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ColumnDeclContext(ColumnTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.ColumnTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(DatalogParser.IDENTIFIER, 0)
        def typee(self):
            return self.getTypedRuleContext(DatalogParser.TypeeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnDecl" ):
                listener.enterColumnDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnDecl" ):
                listener.exitColumnDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnDecl" ):
                return visitor.visitColumnDecl(self)
            else:
                return visitor.visitChildren(self)



    def columnType(self):

        localctx = DatalogParser.ColumnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_columnType)
        try:
            localctx = DatalogParser.ColumnDeclContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(DatalogParser.IDENTIFIER)
            self.state = 77
            self.match(DatalogParser.T__1)
            self.state = 78
            self.typee()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatalogParser.RULE_typee

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BasicTypeContext(TypeeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.TypeeContext
            super().__init__(parser)
            self.mytype = None # Token
            self.copyFrom(ctx)

        def INTTYPE(self):
            return self.getToken(DatalogParser.INTTYPE, 0)
        def BOOLTYPE(self):
            return self.getToken(DatalogParser.BOOLTYPE, 0)
        def STRINGTYPE(self):
            return self.getToken(DatalogParser.STRINGTYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasicType" ):
                listener.enterBasicType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasicType" ):
                listener.exitBasicType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicType" ):
                return visitor.visitBasicType(self)
            else:
                return visitor.visitChildren(self)



    def typee(self):

        localctx = DatalogParser.TypeeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typee)
        self._la = 0 # Token type
        try:
            localctx = DatalogParser.BasicTypeContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            localctx.mytype = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
                localctx.mytype = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssertionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatalogParser.RULE_assertion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssertionClauseContext(AssertionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.AssertionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def clause(self):
            return self.getTypedRuleContext(DatalogParser.ClauseContext,0)

        def DOT(self):
            return self.getToken(DatalogParser.DOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssertionClause" ):
                listener.enterAssertionClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssertionClause" ):
                listener.exitAssertionClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssertionClause" ):
                return visitor.visitAssertionClause(self)
            else:
                return visitor.visitChildren(self)



    def assertion(self):

        localctx = DatalogParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assertion)
        try:
            localctx = DatalogParser.AssertionClauseContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.clause()
            self.state = 83
            self.match(DatalogParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatalogParser.RULE_query

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class QueryInstructionContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.QueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(DatalogParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryInstruction" ):
                listener.enterQueryInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryInstruction" ):
                listener.exitQueryInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueryInstruction" ):
                return visitor.visitQueryInstruction(self)
            else:
                return visitor.visitChildren(self)



    def query(self):

        localctx = DatalogParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_query)
        try:
            localctx = DatalogParser.QueryInstructionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.literal()
            self.state = 86
            self.match(DatalogParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetractionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatalogParser.RULE_retraction

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RetractionClauseContext(RetractionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.RetractionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def clause(self):
            return self.getTypedRuleContext(DatalogParser.ClauseContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetractionClause" ):
                listener.enterRetractionClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetractionClause" ):
                listener.exitRetractionClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetractionClause" ):
                return visitor.visitRetractionClause(self)
            else:
                return visitor.visitChildren(self)



    def retraction(self):

        localctx = DatalogParser.RetractionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_retraction)
        try:
            localctx = DatalogParser.RetractionClauseContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.clause()
            self.state = 89
            self.match(DatalogParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatalogParser.RULE_clause

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ClauseFactContext(ClauseContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.ClauseContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicate_sym(self):
            return self.getTypedRuleContext(DatalogParser.Predicate_symContext,0)

        def LEFT_PAR(self):
            return self.getToken(DatalogParser.LEFT_PAR, 0)
        def terms_l(self):
            return self.getTypedRuleContext(DatalogParser.Terms_lContext,0)

        def RIGHT_PAR(self):
            return self.getToken(DatalogParser.RIGHT_PAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClauseFact" ):
                listener.enterClauseFact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClauseFact" ):
                listener.exitClauseFact(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClauseFact" ):
                return visitor.visitClauseFact(self)
            else:
                return visitor.visitChildren(self)


    class ClauseRuleContext(ClauseContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.ClauseContext
            super().__init__(parser)
            self.head = None # LiteralContext
            self.copyFrom(ctx)

        def ASSIGN(self):
            return self.getToken(DatalogParser.ASSIGN, 0)
        def body(self):
            return self.getTypedRuleContext(DatalogParser.BodyContext,0)

        def literal(self):
            return self.getTypedRuleContext(DatalogParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClauseRule" ):
                listener.enterClauseRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClauseRule" ):
                listener.exitClauseRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClauseRule" ):
                return visitor.visitClauseRule(self)
            else:
                return visitor.visitChildren(self)



    def clause(self):

        localctx = DatalogParser.ClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_clause)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = DatalogParser.ClauseRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                localctx.head = self.literal()
                self.state = 92
                self.match(DatalogParser.ASSIGN)
                self.state = 93
                self.body()
                pass

            elif la_ == 2:
                localctx = DatalogParser.ClauseFactContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.predicate_sym()
                self.state = 96
                self.match(DatalogParser.LEFT_PAR)
                self.state = 97
                self.terms_l()
                self.state = 98
                self.match(DatalogParser.RIGHT_PAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatalogParser.RULE_body

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BodyBaseContext(BodyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.BodyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(DatalogParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBodyBase" ):
                listener.enterBodyBase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBodyBase" ):
                listener.exitBodyBase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodyBase" ):
                return visitor.visitBodyBase(self)
            else:
                return visitor.visitChildren(self)


    class BodyListContext(BodyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.BodyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(DatalogParser.LiteralContext,0)

        def COMA(self):
            return self.getToken(DatalogParser.COMA, 0)
        def body(self):
            return self.getTypedRuleContext(DatalogParser.BodyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBodyList" ):
                listener.enterBodyList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBodyList" ):
                listener.exitBodyList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodyList" ):
                return visitor.visitBodyList(self)
            else:
                return visitor.visitChildren(self)



    def body(self):

        localctx = DatalogParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_body)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = DatalogParser.BodyListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.literal()
                self.state = 103
                self.match(DatalogParser.COMA)
                self.state = 104
                self.body()
                pass

            elif la_ == 2:
                localctx = DatalogParser.BodyBaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatalogParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdbQueryContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicate_sym(self):
            return self.getTypedRuleContext(DatalogParser.Predicate_symContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdbQuery" ):
                listener.enterIdbQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdbQuery" ):
                listener.exitIdbQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdbQuery" ):
                return visitor.visitIdbQuery(self)
            else:
                return visitor.visitChildren(self)


    class SomthingContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(DatalogParser.VARIABLE, 0)
        def ASSIGN(self):
            return self.getToken(DatalogParser.ASSIGN, 0)
        def external_sym(self):
            return self.getTypedRuleContext(DatalogParser.External_symContext,0)

        def LEFT_PAR(self):
            return self.getToken(DatalogParser.LEFT_PAR, 0)
        def terms_l(self):
            return self.getTypedRuleContext(DatalogParser.Terms_lContext,0)

        def RIGHT_PAR(self):
            return self.getToken(DatalogParser.RIGHT_PAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSomthing" ):
                listener.enterSomthing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSomthing" ):
                listener.exitSomthing(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSomthing" ):
                return visitor.visitSomthing(self)
            else:
                return visitor.visitChildren(self)


    class NotEqualPredicateContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DatalogParser.TermContext)
            else:
                return self.getTypedRuleContext(DatalogParser.TermContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotEqualPredicate" ):
                listener.enterNotEqualPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotEqualPredicate" ):
                listener.exitNotEqualPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotEqualPredicate" ):
                return visitor.visitNotEqualPredicate(self)
            else:
                return visitor.visitChildren(self)


    class EqPredicateContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DatalogParser.TermContext)
            else:
                return self.getTypedRuleContext(DatalogParser.TermContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqPredicate" ):
                listener.enterEqPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqPredicate" ):
                listener.exitEqPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqPredicate" ):
                return visitor.visitEqPredicate(self)
            else:
                return visitor.visitChildren(self)


    class AggregateDeclContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AGGREGATE(self):
            return self.getToken(DatalogParser.AGGREGATE, 0)
        def LEFT_PAR(self):
            return self.getToken(DatalogParser.LEFT_PAR, 0)
        def terms_l(self):
            return self.getTypedRuleContext(DatalogParser.Terms_lContext,0)

        def RIGHT_PAR(self):
            return self.getToken(DatalogParser.RIGHT_PAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateDecl" ):
                listener.enterAggregateDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateDecl" ):
                listener.exitAggregateDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateDecl" ):
                return visitor.visitAggregateDecl(self)
            else:
                return visitor.visitChildren(self)


    class EmptyPredicateDeclContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicate_sym(self):
            return self.getTypedRuleContext(DatalogParser.Predicate_symContext,0)

        def LEFT_PAR(self):
            return self.getToken(DatalogParser.LEFT_PAR, 0)
        def RIGHT_PAR(self):
            return self.getToken(DatalogParser.RIGHT_PAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyPredicateDecl" ):
                listener.enterEmptyPredicateDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyPredicateDecl" ):
                listener.exitEmptyPredicateDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyPredicateDecl" ):
                return visitor.visitEmptyPredicateDecl(self)
            else:
                return visitor.visitChildren(self)


    class PredicateDeclContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicate_sym(self):
            return self.getTypedRuleContext(DatalogParser.Predicate_symContext,0)

        def LEFT_PAR(self):
            return self.getToken(DatalogParser.LEFT_PAR, 0)
        def terms_l(self):
            return self.getTypedRuleContext(DatalogParser.Terms_lContext,0)

        def RIGHT_PAR(self):
            return self.getToken(DatalogParser.RIGHT_PAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicateDecl" ):
                listener.enterPredicateDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicateDecl" ):
                listener.exitPredicateDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicateDecl" ):
                return visitor.visitPredicateDecl(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = DatalogParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_literal)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = DatalogParser.EmptyPredicateDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.predicate_sym()
                self.state = 110
                self.match(DatalogParser.LEFT_PAR)
                self.state = 111
                self.match(DatalogParser.RIGHT_PAR)
                pass

            elif la_ == 2:
                localctx = DatalogParser.PredicateDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.predicate_sym()
                self.state = 114
                self.match(DatalogParser.LEFT_PAR)
                self.state = 115
                self.terms_l()
                self.state = 116
                self.match(DatalogParser.RIGHT_PAR)
                pass

            elif la_ == 3:
                localctx = DatalogParser.AggregateDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.match(DatalogParser.AGGREGATE)
                self.state = 119
                self.match(DatalogParser.LEFT_PAR)
                self.state = 120
                self.terms_l()
                self.state = 121
                self.match(DatalogParser.RIGHT_PAR)
                pass

            elif la_ == 4:
                localctx = DatalogParser.IdbQueryContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.predicate_sym()
                pass

            elif la_ == 5:
                localctx = DatalogParser.EqPredicateContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 124
                self.term()
                self.state = 125
                self.match(DatalogParser.T__4)
                self.state = 126
                self.term()
                pass

            elif la_ == 6:
                localctx = DatalogParser.NotEqualPredicateContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 128
                self.term()
                self.state = 129
                self.match(DatalogParser.T__5)
                self.state = 130
                self.term()
                pass

            elif la_ == 7:
                localctx = DatalogParser.SomthingContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 132
                self.match(DatalogParser.VARIABLE)
                self.state = 133
                self.match(DatalogParser.ASSIGN)
                self.state = 134
                self.external_sym()
                self.state = 135
                self.match(DatalogParser.LEFT_PAR)
                self.state = 136
                self.terms_l()
                self.state = 137
                self.match(DatalogParser.RIGHT_PAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Predicate_symContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatalogParser.RULE_predicate_sym

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PredicateRelationIdentifierContext(Predicate_symContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.Predicate_symContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(DatalogParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicateRelationIdentifier" ):
                listener.enterPredicateRelationIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicateRelationIdentifier" ):
                listener.exitPredicateRelationIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicateRelationIdentifier" ):
                return visitor.visitPredicateRelationIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class PredicateStringContext(Predicate_symContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.Predicate_symContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(DatalogParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicateString" ):
                listener.enterPredicateString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicateString" ):
                listener.exitPredicateString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicateString" ):
                return visitor.visitPredicateString(self)
            else:
                return visitor.visitChildren(self)



    def predicate_sym(self):

        localctx = DatalogParser.Predicate_symContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_predicate_sym)
        try:
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                localctx = DatalogParser.PredicateRelationIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(DatalogParser.IDENTIFIER)
                pass
            elif token in [20]:
                localctx = DatalogParser.PredicateStringContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(DatalogParser.STRING)
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


    class External_symContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(DatalogParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return DatalogParser.RULE_external_sym

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExternal_sym" ):
                listener.enterExternal_sym(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExternal_sym" ):
                listener.exitExternal_sym(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExternal_sym" ):
                return visitor.visitExternal_sym(self)
            else:
                return visitor.visitChildren(self)




    def external_sym(self):

        localctx = DatalogParser.External_symContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_external_sym)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(DatalogParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Terms_lContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatalogParser.RULE_terms_l

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TermListContext(Terms_lContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.Terms_lContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(DatalogParser.TermContext,0)

        def COMA(self):
            return self.getToken(DatalogParser.COMA, 0)
        def terms_l(self):
            return self.getTypedRuleContext(DatalogParser.Terms_lContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermList" ):
                listener.enterTermList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermList" ):
                listener.exitTermList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermList" ):
                return visitor.visitTermList(self)
            else:
                return visitor.visitChildren(self)


    class TermBaseContext(Terms_lContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.Terms_lContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(DatalogParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermBase" ):
                listener.enterTermBase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermBase" ):
                listener.exitTermBase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermBase" ):
                return visitor.visitTermBase(self)
            else:
                return visitor.visitChildren(self)



    def terms_l(self):

        localctx = DatalogParser.Terms_lContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_terms_l)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = DatalogParser.TermBaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.term()
                pass

            elif la_ == 2:
                localctx = DatalogParser.TermListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.term()
                self.state = 149
                self.match(DatalogParser.COMA)
                self.state = 150
                self.terms_l()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatalogParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TermConstantContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def constant(self):
            return self.getTypedRuleContext(DatalogParser.ConstantContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermConstant" ):
                listener.enterTermConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermConstant" ):
                listener.exitTermConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermConstant" ):
                return visitor.visitTermConstant(self)
            else:
                return visitor.visitChildren(self)


    class TermVariableContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(DatalogParser.VARIABLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermVariable" ):
                listener.enterTermVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermVariable" ):
                listener.exitTermVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermVariable" ):
                return visitor.visitTermVariable(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = DatalogParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_term)
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = DatalogParser.TermVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(DatalogParser.VARIABLE)
                pass
            elif token in [10, 11, 18, 20, 21]:
                localctx = DatalogParser.TermConstantContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.constant()
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


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatalogParser.RULE_constant

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdentifierConstantContext(ConstantContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.ConstantContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(DatalogParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierConstant" ):
                listener.enterIdentifierConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierConstant" ):
                listener.exitIdentifierConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierConstant" ):
                return visitor.visitIdentifierConstant(self)
            else:
                return visitor.visitChildren(self)


    class IntConstantContext(ConstantContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.ConstantContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(DatalogParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntConstant" ):
                listener.enterIntConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntConstant" ):
                listener.exitIntConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntConstant" ):
                return visitor.visitIntConstant(self)
            else:
                return visitor.visitChildren(self)


    class StringConstantContext(ConstantContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.ConstantContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(DatalogParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringConstant" ):
                listener.enterStringConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringConstant" ):
                listener.exitStringConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringConstant" ):
                return visitor.visitStringConstant(self)
            else:
                return visitor.visitChildren(self)


    class BooleanConstantContext(ConstantContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DatalogParser.ConstantContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(DatalogParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(DatalogParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanConstant" ):
                listener.enterBooleanConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanConstant" ):
                listener.exitBooleanConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanConstant" ):
                return visitor.visitBooleanConstant(self)
            else:
                return visitor.visitChildren(self)



    def constant(self):

        localctx = DatalogParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                localctx = DatalogParser.IdentifierConstantContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(DatalogParser.IDENTIFIER)
                pass
            elif token in [20]:
                localctx = DatalogParser.StringConstantContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(DatalogParser.STRING)
                pass
            elif token in [21]:
                localctx = DatalogParser.IntConstantContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.match(DatalogParser.INTEGER)
                pass
            elif token in [10, 11]:
                localctx = DatalogParser.BooleanConstantContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                _la = self._input.LA(1)
                if not(_la==10 or _la==11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
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





