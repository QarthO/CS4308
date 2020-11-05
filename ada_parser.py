#Scanner
#Derek, Thomas, Kellen

class Parser:

    def __init__(self, tokens):

    syntaxErrors = []

    #print parser output
    def getOutput():
        #loop for chopping up input from scanner into lines
        for x in tokens.length:
            line = [token for token in tokens if token.get('line_number') == x]

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

