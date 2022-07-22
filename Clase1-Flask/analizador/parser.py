from ply.yacc import yacc
import lexer

tokens = lexer.tokens

# precedencia

precedence = (
    ('left', 'MENOS', 'MAS'),
    ('left', 'MULTI', 'DIV'),
    ('right', 'UNARIO'),
)

def p_expression(p):
    """
    expression : term MAS term
               | term MENOS term
    """
    # p contiene los elementos de la gramatica
    #
    # expression : term PLUS term
    #   p[0]     : p[1] p[2] p[3]
    #
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]


def p_expression_term(p):
    """
    expression : term
    """
    p[0] = p[1]


def p_term(p):
    """
    term : factor MULTI factor
         | factor DIV factor
    """
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_term_factor(p):
    """
    term : factor
    """
    p[0] = p[1]


def p_factor_number(p):
    """
    factor : NUMERO
    """
    p[0] = p[1]


def p_factor_unario(p):
    """
    factor : MAS factor
           | MENOS factor %prec UNARIO
    """
    if p[1] == '-':
        p[0] = -p[2]
    else:
        p[0] = p[2]


def p_factor_grouped(p):
    """
    factor : PARA expression PARC
    """
    p[0] = p[2]


# Error sintactico
def p_error(p):
    print(f'Error de sintaxis {p.value!r}')


# Build the parser
parser = yacc()

# Parse an expression
ast = parser.parse('2 * 3 + 4 * (5 - 4)')
print(ast)
