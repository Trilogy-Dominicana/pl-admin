#!/usr/bin/python
import sys, getopt, json

from src.database import Database
from src.files import Files

def main(argv):
    ''' Main function to execute command line '''

    emethod = ''
    try:
        opts, arg = getopt.getopt(argv, "hie:", ["emethod="])
    except getopt.GetoptError:
        # print('Something wrong with the args. type -h to see help ')
        sys.exit(2)

    
    
    for opt, arg in opts:
        if opt in ('-i'):
            ''' List invalid packages on DB '''
            
            # files = Files()
            # print(files.objType.package)

            db = Database()
            # result = db.listInvalidObjects(status='INVALID')[0]
            db.compileObj()

            # print(result['object_name'])
            # print(result)

            
        elif opt in ("-e", "--emethod"):
            emethod = arg
        else:
            print('Available opcions -e <method_name>\n')
            sys.exit('0')

if __name__ == "__main__": 
    main(sys.argv[1:])
