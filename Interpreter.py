from MyScanner import MyScanner
from MyParser import MyParser
from SymbolTable import SymbolTable
import AST
import numpy as np
from visit import *

class Interpreter(object):

    def __init__(self):
        self.ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,

            ".+": lambda A, B: A + B,
            ".-": lambda A, B: A - B,
            ".*": lambda A, B: A * B,
            "./": lambda A, B: A / B,

            "+=": lambda a, b: a + b,
            "-=": lambda a, b: a - b,
            "*=": lambda a, b: a * b,
            "/=": lambda a, b: a / b,

            "<": lambda a, b: a < b,
            "<=": lambda a, b: a <= b,
            ">": lambda a, b: a > b,
            ">=": lambda a, b: a >= b,
            "==": lambda a, b: a == b,
            "!=": lambda a, b: a != b
        }

        self.symbol_table = SymbolTable()

        self.loop_level = 0

    @on('node')
    def visit(self, node):
        pass

    @when(AST.StatementsNode)
    def visit(self, node):
        for stmt in node.statements:
            flag = self.visit(stmt)
            if flag == 1 or flag == 2 or flag == 3:
                return flag
        return 0

    @when(AST.BlankStatement)
    def visit(self, node):
        return 0

    # ==================================================================================================================
    # STATEMENTS
    # ==================================================================================================================

    @when(AST.AssignExpr)
    def visit(self, node):

        ref = self.visit(node.ref, False)
        op = node.op
        value = self.visit(node.value)

        if op != '=':
            current_value = self.visit(node.ref)
            value = self.ops[op](current_value, value)

        self.symbol_table.put(ref, value)

        return 0

    @when(AST.ForLoop)
    def visit(self, node):

        ref = self.visit(node.ref, False)
        start = self.visit(node.start)
        end = self.visit(node.end)
        self.symbol_table.put(ref, start)
        instructions = node.instructions

        for i in range(start, end):
            flag = self.visit(instructions)
            print("for", flag)
            if flag == 1 or flag == 2:
                return flag

            instructions = node.instructions
            self.symbol_table.put(ref, i+1)

        return 0

    @when(AST.WhileLoop)
    def visit(self, node):

        condition = node.condition
        instructions = node.instructions

        while self.visit(condition):
            flag = self.visit(instructions)
            if flag == 1 or flag == 2:
                return flag
            condition = node.condition
            instructions = node.instructions

        return 0

    @when(AST.IfElseExpr)
    def visit(self, node):

        condition = node.condition
        if_instructions = node.if_instructions
        else_instructions = node.else_instructions

        if self.visit(condition):
            flag = self.visit(if_instructions)
            if flag == 1 or flag == 2 or flag == 3:
                return flag
        else:
            flag = self.visit(else_instructions)
            if flag == 1 or flag == 2 or flag == 3:
                return flag

        return 0

    @when(AST.Print)
    def visit(self, node):
        value = self.visit(node.value)
        print("Print: ", value)

    @when(AST.ReturnStatement)
    def visit(self, node):
        return 1

    @when(AST.BreakStatement)
    def visit(self, node):
        return 2

    @when(AST.ContinueStatement)
    def visit(self, node):
        return 3

    # ==================================================================================================================
    # EXPRESSIONS
    # ==================================================================================================================

    @when(AST.BinExpr)
    def visit(self, node):

        left = self.visit(node.left)
        op = node.op
        right = self.visit(node.right)

        return self.ops[op](left, right)

    @when(AST.RelExpr)
    def visit(self, node):

        left = self.visit(node.left)
        op = node.op
        right = self.visit(node.right)

        return self.ops[op](left, right)

    # ==================================================================================================================
    # REFERANCE
    # ==================================================================================================================

    @when(AST.IDRef)
    def visit(self, node, getValue = True):

        name = node.name

        if getValue:
            return self.symbol_table.get(name)
        else:
            return name


    # ==================================================================================================================
    # VALUES
    # ==================================================================================================================

    @when(AST.Expr)
    def visit(self, node):
        expr = self.visit(node.expr)
        return expr

    @when(AST.StringOfValues)
    def visit(self, node):
        if len(node.values) == 1:
            return self.visit(node.values[0])
        return [self.visit(val) for val in node.values]

    @when(AST.Value)
    def visit(self, node):
        value = self.visit(node.value)
        return value

    @when(AST.IntNum)
    def visit(self, node):
        return node.value

    @when(AST.FloatNum)
    def visit(self, node):
        return node.value

    @when(AST.String)
    def visit(self, node):
        return node.value

    @when(AST.EyeFunc)
    def visit(self, node):

        size = self.visit(node.size)

        return np.eye(size)

    @when(AST.OnesFunc)
    def visit(self, node):

        size = self.visit(node.size)

        return np.ones(size)

    @when(AST.ZerosFunc)
    def visit(self, node):

        size = self.visit(node.size)

        return np.zeros(size)

    @when(AST.NegationRef)
    def visit(self, node):

        value = self.visit(node.value)

        return (-1) * value

if __name__ == '__main__':

    EXAMPLES = [
        # "ex1",
        # "ex2",
        # "ex3",
        "ex4"
    ]

    for example in EXAMPLES:
        with open(f"./z2/{example}.txt", "r") as f:

            print(f"+++++++++++++++++++++++++++++++")
            print(f"RUNNING {example}")
            print(f"+++++++++++++++++++++++++++++++")
            data = f.read()

            lexer = MyScanner()
            parser = MyParser()
            interpreter = Interpreter()

            tokens = lexer.tokenize(data)

            for tok in tokens:
                print(f"({tok.lineno}): {tok.type}({tok.value})")

            ast = parser.parse(lexer.tokenize(data))
            ast.printTree()

            print(f"+++++++++++++++++++++++++++++++")

            interpreter.visit(ast)