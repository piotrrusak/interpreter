class Node:
    def __init__(self, lineno):
        self.lineno = lineno

class StatementsNode(Node):
    def __init__(self, statements, lineno):
        super().__init__(lineno)
        self.statements = statements

class Expr(Node):
    def __init__(self, expr, lineno):
        super().__init__(lineno)
        self.expr = expr

class IntNum(Node):
    def __init__(self, value, lineno):
        super().__init__(lineno)
        self.value = value

class FloatNum(Node):
    def __init__(self, value, lineno):
        super().__init__(lineno)
        self.value = value

class Variable(Node):
    def __init__(self, name, lineno):
        super().__init__(lineno)
        self.name = name

class Value(Node):
    def __init__(self, value, lineno):
        super().__init__(lineno)
        self.value = value

class String(Node):
    def __init__(self, value, lineno):
        super().__init__(lineno)
        self.value = value

class BinExpr(Node):
    def __init__(self, left, op, right, lineno):
        super().__init__(lineno)
        self.left = left
        self.op = op
        self.right = right

class UnaryExpr(Node):
    def __init__(self, operator, operand, lineno):
        super().__init__(lineno)
        self.operator = operator
        self.operand = operand

class RelExpr(Node):
    def __init__(self, left, op_operator, right, lineno):
        super().__init__(lineno)
        self.left = left
        self.op = op_operator
        self.right = right

class AssignExpr(Node):
    def __init__(self, ref, op, value, lineno):
        super().__init__(lineno)
        self.ref = ref
        self.op = op
        self.value = value

class IfElseExpr(Node):
    def __init__(self, condition, if_instructions, else_instructions, lineno):
        super().__init__(lineno)
        self.condition = condition
        self.if_instructions = if_instructions
        self.else_instructions = else_instructions

class ForLoop(Node):
    def __init__(self, start, end, instructions, lineno):
        super().__init__(lineno)
        self.start = start
        self.end = end
        self.instructions = instructions

class WhileLoop(Node):
    def __init__(self, condition, instructions, lineno):
        super().__init__(lineno)
        self.condition = condition
        self.instructions = instructions

class Matrix(Node):
    def __init__(self, matrix, lineno):
        super().__init__(lineno)
        self.matrix = matrix

class EyeFunc(Node):
    def __init__(self, name, size, lineno):
        super().__init__(lineno)
        self.name = name
        self.size = size

class ZerosFunc(Node):
    def __init__(self, name, size, lineno):
        super().__init__(lineno)
        self.name = name
        self.size = size

class OnesFunc(Node):
    def __init__(self, name, size, lineno):
        super().__init__(lineno)
        self.name = name
        self.size = size

class IDRef(Node):
    def __init__(self, name, lineno):
        super().__init__(lineno)
        self.name = name

class MatrixCellRef(Node):
    def __init__(self, ID, idx, lineno):
        super().__init__(lineno)
        self.ID = ID
        self.idx = idx

class Print(Node):
    def __init__(self, value, lineno):
        super().__init__(lineno)
        self.value = value

class BreakStatement(Node):
    def __init__(self, lineno):
        super().__init__(lineno)

class ContinueStatement(Node):
    def __init__(self, lineno):
        super().__init__(lineno)

class ReturnStatement(Node):
    def __init__(self, value, lineno):
        super().__init__(lineno)
        self.value = value

class BlankStatement(Node):
    def __init__(self, lineno):
        super().__init__(lineno)

class NegationRef(Node):
    def __init__(self, value, lineno):
        super().__init__(lineno)
        self.value = value

class TransposeRef(Node):
    def __init__(self, value_vector, lineno):
        super().__init__(lineno)
        print(type(value_vector))
        self.value = value_vector

class StringOfValues(Node):
    def __init__(self, values, lineno):
        super().__init__(lineno)
        self.values = values

class Vector(Node):
    def __init__(self, string_of_values, lineno):
        super().__init__(lineno)
        self.string_of_values = string_of_values