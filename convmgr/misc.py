#!/usr/bin/python3

import os
import argparse

def parseArgs( ):
    parser = argparse.ArgumentParser( description='Conversion Manager' )
    parser.add_argument( '-d', '--workPath', type=str, required=True, help='Root directory of path to be managed' )
    parser.add_argument( '-i', '--inputDir', type=str, required=False, default='Input', help='Relative dir inside workPath for input directory' )
    parser.add_argument( '-o', '--outputDir', type=str, required=False, default='Output', help='Relative dir inside workPath for output directory' )
    parser.add_argument( '-w', '--watchDir', type=str, required=False, default='Watch', help='Relative dir inside workPath for watch directory' )

    return parser.parse_args( )

def createDir( path ):
    if not os.path.exists( path ):
        os.mkdir( path )
def setupDirectories( args ):
    root = os.path.realpath( args.workPath )
    createDir( root )
    createDir( os.path.join( root, args.inputDir ) )
    createDir( os.path.join( root, args.outputDir ) )
    createDir( os.path.join( root, args.watchDir ) )
