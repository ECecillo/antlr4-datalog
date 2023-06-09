""" Main file for the project that will run the program. """

from antlr4 import FileStream, CommonTokenStream
from DatalogParser import DatalogParser
from DatalogLexer import DatalogLexer
from DatalogInterpretVisitor import MyDatalogVisitor
# from DatalogTypeVisitor import DatalogTypeVisitor

from datalog_types import AggregateFunction, Fact, Predicate, Rule
from utils import datalog_engine_evaluation

from display_database import print_database


print(" ==== MIF14 - Base de données déductives - Datalog Engine Extension for Aggregates Functions ====")

def main():
    # data/insertion_test.dl ✅
    # data/column_decl.dl ✅
    # data/basic_instruction.dl
    # data/facts_test.dl
    # data/clause_parse.dl
    # "data/sample_test.dl"
    # "data/sample_test2.dl"
    input_file = "data/sample_test2.dl"
    input_stream = FileStream(input_file)
    lexer = DatalogLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DatalogParser(token_stream)
    tree = parser.program()

    # visitor = DatalogTypeVisitor()
    visitor = MyDatalogVisitor()
    visitor.visit(tree)
    print(f'visitor rules : {visitor.rulesToEvaluate}')
    print_database(visitor)
 
    print("\n ===================== Starting the evaluation ================= \n")

    
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
