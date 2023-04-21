from ply import lex, yacc

tokens = (
    "VARIABLE",
    "CONSTANT",
    "PREDICATE",
    "COMMA",
    "LPAREN",
    "RPAREN",
    "COLON_DASH"
)

# Define token patterns
t_VARIABLE = r'[A-Z][a-zA-Z0-9_]*'
t_CONSTANT = r'[a-z][a-zA-Z0-9_]*'
t_PREDICATE = r'[A-Z][a-zA-Z0-9_]*'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON_DASH = r':-'

# Define a rule for handling whitespace
t_ignore = " \t\n"

# Define an error handling rule


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
