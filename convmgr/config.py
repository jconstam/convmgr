import os
import json

class convmgrconfig:
    fileName = 'convmgrconfig.json'

    def __init__( self, rootPath ):
        self.filePath = os.path.join( rootPath, convmgrconfig.fileName )
        self.data = { }

    def readFile( self ):
        if os.path.exists( self.filePath ):
            with open( self.filePath, 'r' ) as json_file:
                self.data = json.load( json_file )
    
    def getValue( self, valueName ):
        if valueName in self.data:
            return self.data[ valueName ]
        else:
            return ''
