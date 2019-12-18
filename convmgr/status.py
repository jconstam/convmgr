import os
import json

from enum import Enum

class FILE_STATUS( Enum ):
    WAITING = 1
    IN_PROGRESS = 2
    DONE = 3

class convmgrstatus:
    def __init__( self, rootPath ):
        self.clearData( )
        self.fileName = os.path.join( rootPath, '.convmgrstatus.json' )

    def loadFile( self ):
        with open( self.fileName, 'r' ) as json_file:
            self.data = json.load( json_file )
    def saveFile( self ):
        with open( self.fileName, 'w+' ) as json_file:
            json.dump( self.data, json_file )
    
    def clearData( self ):
        self.data = { }
    
    def addFile( self, fileName, fileStatus ):
        if not self.data:
            self.clearData( )
        
        key = '{}'.format( fileStatus )
        if not key in self.data:
            self.data[ key ] = [ fileName ]
        else:
            self.data[ key ].append( fileName )