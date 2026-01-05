import ply.yacc as yacc
from sympy import symbols, And, Or, Not, Xor, Nand, Nor, Implies, Equivalent
from sympy.logic.boolalg import BooleanFunction
from prop_lexer import PropLexer

# 定義 CONCAT 類別以區分 CONCAT 和普通的 AND
class Concat(BooleanFunction):
    """CONCAT 運算符，用於連接多個等式"""
    @classmethod
    def eval(cls, *args):
        # 如果只有一個參數，直接返回
        if len(args) == 1:
            return args[0]
        # 否則返回 Concat 對象
        return None

class PropParser(object):
    tokens = PropLexer.tokens
    """
        id: symbol | ( prop )
        term : id
        prop: term
            | ( * prop prop )
            | ( + prop prop )
            | ( & prop prop )
            | ( ! prop )
    """

    # Parsing rules
    precedence = (
        ("left", "OR"),
        ("left", "XOR"),
        ("left", "AND"),
        ("left", "CONCAT"),
        ("right", "NOT"),
    )

    def __init__(self):
        self.lexer = PropLexer()
        self.lexer.build()
        self.atoms = {}
        self.concat_spliter = {}
        self.concat_spliter_id = 0

    # for parsing the proposition
    def p_prop_term(self, p):
        "prop : term"
        p[0] = p[1]

    def p_prop_and(self, p):
        "prop : LPAREN AND prop prop RPAREN"
        p[0] = And(p[3], p[4])

    def p_prop_or(self, p):
        "prop : LPAREN OR prop prop RPAREN"
        p[0] = Or(p[3], p[4])
    
    def p_prop_xor(self, p):
        "prop : LPAREN XOR prop prop RPAREN"
        p[0] = Xor(p[3], p[4])
        
    def p_prop_concat(self, p):
        "prop : LPAREN CONCAT prop prop RPAREN"
        # CONCAT (&) 用於連接多個等式，使用 Concat 類別以區分於普通的 AND
        p[0] = Concat(p[3], p[4])
        
        # Track components for splitting concat expressions
        # Since parsing is bottom-up, components from nested Concat are already added
        # We only need to add new components (non-Concat leaves)
        if isinstance(p[3], Concat):
            # Left side is already a Concat, its components are already tracked
            # Just add the right component (p[4])
            self.concat_spliter[self.concat_spliter_id] = p[4]
            self.concat_spliter_id += 1
        else:
            # Left side is not a Concat, add both components
            # This is the first (innermost) concat
            self.concat_spliter[self.concat_spliter_id] = p[3]
            self.concat_spliter[self.concat_spliter_id + 1] = p[4]
            self.concat_spliter_id += 2

    def p_prop_not(self, p):
        "prop : LPAREN NOT prop RPAREN"
        p[0] = Not(p[3])

    def p_term_id(self, p):
        "term : id"
        p[0] = p[1]

    def p_id_symbol(self, p):
        "id : SYMBOL"
        if p[1] not in self.atoms:
            self.atoms[p[1]] = symbols(p[1])
        p[0] = self.atoms[p[1]]

    def p_error(self, p):
        print("Syntax error at '%s'" % p)

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse(self, data):
        self.lexer.input(data)
        return self.parser.parse(data, lexer=self.lexer.lexer), self.concat_spliter


# test string
# parser = PropParser()
# parser.build()
# result = parser.parse("(& (* pi2 pi3) pi4)")
# print(result)
