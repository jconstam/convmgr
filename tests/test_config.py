# import os
# import json
# import shutil
# import pytest

# from convmgr import config

# rootPath = os.path.dirname( os.path.realpath( __file__ ) )
# filePath = os.path.join( rootPath, config.convmgrconfig.fileName )

# @pytest.fixture
# def testData( ):
#     return config.convmgrconfig( rootPath )

# def setupPath( path ):
#     if os.path.exists( path ):
#         shutil.rmtree( path )
#     os.mkdir( path )
# def setupRoot( ):
#     setupPath( rootPath )

# def test_constructor( testData ):
#     assert testData.filePath == os.path.join( rootPath, config.convmgrconfig.fileName )
#     assert not testData.data

# @pytest.mark.parametrize( 'fileName', [ config.convmgrconfig.fileName, 'file1.json', 'file2' ] )
# def test_readFile( testData, fileName ):
#     setupRoot( )

#     with open( os.path.join( rootPath, fileName ), 'w+' ) as json_file:
#         json.dump( { 'testKey1': 'testValue1', 'testKey2': 4 }, json_file )
    
#     testData.readFile( )
#     if config.convmgrconfig.fileName == fileName:
#         assert 'testKey1' in testData.data
#         assert testData.data[ 'testKey1' ] == 'testValue1'
#         assert 'testKey2' in testData.data
#         assert testData.data[ 'testKey2' ] == 4
#     else:
#         assert not 'testKey1' in testData.data
#         assert not 'testKey2' in testData.data
    
#     shutil.rmtree( rootPath )