from ada_scanner import Scanner

def parse(scanner, y):
     tokens = scanner.getTokens()

     line = [token for token in tokens if token.get('line_number') == y]
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
     tree = (parent, left, right)

     code_at_line = scanner.getLines()[y].rstrip()
     # start = tree[1][-1].get('line_pos')
     # l = code_at_line[:start]
     # print("Start", start)
     # print(code_at_line[:start])
     print('Code | Line: ' + str(y) + ' \n', code_at_line)
     print('Parser Output:')
     print('<block> -> <statement>')
     print('<statement> <' + tree_type + '>') 
     if tree_type == 'assignment_statement':
          print('<assignment_statement> -> identifier <assignment_opeator> <value>' )
          print(tree[1], '-> <identifier>')
          print(tree[0], '-> <assignment_opeator>')
          print(tree[2], '-> <value>')
     elif tree_type == 'type_statement':
          print('<type_statement> -> identifier <type_operator> <type>' )
          print(tree[1], '-> <identifier>')
          print(tree[0], '-> <type_opeator>')
          print(tree[2], '-> <value>')
     elif tree_type == 'function_statement':
          print('<function_statement> -> identifier <function_operator> <function_parameters>' )
          print(tree[1], '-> <identifier>')
          print(tree[0], '-> <function_operator>')
          print(tree[2], '-> <function_parameters>')
     elif tree_type == 'conditional_statement':
          print('<conditional_statement> -> <conditional_keyword> <condition>' )
          print(tree[1], '-> <conditional_keyword>')
          print(tree[2], '-> <condition>')
     



def main():
     file1 = Scanner('test files/testfile.adb')

     parse(file1, 15)
main()


# Code:
# x = 7

# Parser Output:
# <block> -> <statement>
# <statement> -> <assignment_statement>
# <assignment_statement> -> id <assignment_operator>
# <arithmetic_expression>
# <assignment_operator> -> <eq_operator>
# <arithmetic_expression> -> <literal_integer> x -> id
# = -> <assignment_operator>
# 7 -> <literal_integer>
# = x 7	//pre-fix
 

# x 7 =	//post-fix
