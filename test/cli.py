import sys


from docopt import docopt

import test


documentation={}

documentation['help'] = '''

Usage:
     
    testproj -h | --help
    testproj -v | --version
     

Options:
    -h --help               show this screen.
    -v --verbose            show more log.
    -s --settings=<file>    specify a setting file.
    -p --port=<port>        specify the server port.
    -f --force              search a theme without cache
    -c --clean              show theme name only.
    --version               show version.

'''

documentation['version']='''
Usage:
    liquidluck create [-s <file>|--settings=<file>]

Options:
    -h --help               show this screen.
    -s --settings=<file>    specify a setting file.
"""

'''


def main():
     
    command = 'help'
    if len(sys.argv) > 1:
        command = sys.argv[1]
    if command in documentation:
        args = docopt(documentation[command])
    else:
        args = docopt(
            documentation['help'],
             
        )


def hello():
    print "say hello!!!" 



if __name__ == '__main__':
    main()