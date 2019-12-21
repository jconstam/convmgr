#!/usr/bin/python3

import pytest
import datetime

import pushbullet

from convmgr import notification, config, status
from tests import common

try:
    from unittest import mock  # python 3.3+
except ImportError:
    import mock  # python 2.6-3.2

testConfigFile = config.convmgrconfig( common.rootPath )
testStatusFile = status.convmgrstatus( common.rootPath )
testDate = datetime.datetime( 2002, 5, 6, 2, 35, 19 )

def setup_function( ):
    common.setupRoot( )
def teardown_function( ):
    common.cleanupRoot( )

@pytest.fixture
def testDataEmpty( ):
    return notification.convmgrnotification( testConfigFile, testStatusFile )
@pytest.fixture
def testData( ):
    testConfigFile.data[ notification.convmgrnotification.__pushbulletAPIKey_Key__ ] = 'A_KEY'
    testConfigFile.data[ notification.convmgrnotification.__maxNotifyPeriod_Key__ ] = 1
    testStatusFile.data[ notification.convmgrnotification.__lastNotifyTime_Key__ ] = testDate.strftime( notification.convmgrnotification.__datetimeFormat__ )
    return notification.convmgrnotification( testConfigFile, testStatusFile )

def test_constructorDefaults( testDataEmpty ):
    assert testDataEmpty.configFile
    assert testDataEmpty.statusFile
    assert not testDataEmpty.pb
    assert testDataEmpty.maxNotifyPeriod == notification.convmgrnotification.__defaultMaxNotifyPeriod__
    assert ( testDataEmpty.lastNotifyTime - datetime.datetime.now( ) ).total_seconds( ) < 1

def test_constructor( testData ):
    assert testData.configFile
    assert testData.statusFile
    assert not testData.pb
    assert testData.maxNotifyPeriod == 1
    assert testData.lastNotifyTime == testDate