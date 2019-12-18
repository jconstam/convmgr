import os
import pytest
import shutil

from pathlib import Path

from convmgr import request

rootPath = os.path.join( os.path.dirname( os.path.realpath( __file__ ) ), 'test' )

@pytest.fixture
def testData( ):
    return request.convmgrrequest( )

def test_constructor( testData ):
    assert not testData.reqFileList

def test_scanForFilesNoFolder( testData ):
    if os.path.exists( rootPath ):
        shutil.rmtree( rootPath )

    testData.scanForFiles( rootPath )
    assert not testData.reqFileList

@pytest.mark.parametrize( 'fileList', [ ( 'file1' ), ( 'file1', 'file2.json' ), ( 'file1', 'file2.json', 'file3.json', 'file4.json', 'file5' ) ] )
def test_scanForFiles( testData, fileList ):
    if os.path.exists( rootPath ):
        shutil.rmtree( rootPath )
    os.mkdir( rootPath )
    for file in fileList:
        Path( os.path.join( rootPath, file ) ).touch( )
    
    testData.scanForFiles( rootPath )
    for file in fileList:
        filePath = os.path.join( file, rootPath )
        if filePath.endswith( '.json' ):
            assert filePath in testData.reqFileList
        else:
            assert not filePath in testData.reqFileList

    shutil.rmtree( rootPath )


    