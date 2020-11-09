#Scanner
#Derek, Thomas, Kellen

class Parser:

    def __init__(self, tokens):

    syntaxErrors = []

    def parse(self, tokens):
        counter = 0
        tokenCounter = 1
        previous = 0
        for x in tokens:
            if (tokens.get('line_number')>6 and tokens.get('line_number')<12) or (tokens.get('line_number')>13 and tokens.get('line_number')<26):
                if tokens.get('line_number')!=counter:
                    counter = tokens.get('line_number')
                    #tree starts
                    root.data = x
                if tokens.get('type') = 'delimiter':
                    temp.data = root
                    root.data = x
                    root.left = temp


    #print parser output
    def getOutput():
        #loop for chopping up input from scanner into lines
        for x in tokens.length:
            line = [token for token in tokens if token.get('line_number') == x]

class Node:

    def __init__(self, data):
    
        # left child
        self.left = None
        # right child
        self.right = None
        # node's value
        self.data = data

#need to build out tree class
class Tree:

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

#import list of tokens from scanner
#split array into individual lines
#parse tokens from each line


#print line of code

#detect errors
#need line #, token #, an example of the BNF grammar
#display the expression causing the error
#description of what syntax is expected

#parse tree output

#output in post-fix notation