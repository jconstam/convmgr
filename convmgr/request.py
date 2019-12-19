import os
import json

class convmgrrequest:
    def __init__( self ):
        self.reqFileList = [ ]
        self.outFileList = [ ]
    
    def scanForFiles( self, rootPath ):
        if os.path.exists( rootPath ):
            for file in os.listdir( rootPath ):
                if file.endswith( '.json' ):
                    self.reqFileList.append( os.path.join( rootPath, file ) )
    
    def __processFolder__( self, path, extensions ):
        if os.path.exists( path ):
            for file in os.listdir( path ):
                for ext in extensions:
                    if file.endswith( ext ):
                        self.outFileList.append( os.path.join( path, file ) )
    def processFiles( self ):
        for filePath in self.reqFileList:
            with open( filePath, 'r' ) as json_file:
                data = json.load( json_file )
                self.__processFolder__( data[ 'rootPath' ], data[ 'extensions' ] )
    
    def getOutputFileList( self ):
        return self.outFileList
