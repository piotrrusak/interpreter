from __future__ import print_function
import AST


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator


class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.StatementsNode)
    def printTree(self, indent=0):
        for stmt in self.statements:
            stmt.printTree(indent)

    @addToClass(AST.Expr)
    def printTree(self, indent=0):
        self.expr.printTree(indent)

    @addToClass(AST.AssignExpr)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}{self.op}")
        self.ref.printTree(indent + 1)
        self.value.printTree(indent + 1)

    @addToClass(AST.RelExpr)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}{self.op}")
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.ZerosFunc)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}ZEROS")
        self.size.printTree(indent + 1)

    @addToClass(AST.OnesFunc)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}ONES")
        self.size.printTree(indent + 1)

    @addToClass(AST.EyeFunc)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}EYE")
        self.size.printTree(indent + 1)

    @addToClass(AST.StringOfValues)
    def printTree(self, indent=0):
        for value in self.values:
            value.printTree(indent)

    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}VECTOR")
        self.string_of_values.printTree(indent+1)

    @addToClass(AST.VectorCellRef)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}VECTOR CELL REF")
        self.ID.printTree(indent + 1)
        self.idx.printTree(indent + 1)

    @addToClass(AST.MatrixCellRef)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}{self.name}")
        self.idx_array.printTree(indent + 1)

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}{self.value}")

    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}{self.value}")

    @addToClass(AST.String)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}{self.value}")

    @addToClass(AST.Value)
    def printTree(self, indent=0):
        self.value.printTree(indent)

    @addToClass(AST.NegationRef)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}NEGATIVE")
        self.value.printTree(indent+1)

    @addToClass(AST.IDRef)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}{self.name}")

    @addToClass(AST.TransposeRef)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}TRANSPOSE")
        self.value.printTree(indent + 1)

    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}{self.op}")
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.ForLoop)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}FOR")
        self.ref.printTree(indent + 1)
        self.start.printTree(indent + 2)
        self.end.printTree(indent + 2)
        self.instructions.printTree(indent + 1)

    @addToClass(AST.Print)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}PRINT")
        self.value.printTree(indent + 1)

    @addToClass(AST.WhileLoop)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}WHILE")
        self.condition.printTree(indent + 1)
        self.instructions.printTree(indent + 1)

    @addToClass(AST.IfElseExpr)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}IF")
        self.condition.printTree(indent)
        print(f"{'|  ' * indent}THEN")
        self.if_instructions.printTree(indent + 1)

        if (self.else_instructions == None):
            return

        print(f"{'|  ' * indent}ELSE")
        self.else_instructions.printTree(indent + 1)

    @addToClass(AST.BreakStatement)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}BREAK")

    @addToClass(AST.ContinueStatement)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}CONTINUE")

    @addToClass(AST.ReturnStatement)
    def printTree(self, indent=0):
        print(f"{'|  ' * indent}RETURN")
        self.value.printTree(indent+1)

    @addToClass(AST.BlankStatement)
    def printTree(self, indent=0):
        pass