#Scanner
#Derek, Thomas, Kellen

class Parser:

    Tokens = []
    code = None

    tree = None

    def __init__(self, tokens, code):
        self.tokens = tokens
        self.code = code
        syntaxErrors = []
        
    def parse(self, line_number):
        line = [token for token in self.tokens if token.get('line_number') == line_number]
        statement = [token for token in line if token.get('name') == ':' or token.get('name') == ':=' or token.get('name') == 'if' or token.get('name') == 'else' or token.get('name') == 'then' or token.get('name') == '(' or token.get('name') == ')']


        #[:, :=]
        tree_type = None
        line_pos = None
        line_pos2 = None
        paren_counter = 0
        Tree = None
        left = None
        right = None
        parent = None

        for operator_token in statement:
            if operator_token.get('name') == ':=':
                tree_type = 'assignment'
                line_pos = operator_token.get('line_pos')
                break
            elif operator_token.get('name') == ':':
                if next(token for token in statement if token.get('name') == ':='):
                        tree_type = 'assignment_statement'
                        ptoken = next(token for token in statement if token.get('name') == ':=')
                        line_pos = ptoken.get('line_pos')
                else: 
                        tree_type = 'type_statement'
                        line_pos = operator_token.get('line_pos')
                break    
            elif operator_token.get('name') == '(': # or operator_token.get('name') == ')':
                #if operator_token.get('name') == '(':
                        paren_counter += 1
                        tree_type = 'function_statement'
                        line_pos = operator_token.get('line_pos')
                        break
                # elif operator_token.get('name') == ')':
                #      paren_counter -=1
                #      line_pos2 = operator_token.get('line_pos')
                #      if paren_counter == 0:
                #           break
            elif operator_token.get('name') == 'if':
                if operator_token.get('name') == 'if':
                        tree_type = 'conditional_statement'
                        line_pos = operator_token.get('line_pos')
                elif operator_token.get('name') == 'then':
                        line_pos2 = operator_token.get('line_pos')
                        break
        
        if tree_type == 'assignment_statement':
            parent = next(token for token in line if token.get('line_pos') == line_pos)
            left = [token for token in line if token.get('line_pos') < line_pos]
            right = [token for token in line if token.get('line_pos') > line_pos]
            
        elif tree_type == 'type_statement':
            parent = next(token for token in line if token.get('line_pos') == line_pos)
            left = [token for token in line if token.get('line_pos') < line_pos]
            right = [token for token in line if token.get('line_pos') > line_pos]
        elif tree_type == 'function_statement':
            parent = 'function'
            left = [token for token in line if token.get('line_pos') < line_pos]
            right = [token for token in line if token.get('line_pos') > line_pos] #and token.get('line_pos') < line_pos2]
        elif tree_type == 'if':
            parent = 'conditional_statement'
            left = 'if'
            right = [token for token in line if token.get('line_pos') > line_pos and token.get('line_pos') < line_pos2]
        self.tree = (parent, left, right, tree_type)

    def parserOutput(self, line_number):
        code_at_line = self.code[line_number-1].rstrip()
        print('Code | Line: ' + str(line_number) + ' \n', code_at_line)
        print('Parser Output:')
        print('<block> -> <statement>')
        print('<statement> <' + self.tree[3] + '>') 
        if self.tree[3] == 'assignment_statement':
            print('<assignment_statement> -> identifier <assignment_opeator> <value>' )
            print(self.tree[1], '-> <identifier>')
            print(self.tree[0], '-> <assignment_opeator>')
            print(self.tree[2], '-> <value>')
        elif self.tree[3] == 'type_statement':
            print('<type_statement> -> identifier <type_operator> <type>' )
            print(self.tree[1], '-> <identifier>')
            print(self.tree[0], '-> <type_opeator>')
            print(tree[2], '-> <value>')
        elif self.tree[3] == 'function_statement':
            print('<function_statement> -> identifier <function_operator> <function_parameters>' )
            print(self.tree[1], '-> <identifier>')
            print(self.tree[0], '-> <function_operator>')
            print(self.tree[2], '-> <function_parameters>')
        elif self.tree[3] == 'conditional_statement':
            print('<conditional_statement> -> <conditional_keyword> <condition>' )
            print(self.tree[1], '-> <conditional_keyword>')
            print(self.tree[2], '-> <condition>')
class Node:
    node_counter = 0

    def __init__(self, parent_id, left_id, right_id):
        Node.node_counter += 1
        self.parent_id = parent_id
        self.left_id = left_id
        self.right_id = right_id
        self.id = node_counter
    
    #overrides equals based on id
    def __eq__(self, node):
        return self.id == node.id

class Tree:

    #token/id counter
    tree_counter = 0

    #initialization 
    def __init__(self, parent, left, right):
        Tree.tree_counter += 1
        self.parent = parent
        self.left = left
        self.right = right
        self.id = tree_counter

