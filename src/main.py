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
    input_file = "data/facts_test.dl"
    input_stream = FileStream(input_file)
    lexer = DatalogLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DatalogParser(token_stream)
    tree = parser.program()

#    visitor = DatalogTypeVisitor()
    visitor = MyDatalogVisitor()
    visitor.visit(tree)

    # Process the parse tree as needed
    # Testing our algorithm
    # Fact: (predicate, values)
    EDB = [
        Fact('student', ['s1']),
        Fact('student', ['s2']),
        Fact('student', ['s3']),
        Fact('grade', ['s1', '85']),
        Fact('grade', ['s1', '90']),
        Fact('grade', ['s1', '95']),
        Fact('grade', ['s2', '88']),
        Fact('grade', ['s2', '92']),
        Fact('grade', ['s3', '80']),
        Fact('man', ['s1', '95']),
        Fact('man', ['s2', '88']),
        Fact('man', ['s2', '92']),
        Fact('woman', ['s3', '80']),
        Fact('woman', ['s3', '80']),
    ]

    # Rule: (head, body)
    # Body can be a list of Predicates or AggregateFunctions
    datalog_rules = [
        Rule(
            head = Predicate('q', ['I', 'Count', 'Average']), 
            body = [
                Predicate('student', ['I']),
                Predicate('grade', ['I', 'V']),
                AggregateFunction('COUNT', 'V', 'Count'),
                AggregateFunction('AVG', 'V', 'Average')
            ]
        ),
    ]
    results = datalog_engine_evaluation(datalog_rules, EDB)
    for fact in results:
        print(f"{fact.predicate}({fact.values})")

if __name__ == "__main__":
    main()
