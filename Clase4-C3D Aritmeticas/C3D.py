tokens = (
    'PARA',
    'PARC',
    'MAS',
    'MENOS',
    'MULTI',
    'DIV',
    'ENTERO',
)

t_PARA = r'\('
t_PARC = r'\)'
t_MAS = r'\+'
t_MENOS = r'\-'
t_MULTI = r'\*'

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Error en el entero")

    return t

t_ignore = " \t"

def t_error(t):
    print("No se reconoce el caracter " + t.value[0])


import ply.lex as lex
lexer = lex.lex()


def p_inicio(t):
    'inicio : E'
    print(str(t[1]))

def p_e(t):
    '''
    E   : T MAS E
        | T MENOS E
    '''
    if t[2] == '+': 
        print(str(t[1]) + " + " + str(t[3]))
        t[0] = t[1]+t[3]
    elif t[2] == '-': 
        print(str(t[1]) + " - " + str(t[3]))
        t[0] = t[1]+t[3]

def p_e_sin(t):
    'E : T'
    t[0] = t[1]

def p_T(t):
    '''
    T   : A MULTI T
        | A DIV T
    '''
    if t[2] == '*': 
        print(str(t[1]) + " * " + str(t[3]))
        t[0] = t[1]*t[3]
    elif t[2] == '/': 
        print(str(t[1]) + " / " + str(t[3]))
        t[0] = t[1]/t[3]


def p_sin(t):
    ' T : A'
    t[0] = t[1]

def p_A(t):
    'A   : PARA E PARC'
    t[0] = t[2]

def p_A_num(t):
    'A   : ENTERO '
    t[0] = t[1]

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

input = "1 + 1 + 2"
parser.parse(input) 