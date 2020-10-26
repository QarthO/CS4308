# ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
# ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
# ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
# ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
# ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
# ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
              
class Token:

    token_counter = 0

    def __init__(self, name, type, line_number, token_pos):
        Token.token_counter += 1
        self.token = dict()
        self.token['name'] = name
        self.token['type'] = type
        self.token['line_number'] = line_number
        self.token['token_pos'] = token_pos
        self.id = Token.token_counter

    def __str__(self):
        return str((self.get('name'), self.get('type'), self.get('line_number'), self.get('token_pos')))

    def __repr__(self):
        return str((self.get('name'), self.get('type'), self.get('line_number'), self.get('token_pos')))
    
    def __eq__(self, token):
        return self.id == token.id

    def get(self, value):
        return self.token.get(value)

    def set(self, key, value):
        self.token[key] = value
    
def read(file):
    print("Reading File: " + file)
    print('===================================================================')
    file = open(file, 'r')
    lines = file.readlines()
    print(''.join(map(str,lines)))
    print('===================================================================')

    return lines

#all single character ada delimiters
delimiters = ['&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '|', '\"', '#', '[', ']', '{', '}', ' ']
compound_delimiters = ['=>', '..', '**', ':=', '/=', '>=', '<=', '<<', '>>', '<>']

def prepLine(line):
    for delimiter in delimiters:
        if delimiter in line:

            line = line.replace(delimiter, (' ' + delimiter + ' '))
    return line

def combineCompoundTokens(tokens):
    
    #seperate by line
        #if on seperate lines ignore
    #check compound delimiters
        #if 2 delimiters are back2back then combine into 1 token
    #check string literals
        #if string delimiter is found, combine all raw tokens until string delimiter is found again
    #check comment
        #if comment syntax is found combine the rest of the raw tokens on that line 
    return

def classifyRawToken(value):
    type = None

    #put better classify code here

    return type

def generateRawTokens(lines):
    tokens = []
    line_number = 0
    for line in lines:
        line_number += 1
        token_pos = 1
        line = prepLine(line)
        values = line.split()
        for value in values:
            token = Token(value, classifyRawToken(value), line_number, token_pos)
            token_pos += 1
            tokens.append(token)
    print("Tokens Array:\n" + '\n'.join(map(str,tokens)))
    return tokens

def newPrepLine(line):
    tokens = []
    line_number = 0
    for line in lines:
        line_number += 1
        token_pos = 1
        raw_tokens = line.split()
        current_token = None
        name = None
        token_type = None
        end = False
        for value in raw_tokens:
            name += value
            token = Token(name, token_type, line_number, token_pos)
            token_pos += 1
            tokens.append(token)
            name = None

def main():
    lines = read('testfile.adb')
    # tokens = generateRawTokens(lines)
    # combineCompoundTokens(tokens)

    # testtokens = splitLine(lines)
    
    line = 'x += 1;'

    x = line.split()

    print(x)


    # line = [token for token in tokens if token.get('line_number') == 1]


# line = [token for token in tokens if token.get('line_number') == line_number]

main()