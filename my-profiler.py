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
    # def visit_Call(self, node):
    #     print(ast.dump(node))

    # def visit_BinOp(self, stmt_binop):
    #     print('expression: ')
    #
    #     for child in ast.iter_fields(stmt_binop):
    #         print('  child %s ',  str(child))

        #self.continue(stmt_binop)
    # def visit_Name(self, node):
    #     print('Name :', node.id)
    #
    # def visit_Num(self, node):
    #     print('Num :', node.__dict__['n'])
    #
    # def visit_Str(self, node):
    #     print("Str :", node.s)
    #
    # def visit_Print(self, node):
    #     print("Print :")
    #     ast.NodeVisitor.generic_visit(self, node)

    def visit_Assign(self, node):
        print("Transform Assign :")

        #import_node = ast.Import(names=[ast.alias(name='quux', asname=None)])

        #assign_node = ast.Assign(targets=[ast.Name(id='eggs', ctx=ast.Store())], value=ast.Str(s='ham'))
        #value = Call(func=Name(id='open', ctx=Load())

        # call_node = ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Str(s='Line number is: '), ast.Num(n=1)], keywords=[])
        #
        # node.append(call_node)
        #ast.fix_missing_locations(node)

        return node

    def visit_Call(self, node):
        print(ast.dump(node))
        return node


MyTransformer().visit(tree)


print(astunparse.unparse(tree))
