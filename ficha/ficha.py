#!/usr/bin/python3

__version__ = '0.1'

def main():
    """ Function doc """
    import sys
    from os.path import dirname, realpath, exists
    filePath = dirname(realpath(__file__))
    if exists(filePath + '/images/ficha.png'):
        print( 'found: ' + filePath + '/images/ficha.png')
    else:
        print('no existe' + filePath + '/images/ficha.png')



if __name__ == '__main__':
    main()
