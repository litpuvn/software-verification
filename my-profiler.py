import ast
import astunparse

my_program_code = "my-program.py"
code = open(my_program_code).read()

tree = ast.parse(code)


class ParentChildNodeTransformer(object):

    def visit(self, node):
        self._prepare_node(node)
        for field, value in ast.iter_fields(node):
            self._process_field(node, field, value)
        return node

    @staticmethod
    def _prepare_node(node):
        if not hasattr(node, 'parent'):
            node.parent = None
            node.parents = []
        if not hasattr(node, 'children'):
            node.children = []

    def _process_field(self, node, field, value):
        if isinstance(value, list):
            for index, item in enumerate(value):
                if isinstance(item, ast.AST):
                    self._process_child(item, node, field, index)
        elif isinstance(value, ast.AST):
            self._process_child(value, node, field)

    def _process_child(self, child, parent, field_name, index=None):
        self.visit(child)
        child.parent = parent
        child.parents.append(parent)
        child.parent_field = field_name
        child.parent_field_index = index
        child.parent.children.append(child)

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

    def append_print_line(self, node):

        new_code = astunparse.unparse(node)

        line_number = str(node.lineno)
        # new_code += "\nprint('running line', 2)\n"
        new_code += "\nprint('running line'," + line_number + ")\n"

        new_node = ast.parse(new_code)

        ast.copy_location(new_node, node)
        ast.fix_missing_locations(new_node)

        return new_node


    def visit_Assign(self, node):

        return self.append_print_line(node)

    def visit_Call(self, node):

        return self.append_print_line(node)


tree = ParentChildNodeTransformer().visit(tree)
# print(astunparse.unparse(tree))

print("***************** New Tree ****************")

MyTransformer().visit(tree)

ast.fix_missing_locations(tree)

print(astunparse.unparse(tree))

with open('my-intrumented-program.py', 'w') as file:
    file.write(astunparse.unparse(tree))

print("Done and Bye!")