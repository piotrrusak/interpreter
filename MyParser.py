from MyScanner import MyScanner
import AST
from sly import Parser

class MyParser(Parser):
    tokens = MyScanner.tokens
    debugfile = 'parser.out'

    precedence = (
        ('nonassoc', IFX),
        ('nonassoc', ELSE),
        ('nonassoc', LTE, GTE, EQ, NEQ, LT, GT),
        ('left', ADD, SUB, DOTADD, DOTSUB),
        ('left', MUL, DIV, DOTMUL, DOTDIV),
        # ('nonassoc', "'")
    )

    @_('stmt',
       'statements stmt')
    def statements(self, p):
        if len(p) == 1:
            return AST.StatementsNode([p[0]], lineno=p.lineno)

        statements = p[0].statements.copy()
        statements.append(p[1])

        return AST.StatementsNode(statements, lineno=p.lineno)

    @_('";"',
       '"{" statements "}"',
       'if_stmt',
       'while_stmt',
       'for_stmt',
       'assign_expr',
       'print_stmt',
       'BREAK ";"',
       'CONTINUE ";"',
       'RETURN expr ";"')
    def stmt(self, p):
        try:
            if (p.BREAK):
                return AST.BreakStatement(lineno=p.lineno)
        except:
            pass
        try:
            if (p.CONTINUE):
                return AST.ContinueStatement(lineno=p.lineno)
        except:
            pass
        try:
            if (p.RETURN):
                return AST.ReturnStatement(p[1], lineno=p.lineno)
        except:
            pass

        if p[0] == ";":
            return AST.BlankStatement(lineno=p.lineno)

        if len(p) == 1:
            return p[0]

        return p[1]

    @_('IF "(" rel_expr ")" stmt ELSE stmt',
       'IF "(" rel_expr ")" stmt %prec IFX')
    def if_stmt(self, p):
        condition = p[2]
        if_body = p[4]
        else_body = None

        try:
            if (p.ELSE):
                else_body = p[6]
        except:
            pass

        return AST.IfElseNode(condition, if_body, else_body, lineno=p.lineno)

    @_('referance',
       'INTNUM')
    def int_referance(self, p):
        try:
            if (p.INTNUM):
                return AST.IntNum(p[0], lineno=p.lineno)
        except:
            pass
        try:
            if (p.ID):
                return AST.IDRef(p[0], lineno=p.lineno)
        except:
            pass

    @_('FOR referance "=" int_referance ":" int_referance stmt')
    def for_stmt(self, p):
        return AST.ForLoop(p[3], p[5], p[6], p.lineno)

    @_('WHILE "(" rel_expr ")" stmt')
    def while_stmt(self, p):
        return AST.WhileLoop(p[3], p[5], p.lineno)

    @_('PRINT expr')
    def print_stmt(self, p):
        return AST.Print(p[1], lineno=p.lineno)

    @_('INTNUM')
    def value(self, p):
        return AST.IntNum(p[0], p.lineno)

    @_('FLOATNUM')
    def value(self, p):
        return AST.FloatNum(p[0], p.lineno)

    @_('STRING')
    def value(self, p):
        return AST.String(p[0], p.lineno)

    @_('value',
       'value_vector "," value')
    def value_vector(self, p):
        if len(p) == 1:
            values = [p[0]]
        else:
            values = p[0].values
            values.append(p[2])
        return AST.ValueVector(values, p.lineno)

    @_('ID',
       'ID "[" value_vector "]"')
    def referance(self, p):
        if len(p) == 1:
            return AST.IDRef(p[0], p.lineno)
        else:
            return AST.MatrixCellRef(p[0], p[2]. p.lineno)

    @_('value_vector',
       'rel_expr',)
    def expr(self, p):
        return AST.Expr(p[0], p.lineno)

    @_('expr ADD expr',
       'expr SUB expr',
       'expr MUL expr',
       'expr DIV expr',
       'expr DOTADD expr',
       'expr DOTSUB expr',
       'expr DOTMUL expr',
       'expr DOTDIV expr',)
    def expr(self, p):
        return AST.BinExpr(p[0], p[1], p[2], p.lineno)

    @_('expr LT expr',
       'expr GT expr',
       'expr LTE expr',
       'expr GTE expr',
       'expr EQ expr',
       'expr NEQ expr')
    def rel_expr(self, p):
        return AST.RelExpr(p[0], p[1], p[2], p.lineno)

    @_('referance "=" expr',
       'referance ADDASSIGN expr',
       'referance SUBASSIGN expr',
       'referance MULASSIGN expr',
       'referance DIVASSIGN expr')
    def assign_expr(self, p):
        return AST.AssignExpr(p[0], p[1], p[2], p.lineno)



if __name__ == '__main__':
    lexer = MyScanner()
    parser = MyParser()

    # print("##### [TEST 1] #####")
    # with open("z2/ex1.txt") as file:
    #     data = file.read()
    #     ast = parser.parse(lexer.tokenize(data))
        # ast.printTree()

    # print("##### [TEST 2] #####")
    # with open("z2/ex2.txt") as file:
    #     data = file.read()
    #     ast = parser.parse(lexer.tokenize(data))
        # ast.printTree()

    print("##### [TEST 3] #####")
    with open("z2/ex3.txt") as file:
        data = file.read()
        # ast = parser.parse(lexer.tokenize(data))

