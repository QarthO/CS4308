from ada_scanner import Scanner

def main():
     file1 = Scanner('test files/testfile.adb')
     tokens = file1.getTokens()

main()