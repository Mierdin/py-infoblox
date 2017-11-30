#!/usr/bin/env python


"""
infoblox-cli is the Infoblox CLI client application.

It is used for getting, creating, updating and
removing of objects from an Infoblox server instance.

"""

from docopt import docopt
from infoblox.core import Infoblox

def main():
    
    #args = docopt(usage, version='0.1.0')

    import os.path
    if os.path.isfile('infoblox.conf'):
      ib = Infoblox('infoblox.conf')
    else:
      print "Error importing conf file"

    #if args['get']:
    #    result = ib.get_object(args['--type'], args['--data'])
    #elif args['create']:
    #    result = ib.create_object(args['--type'], args['--data'])
    #elif args['update']:
    #    result = ib.update_object(args['--ref'], args['--data'])
    #elif args['remove']:
    #    result = ib.remove_object(args['--ref'])

    for x in range(0, 255):
        for y in range(0, 255):
            result = ib.create_object('network', '{ "network": "10.' + str(x) + '.' + str(y) + '.0/24", "comment": "Test network ' + str(x) + str(y) + '" }')
            print result

        
if __name__ == '__main__':
    main()


