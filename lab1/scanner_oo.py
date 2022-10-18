import ply.lex as lex

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'break': "BREAK",
    'continue': "CONTINUE",
    'return': "RETURN",
    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',
    'print': 'PRINT'
}

tokens = [
    'DOTADD',
    'DOTSUB',
    'DOTMUL',
    'DOTDIV',
    'ADDASSIGN',
    'SUBASSIGN',
    'MULASSIGN',
    'DIVASSIGN',
    'GT',
    'LT',
    'GE',
    'LE',
    'NE',
    'EQ',
    'ID',
    'INTNUM',
    'FLOATNUM',
    'STRING',
    'COMMENT'
] + list(reserved.values())

literals = r'+-/*;:\'",()[]{}='

t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\./'
t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_NE = r'!='
t_EQ = r'=='


def t_FLOATNUM(t):
    r'[+-]?(\d+\.\d*)|(\d*\.\d+)'
    t.value = float(t.value)
    return t


def t_INTNUM(t):
    r'[+-]?\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[A-Za-z_][A-Za-z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_STRING(t):
    r'"(([^"\\])|(\\.))*"'
    return t


def t_COMMENT(t):
    r'\#[^\n]*'


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s' at line %d" % (t.value[0], t.lexer.lineno))
    t.lexer.skip(1)


class Scanner:
    def build(this):
        this.lexer = lex.lex()

    def input(this, text):
        this.lexer.input(text)

    def token(this):
        tok = this.lexer.token()
        return None if not tok else "({}): {}({})".format(tok.lineno, tok.type, tok.value)
