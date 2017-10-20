import ast
import astunparse

my_program_code = "my-program.py"
code = open(my_program_code).read()

tree = ast.parse(code)
# for statement in tree.body:
#     print (ast.dump(statement), '\n')


# class FunctionCallVisitor(ast.NodeVisitor):
#     def visit_Assign(self, node):
#         print("Assign :")
#         ast.NodeVisitor.generic_visit(self, node)
#
#     def visit_Expr(self, node):
#         print("Expr :")
#         ast.NodeVisitor.generic_visit(self, node)

# FunctionCallVisitor().visit(tree)

class MyTransformer(ast.NodeTransformer):
    def visit_Assign(self, node):
        print("Transform Assign :")
        return node

    def visit_Call(self, node):
        print("Call:")
        return node


MyTransformer().visit(tree)
print(astunparse.unparse(tree))
