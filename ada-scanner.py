## Class: CS 4308 Section 01
## Term: Fall 2020
## Names: Derek Comella, Kellen Hill, Thomas Williams
## Instructor: Deepa Muralidhar
## Project Deliverable 1: Scanner

#Reads test File
#Prints out the test file to console
#Puts each line of the file into an element of an array
#Returns the array
#Example:
#   line1: x = 5
#   line2: y = 10
#   -----
#   Array: ['x = 5', 'y = 10']
#   Array: [['x', '=', '5'], ['y', '=', '10']]
#
def read(file):
    file1 = open(file, 'r')
    lines = file1.readlines()
    count = 0
    print("Reading File: " + file)
    for line in lines: 
        count += 1
        print("  Line{}: {}".format(count, line.strip()))
    print("End of File")
    return lines

#Splits each line (element) into an array with every element being a token
#Prints out the new 2-D array
#Returns this new 2-D Array
#   Input  Array: ['x = 5', 'y = 10']
#   Output Array: [['x', '=', '5'], ['y', '=', '10']]
def generateTokens(lines):
    global tokens
    tokens = []
    for line in lines:
        tokens.append(line.split())
    print("Tokens Array:", tokens)
    return tokens

#Checks if the input token is a Keyword of the ADA language
#Returns true if the token is a keyword, false if not
def isKeyword(token):
    keywords = ['abort', 'abs', 'abstract', 'accept', 'access', 'aliased', 'all', 'and', 'array', 'at', 'begin', 'body', 'case', 'constant', 'declare', 'delay', 'delta', 'digits', 'do', 'else', 'elseif', 'end', 'entry', 'exception', 'exit', 'for', 'function', 'generic', 'goto', 'if', 'in', 'interface', 'is', 'limited', 'loop', 'mod', 'new', 'not', 'null', 'of', 'or', 'others', 'out', 'overriding', 'package', 'pragma', 'private', 'procedure', 'protected', 'raise', 'range', 'record', 'rem', 'renames', 'requeue', 'return', 'reverse', 'select', 'seperate', 'some', 'subtype', 'synchronized', 'tagged', 'task', 'terminate', 'then', 'type', 'until', 'use', 'when', 'while', 'with', 'xor']
    for keyword in keywords:
        if keyword == token:
            return True
    return False

#Chekcs if the input token is a delimiter of the ADA language
#Returns true if the token is a delimiter, false if not
def isDelimiter(token):
    single_delimiters = ['&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '|']
    compound_delimiters = ['=>', '..', '**', ':=', '/=', '>=', '<=', '<<', '>>', '<>']
    other_delimiters = ['\"', '#', '[', ']', '{', '}']
    
    for single_delimiter in single_delimiters:
        if single_delimiter == token:
            return True
    
    for compound_delimiter in compound_delimiters:
        if compound_delimiter == token:
            return True

    for other_delimiter in other_delimiters:
        if other_delimiter == token:
            return True

    return False

#Checks if token is an integer
#Returns true if the token is an integer, false if not
def isInteger(token):
    return token.isdigit()

#Checks if token is a float
#Returns true if the token is a float, false if not
def isFloat(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

#Checks if token is a boolean value
#Returns true if the token is a boolean value, false if not
def isBoolean(token):
    return (token.lower() == 'true' or token.lower() == 'false')

#Checks if token is an identifier
#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). 
#A valid identifier cannot start with a number, or contain any spaces.
#Returns true if the token is an identifier, false if not
def isIdentifier(token):
    return token.isidentifier()

#Checks if token starts with the comment syntax (--)
#Returns true if the token starts with the comment syntax, false if not
def isComment(token):
    return token.startswith('--')

#Checks if token starts or ends with the string syntax ("")
#Returns true if the token starts or ends with the string syntax, false if not
def isString(token):
    return token.startswith("\"") or token.endswith('\"')

#Classify a token putting its type into an array
#Returns an array 
#   Array: [token, type, line number]
def classifyToken(token, line_number):

    #runs through all these forms of classificaiton

    if isKeyword(token):
        return [token, 'keyword', line_number]

    if isDelimiter(token):
        return [token, 'delimiter', line_number]

    if isInteger(token):
        return [token, 'integer', line_number]

    if isFloat(token):
        return [token, 'float', line_number]

    if isBoolean(token):
        return [token, 'boolean', line_number]

    if isIdentifier(token):
        return [token, 'identifier', line_number]
    
    if isComment(token):
        return True

    if isString(token):
        return True

    #if the token isnt one of the above things, defaults to unclassified
    return [token, 'unclassified', line_number]

#Takes the 2-D array of tokens and classifies all 
def classifyAll(tokens):
    classifiedTokens = []

    #Loop through all the tokens 
    line_number = 0
    comment = False
    string = 0
    for line in tokens:
        line_number += 1
        for token in line:
            if isComment(token):
                comment = True
            if comment != True:
                if isString(token):
                    string += 1
                if string == 0:
                    classifiedTokens.append(classifyToken(token, line_number))
                else:
                    if string == 2:
                        string = 0
                    classifiedTokens.append([token, 'string', line_number])
            else:
                classifiedTokens.append([token, 'comment', line_number])
        comment = False        
    return classifiedTokens


#Global Variable (2-D Array) that holds all the classified tokens, and their line number in order from left to right
#Each element is a classified token
#    Classified Token:  [token value, token type, line number]
#    Example:           [10, 'intgeger', 4]
#       so this token value is 10, its an integer, and its on line 4
global classifiedTokens
classifiedTokens = []

#Main function
def main():
    #Reads the test file putting into array of lines of code
    file1 = read('testfile.adb')

    #Translates into tokens
    tokens1 = generateTokens(file1)

    #Classifies each token
    classifiedTokens1 = classifyAll(tokens1)

    #Prints to show that we successfully stored all the variables
    print('Classified Tokens:', classifiedTokens1)

#runs the main function
main()