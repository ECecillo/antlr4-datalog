""" Main file for the project that will run the program. """

from DatalogParser import DatalogParser
from DatalogLexer import DatalogLexer
from antlr4 import FileStream, CommonTokenStream

from DatalogInterpretVisitor import MyDatalogVisitor
from datalog_types import AggregateFunction, Fact, Predicate, Rule
# from datalog_types import AggregateFunction, Fact, Predicate, Rule
from utils import datalog_engine_evaluation
# from DatalogTypeVisitor import DatalogTypeVisitor

print(" ==== MIF14 - Base de données déductives - Datalog Engine Extension for Aggregates Functions ====")


def main():
    # data/insertion_test.dl ✅
    # data/column_decl.dl ✅
    # data/basic_instruction.dl
    # data/facts_test.dl
    # data/clause_parse.dl
    input_file = "data/sample_test.dl"
    input_stream = FileStream(input_file)
    lexer = DatalogLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DatalogParser(token_stream)
    tree = parser.program()

    # visitor = DatalogTypeVisitor()
    visitor = MyDatalogVisitor()
    visitor.visit(tree)
    print(f'visitor database : {visitor.database}')
    print(f'visitor rules : {visitor.rulesToEvaluate}')
# 
#   # Process the parse tree as needed # Testing our algorithm 
    # Fact: (predicate, values) 
    results = datalog_engine_evaluation(visitor.rulesToEvaluate, visitor.database)
    for fact in results:
       print(f"{fact.predicate}({fact.values})")

#     results = datalog_engine_evaluation(datalog_rules, EDB)
#     for fact in results:
#         print(f"{fact.predicate}({fact.values})")

if __name__ == "__main__":
    main()
