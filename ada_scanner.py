# ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
# ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
# ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
# ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
# ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
# ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

import copy
from ada_parser import Parser

#token object             
class Token:

    #token/id counter
    token_counter = 0

    #initialization 
    def __init__(self, name, line_number, line_pos):
        Token.token_counter += 1
        self.token = dict()
        self.token['name'] = name
        self.token['type'] = type
        self.token['line_number'] = line_number
        self.token['line_pos'] = line_pos
        self.id = Token.token_counter
        self.updateType()

    #Example of String: token = (name, type, line_number, line_pos)

    #overrides string
    def __str__(self):
        return str((self.get('name'), self.get('type'), self.get('line_number'), self.get('line_pos')))

    #overrides representation
    def __repr__(self):
        return str((self.get('name'), self.get('type'), self.get('line_number'), self.get('line_pos')))
    
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



single_delimiters = ['&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '|', '\"', '#', '[', ']', '{', '}']
compound_delimiters = ['=>', '..', '**', ':=', '/=', '>=', '<=', '<<', '>>', '<>', '--']
keywords = ['abort', 'abs', 'abstract', 'accept', 'access', 'aliased', 'all', 'and', 'array', 'at', 'begin', 'body', 'case', 'constant', 'declare', 'delay', 'delta', 'digits', 'do', 'else', 'elseif', 'end', 'entry', 'exception', 'exit', 'for', 'function', 'generic', 'goto', 'if', 'in', 'interface', 'is', 'limited', 'loop', 'mod', 'new', 'not', 'null', 'of', 'or', 'others', 'out', 'overriding', 'package', 'pragma', 'private', 'procedure', 'protected', 'raise', 'range', 'record', 'rem', 'renames', 'requeue', 'return', 'reverse', 'select', 'seperate', 'some', 'subtype', 'synchronized', 'tagged', 'task', 'terminate', 'then', 'type', 'until', 'use', 'when', 'while', 'with', 'xor']


def isIndent(name):
    for c in name:
        if c != ' ':
            return False
    return True

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
    
    for single_delimiter in single_delimiters:
        if single_delimiter == name:
            return True
    
    for compound_delimiter in compound_delimiters:
        if compound_delimiter == name:
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

#Scanner class
class Scanner:

    #Creating the tokens array
    tokens = []
    
    #Initialization function
    def __init__(self, filename):
        self.debug = False
        self.file_lines = self.read(filename)
        self.generateTokens(self.file_lines)
        self.parser = Parser(self.tokens, self.file_lines)
        
    #Reads the file
    def read(self, filename):
        if self.debug:
            print("Reading File: " + filename)
            print('===================================================================')
        file = open(filename, 'r')
        lines = file.readlines()
        if self.debug:
            print(''.join(map(str,lines)))
            print('===================================================================')
        return lines

    #Generates the tokens from the lines of code from the file
    def generateTokens(self, lines):
        line_number = 0
        for line in lines:
            line_number += 1
            token_pos = 1
            values = self.seperate(line)
            for value in values:
                token = Token(value[0], line_number, value[1])
                token_pos += 1
                self.tokens.append(token)
        if self.debug:
            print("Tokens Array Format: (name, type, line number, line position)")
            print('\n'.join(map(str,self.tokens)))
    
    def getLines(self):
        return copy.deepcopy(self.file_lines)

    #Returns a deepcopy of the tokens generated from scanning the file
    def getTokens(self):
        return copy.deepcopy(self.tokens)

    def parseLines(self, line_numbers):
        for line_number in line_numbers:
            self.parser.parse(line_number)
            self.getParserOutput(line_number)

    def getParserOutput(self, line_number):
        self.parser.parserOutput(line_number)
    
    #Enables/Disable printing stuff to console for easier debugging
    def setDebug(self, value):
        self.debug = value
    
    #Splits into seperate raw tokens (unclassified)
    def seperate(self, line):
        raw_tokens = []
        chars = []
        line_pos = 0
        token_name = ''
        start_pos = 1
    
        #Assigns line position to each character
        for c in line:
            line_pos += 1
            chars.append((c, line_pos))

        #Loops through the charactesr
        for c in chars :

            #Skips spaces
            if token_name.isspace():
                token_name = token_name.lstrip()
                start_pos +=1
                token_name += c[0]
            
            elif token_name.startswith('--'):
                token_name += c[0]

            elif token_name.startswith('\"'):
                if c[0] == '\"':
                    raw_tokens.append((token_name+c[0], start_pos))
                    start_pos = c[1]+1
                    token_name = ''
                else:
                    token_name += c[0]

            #If next character is a space or delimiter, then puts concatentated token name into the raw tokens
            elif token_name and (isDelimiter(c[0]) or c[0].isspace()):
                if isDelimiter(token_name):
                    if not isDelimiter(c[0]):
                        raw_tokens.append((token_name, start_pos))
                        start_pos = c[1]
                        token_name = c[0]
                    elif isDelimiter(token_name+c[0]):
                        if not token_name+c[0] == '--':
                            raw_tokens.append((token_name+c[0], start_pos))
                            start_pos = c[1]+1
                            token_name = ''
                        else: 
                            token_name = '--'
                elif not token_name.isspace():
                    raw_tokens.append((token_name, start_pos))
                    start_pos = c[1]
                    token_name = c[0]
            
            elif isDelimiter(token_name):
                if not isDelimiter(c[0]):
                    raw_tokens.append((token_name, start_pos))
                    start_pos = c[1]
                    token_name = c[0]

            else:
                token_name += c[0]
        
        if token_name.startswith('--'):
            raw_tokens.append((token_name.rstrip(), start_pos))

        return raw_tokens