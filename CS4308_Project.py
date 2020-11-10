from ada_scanner import Scanner
     
def main():
     file1 = Scanner('test files/testfile.adb')

     lines_to_parse = [  7,8,9,10,11,        #type and assignment
                         14,15,16,           #functions
                         18,19,              #functions
                         21,22,24,            #conditional
                         30,33,36,39]        #errors

     file1.parseLines(lines_to_parse)
     
main()

