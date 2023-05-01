""" Main file for the project that will run the program. """

from DatalogParser import DatalogParser
from DatalogLexer import DatalogLexer
from antlr4 import FileStream, CommonTokenStream

from MyDatalogVisitor import MyDatalogVisitor
print(" ==== MIF14 - Base de données déductives - Datalog Engine Extension for Aggregates Functions ====")


def main():
    input_file = "data/insertion_test.dl"
    input_stream = FileStream(input_file)
    lexer = DatalogLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DatalogParser(token_stream)
    tree = parser.program()

    visitor = MyDatalogVisitor()
    visitor.visit(tree)

    # Process the parse tree as needed


if __name__ == "__main__":
    main()
