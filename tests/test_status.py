import os
import pytest

from convmgr import status
from tests import common

def setup_function( ):
    common.setupRoot( )
def teardown_function( ):
    common.cleanupRoot( )

@pytest.fixture
def testData( ):
    return status.convmgrstatus( common.rootPath )
@pytest.fixture
def testDataNotEmpty( ):
    data = status.convmgrstatus( common.rootPath )
    data.addData( 'key1', 'value1' )
    data.addData( 'key2', 'value2' )
    data.addData( 'key3', 'value3' )
    return data
    
def test_constructor( testData ):
    assert testData.fileName == common.createTestPath( status.convmgrstatus.fileName )

def test_addDataEmpty( testData ):
    assert not testData.data

    testData.addData( 'key1', 'value1' )
    assert testData.data[ 'key1' ] == 'value1'

    testData.clearData( )
    assert not testData.data

def test_addDataNotEmpty( testDataNotEmpty ):
    testDataNotEmpty.addData( 'key4', 'value4' )
    assert testDataNotEmpty.data[ 'key4' ] == 'value4'

    testDataNotEmpty.clearData( )
    assert not testDataNotEmpty.data

def test_readWriteFile( testDataNotEmpty ):
    filePath = common.createTestPath( status.convmgrstatus.fileName )
    if os.path.exists( filePath ):
        os.remove( filePath )

    testDataNotEmpty.saveFile( )
    assert os.path.exists( filePath )

    newData = status.convmgrstatus( common.rootPath )
    newData.loadFile( )

    for type in testDataNotEmpty.data:
        assert type in newData.data
        for file in testDataNotEmpty.data[ type ]:
            assert file in newData.data[ type ]            
