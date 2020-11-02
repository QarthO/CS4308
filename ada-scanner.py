# ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
# ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
# ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
# ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
# ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
# ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

#token object             
class Token:

    #token/id counter
    token_counter = 0

    #initialization 
    def __init__(self, name, line_number, token_pos):
        Token.token_counter += 1
        self.token = dict()
        self.token['name'] = name
        self.token['type'] = type
        self.token['line_number'] = line_number
        self.token['token_pos'] = token_pos
        self.id = Token.token_counter
        self.updateType()

    #Example of String: token = (name, type, line_number, token_position)

    #overrides string
    def __str__(self):
        return str((self.get('name'), self.get('type'), self.get('line_number'), self.get('token_pos')))

    #overrides representation
    def __repr__(self):
        return str((self.get('name'), self.get('type'), self.get('line_number'), self.get('token_pos')))
    
    #overrides equals based on id
    def __eq__(self, token):
        return self.id == token.id

    #gets the value from the inputed key
    def get(self, key):
        return self.token.get(key)

    #sets the inputed value at the key
    def set(self, key, value):
        self.token[key] = value

    #Classifies the token
    def updateType(self):

        name = self.token['name']

        #Keyword
        if isKeyword(name):
            self.token['type'] = 'keyword'
            return

        #Delimiter
        if isDelimiter(name):
            self.token['type'] = 'delimiter'
            return

        #Integer
        if isInteger(name):
            self.token['type'] = 'integer'
            return
        
        #Float
        if isFloat(name):
            self.token['type'] = 'float'
            return

        #Boolean
        if isBoolean(name):
            self.token['type'] = 'boolean'
            return

        #Identifier
        if isIdentifier(name):
            self.token['type'] = 'identifier'
            return
    
        #Comment
        if isComment(name):
            self.token['type'] = 'comment'
            return

        #String
        if isString(name):
            self.token['type'] = 'string'
            return

        self.token['type'] = None

#if the token isnt one of the above things, defaults to unclassified
#Checks if the input token is a Keyword of the ADA language
#Returns true if the token is a keyword, false if not
def isKeyword(name):
    keywords = ['abort', 'abs', 'abstract', 'accept', 'access', 'aliased', 'all', 'and', 'array', 'at', 'begin', 'body', 'case', 'constant', 'declare', 'delay', 'delta', 'digits', 'do', 'else', 'elseif', 'end', 'entry', 'exception', 'exit', 'for', 'function', 'generic', 'goto', 'if', 'in', 'interface', 'is', 'limited', 'loop', 'mod', 'new', 'not', 'null', 'of', 'or', 'others', 'out', 'overriding', 'package', 'pragma', 'private', 'procedure', 'protected', 'raise', 'range', 'record', 'rem', 'renames', 'requeue', 'return', 'reverse', 'select', 'seperate', 'some', 'subtype', 'synchronized', 'tagged', 'task', 'terminate', 'then', 'type', 'until', 'use', 'when', 'while', 'with', 'xor']
    for keyword in keywords:
        if keyword == name:
            return True
    return False

#Chekcs if the input token is a delimiter of the ADA language
#Returns true if the token is a delimiter, false if not
def isDelimiter(name):
    single_delimiters = ['&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '|']
    compound_delimiters = ['=>', '..', '**', ':=', '/=', '>=', '<=', '<<', '>>', '<>']
    other_delimiters = ['\"', '#', '[', ']', '{', '}']
    
    for single_delimiter in single_delimiters:
        if single_delimiter == name:
            return True
    
    for compound_delimiter in compound_delimiters:
        if compound_delimiter == name:
            return True

    for other_delimiter in other_delimiters:
        if other_delimiter == name:
            return True

    return False

#Checks if token is an integer
#Returns true if the token is an integer, false if not
def isInteger(name):
    return name.isdigit()

#Checks if token is a float
#Returns true if the token is a float, false if not
def isFloat(name):
    try:
        float(name)
        return True
    except ValueError:
        return False

#Checks if token is a boolean value
#Returns true if the token is a boolean value, false if not
def isBoolean(name):
    return (name.lower() == 'true' or name.lower() == 'false')

#Checks if token is an identifier
#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). 
#A valid identifier cannot start with a number, or contain any spaces.
#Returns true if the token is an identifier, false if not
def isIdentifier(name):
    return name.isidentifier()

#Checks if token starts with the comment syntax (--)
#Returns true if the token starts with the comment syntax, false if not
def isComment(name):
    return name.startswith('--')

#Checks if token starts or ends with the string syntax ("")
#Returns true if the token starts or ends with the string syntax, false if not
def isString(name):
    return name.startswith("\"") or name.endswith('\"')    
    
def read(file):
    print("Reading File: " + file)
    print('===================================================================')
    file = open(file, 'r')
    lines = file.readlines()
    print(''.join(map(str,lines)))
    print('===================================================================')
    return lines

def generateTokens(lines):
    tokens = []
    line_number = 0
    for line in lines:
        line_number += 1
        token_pos = 1
        values = line.split()
        for value in values:
            token = Token(value, line_number, token_pos)
            token_pos += 1
            tokens.append(token)
    print("Tokens Array:\n" + '\n'.join(map(str,tokens)))
    return tokens

def main():
    lines = read('programs.adb')
    tokens = generateTokens(lines)

main()