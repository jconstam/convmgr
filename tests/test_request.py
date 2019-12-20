import os
import json
import pytest
import shutil

from convmgr import request
from tests import common

def setup_function( ):
    common.setupRoot( )
def teardown_function( ):
    common.cleanupRoot( )

@pytest.fixture
def testData( ):
    return request.convmgrrequest( )

def test_constructor( testData ):
    assert not testData.reqFileList
    assert not testData.getOutputFileList( )

def test_scanForFilesNoFolder( testData ):
    common.cleanupRoot( )
    testData.scanForFiles( common.rootPath )
    assert not testData.reqFileList
    assert not testData.getOutputFileList( )

@pytest.mark.parametrize( 'fileList', [ ( 'file1' ), ( 'file1', 'file2.json' ), ( 'file1', 'file2.json', 'file3.json', 'file4.json', 'file5' ) ] )
def test_scanForFiles( testData, fileList ):
    for file in fileList:
        common.touchFile( common.createTestPath( file ) )
    
    testData.scanForFiles( common.rootPath )
    for file in fileList:
        filePath = common.createTestPath( file )
        if filePath.endswith( '.json' ):
            assert filePath in testData.reqFileList
        else:
            assert not filePath in testData.reqFileList

    assert not testData.getOutputFileList( )

def test_processFilesMKVNoFolder( testData ):
    testPath = common.createTestPath( 'testPath' )
       
    testFileName = common.createTestPath( 'test1.json' )
    testFileData = { 'rootPath': testPath, 'extensions': [ 'mkv' ] }

    with open( testFileName, 'w+' ) as json_file:
        json.dump( testFileData, json_file )

    testData.scanForFiles( common.rootPath )
    assert testFileName in testData.reqFileList
    testData.processFiles( )
    assert not testData.getOutputFileList( )

@pytest.mark.parametrize( 'fileList', [ ( 'file1' ), ( 'file1', 'file2.mkv' ), ( 'file1', 'file2.mkv', 'file3.mkv', 'file4.mkv', 'file5' ) ] )
def test_processFilesMKV( testData, fileList ):
    testPath = common.createTestPath( 'testPath' )
    common.setupPath( testPath )
       
    testFileName = common.createTestPath( 'test1.json' )
    testFileData = { 'rootPath': testPath, 'extensions': [ 'mkv' ] }

    for file in fileList:
        common.touchFile( os.path.join( testPath, file ) )

    with open( testFileName, 'w+' ) as json_file:
        json.dump( testFileData, json_file )

    testData.scanForFiles( common.rootPath )
    assert testFileName in testData.reqFileList
    testData.processFiles( )
    outputList = testData.getOutputFileList( )

    for file in fileList:
        filePath = os.path.join( testPath, file )
        if filePath.endswith( 'mkv' ):
            assert filePath in outputList
        else:
            assert not filePath in outputList
    