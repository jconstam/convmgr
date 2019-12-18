import os
import pytest

from convmgr import status

rootPath = os.path.dirname( os.path.realpath( __file__ ) )
filePath = os.path.join( rootPath, '.convmgrstatus.json' )

@pytest.fixture
def testData( ):
    return status.convmgrstatus( rootPath )
@pytest.fixture
def testDataNotEmpty( ):
    data = status.convmgrstatus( rootPath )
    data.addFile( 'waitFile', status.FILE_STATUS.WAITING )
    data.addFile( 'progFile', status.FILE_STATUS.IN_PROGRESS )
    data.addFile( 'doneFile', status.FILE_STATUS.DONE )
    return data
    
def test_constructor( testData ):
    assert testData.fileName == filePath

@pytest.mark.parametrize( 'type', [ status.FILE_STATUS.WAITING, status.FILE_STATUS.IN_PROGRESS, status.FILE_STATUS.DONE ] )
def test_addDataEmpty( testData, type ):
    assert not testData.data

    testData.addFile( 'file1', str( type ) )
    assert 'file1' in testData.data[ str( type ) ]

    testData.clearData( )
    assert not testData.data

@pytest.mark.parametrize( 'type', [ status.FILE_STATUS.WAITING, status.FILE_STATUS.IN_PROGRESS, status.FILE_STATUS.DONE ] )
def test_addDataNotEmpty( testDataNotEmpty, type ):
    assert testDataNotEmpty.data
    assert testDataNotEmpty.data[ str( status.FILE_STATUS.WAITING ) ]
    assert testDataNotEmpty.data[ str( status.FILE_STATUS.IN_PROGRESS ) ]
    assert testDataNotEmpty.data[ str( status.FILE_STATUS.DONE ) ]

    testDataNotEmpty.addFile( 'file2', str( type ) )
    assert 'file2' in testDataNotEmpty.data[ str( type ) ]

    testDataNotEmpty.clearData( )
    assert not testDataNotEmpty.data

def test_readWriteFile( testDataNotEmpty ):
    if os.path.exists( filePath ):
        os.remove( filePath )
    testDataNotEmpty.saveFile( )

    newData = status.convmgrstatus( rootPath )
    newData.loadFile( )

    for type in testDataNotEmpty.data:
        assert type in newData.data
        for file in testDataNotEmpty.data[ type ]:
            assert file in newData.data[ type ]
    
    os.remove( filePath )
            
