import os
import json
import pytest
import shutil

from pathlib import Path

from convmgr import request

rootPath = os.path.join( os.path.dirname( os.path.realpath( __file__ ) ), 'test' )

@pytest.fixture
def testData( ):
    return request.convmgrrequest( )

def touchFile( filePath ):
    Path( filePath ).touch( )

def setupPath( path ):
    if os.path.exists( path ):
        shutil.rmtree( path )
    os.mkdir( path )
def setupRoot( ):
    setupPath( rootPath )

def test_constructor( testData ):
    assert not testData.reqFileList
    assert not testData.getOutputFileList( )

def test_scanForFilesNoFolder( testData ):
    if os.path.exists( rootPath ):
        shutil.rmtree( rootPath )

    testData.scanForFiles( rootPath )
    assert not testData.reqFileList
    assert not testData.getOutputFileList( )

@pytest.mark.parametrize( 'fileList', [ ( 'file1' ), ( 'file1', 'file2.json' ), ( 'file1', 'file2.json', 'file3.json', 'file4.json', 'file5' ) ] )
def test_scanForFiles( testData, fileList ):
    setupRoot( )
    for file in fileList:
        touchFile( os.path.join( rootPath, file ) )
    
    testData.scanForFiles( rootPath )
    for file in fileList:
        filePath = os.path.join( file, rootPath )
        if filePath.endswith( '.json' ):
            assert filePath in testData.reqFileList
        else:
            assert not filePath in testData.reqFileList

    assert not testData.getOutputFileList( )

    shutil.rmtree( rootPath )

def test_processFilesMKVNoFolder( testData ):
    testPath = os.path.join( rootPath, 'testPath' )
    setupRoot( )
       
    testFileName = os.path.join( rootPath, 'test1.json' )
    testFileData = { 'rootPath': testPath, 'extensions': [ 'mkv' ] }

    with open( testFileName, 'w+' ) as json_file:
        json.dump( testFileData, json_file )

    testData.scanForFiles( rootPath )
    assert testFileName in testData.reqFileList
    testData.processFiles( )
    assert not testData.getOutputFileList( )

    shutil.rmtree( rootPath )

@pytest.mark.parametrize( 'fileList', [ ( 'file1' ), ( 'file1', 'file2.mkv' ), ( 'file1', 'file2.mkv', 'file3.mkv', 'file4.mkv', 'file5' ) ] )
def test_processFilesMKV( testData, fileList ):
    testPath = os.path.join( rootPath, 'testPath' )
    setupRoot( )
    setupPath( testPath )
       
    testFileName = os.path.join( rootPath, 'test1.json' )
    testFileData = { 'rootPath': testPath, 'extensions': [ 'mkv' ] }

    for file in fileList:
        touchFile( os.path.join( testPath, file ) )

    with open( testFileName, 'w+' ) as json_file:
        json.dump( testFileData, json_file )

    testData.scanForFiles( rootPath )
    assert testFileName in testData.reqFileList
    testData.processFiles( )
    outputList = testData.getOutputFileList( )

    for file in fileList:
        filePath = os.path.join( testPath, file )
        if filePath.endswith( 'mkv' ):
            assert filePath in outputList
        else:
            assert not filePath in outputList

    shutil.rmtree( rootPath )
    