from ada_scanner import Scanner
     
def main():
     file1 = Scanner('test files/testfile.adb')

     lines_to_parse = [  7,8,9,10,11,        #type and assignment
                         14,15,16,           #functions
                         18,19,              #functions
                         21,22,23,24,25]     #conditional

     file1.parseLines([11])
     # lines = file1.getLines()

     # line = 15
     # test_tokens = file1.seperate(lines[line-1])
     # print(test_tokens)
main()

