# Generated from Datalog.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .DatalogParser import DatalogParser
else:
    from DatalogParser import DatalogParser

# This class defines a complete generic visitor for a parse tree produced by DatalogParser.

class DatalogVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DatalogParser#program.
    def visitProgram(self, ctx:DatalogParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#edbInsertion.
    def visitEdbInsertion(self, ctx:DatalogParser.EdbInsertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#statement.
    def visitStatement(self, ctx:DatalogParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#edbTypeDeclaration.
    def visitEdbTypeDeclaration(self, ctx:DatalogParser.EdbTypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#edbTypeDefinitionBase.
    def visitEdbTypeDefinitionBase(self, ctx:DatalogParser.EdbTypeDefinitionBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#columnTypeListBase.
    def visitColumnTypeListBase(self, ctx:DatalogParser.ColumnTypeListBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#columnTypeList.
    def visitColumnTypeList(self, ctx:DatalogParser.ColumnTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#columnDecl.
    def visitColumnDecl(self, ctx:DatalogParser.ColumnDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#basicType.
    def visitBasicType(self, ctx:DatalogParser.BasicTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#assertionClause.
    def visitAssertionClause(self, ctx:DatalogParser.AssertionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#queryInstruction.
    def visitQueryInstruction(self, ctx:DatalogParser.QueryInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#retractionClause.
    def visitRetractionClause(self, ctx:DatalogParser.RetractionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#clauseRule.
    def visitClauseRule(self, ctx:DatalogParser.ClauseRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#clauseFact.
    def visitClauseFact(self, ctx:DatalogParser.ClauseFactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#bodyList.
    def visitBodyList(self, ctx:DatalogParser.BodyListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#bodyBase.
    def visitBodyBase(self, ctx:DatalogParser.BodyBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#literal.
    def visitLiteral(self, ctx:DatalogParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#predicateRelationIdentifier.
    def visitPredicateRelationIdentifier(self, ctx:DatalogParser.PredicateRelationIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#predicateString.
    def visitPredicateString(self, ctx:DatalogParser.PredicateStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#external_sym.
    def visitExternal_sym(self, ctx:DatalogParser.External_symContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#termBase.
    def visitTermBase(self, ctx:DatalogParser.TermBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#termList.
    def visitTermList(self, ctx:DatalogParser.TermListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#termVariable.
    def visitTermVariable(self, ctx:DatalogParser.TermVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#termConstant.
    def visitTermConstant(self, ctx:DatalogParser.TermConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#identifierConstant.
    def visitIdentifierConstant(self, ctx:DatalogParser.IdentifierConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#stringConstant.
    def visitStringConstant(self, ctx:DatalogParser.StringConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#intConstant.
    def visitIntConstant(self, ctx:DatalogParser.IntConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#booleanConstant.
    def visitBooleanConstant(self, ctx:DatalogParser.BooleanConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#aggregateOp.
    def visitAggregateOp(self, ctx:DatalogParser.AggregateOpContext):
        return self.visitChildren(ctx)



del DatalogParser