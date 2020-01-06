#!/usr/bin/python3

import datetime
import pushbullet

from convmgr import config, status

class convmgrnotification:
    __defaultMaxNotifyPeriod__ = 60
    __datetimeFormat__ = '%Y/%m/%d %H:%M:%S'
    __pushbulletAPIKey_Key__ = 'pbAPIKey'
    __maxNotifyPeriod_Key__ = 'maxNotifyPeriod'
    __lastNotifyTime_Key__ = 'lastNotifyTime'

    def __init__( self, configFile, statusFile ):
        self.configFile = configFile
        self.statusFile = statusFile

        try:
            self.pb = pushbullet.Pushbullet( self.configFile.getValue( convmgrnotification.__pushbulletAPIKey_Key__ ) )
        except:
            self.pb = None

        self.maxNotifyPeriod = self.configFile.getValue( convmgrnotification.__maxNotifyPeriod_Key__ )
        if not self.maxNotifyPeriod:
            self.maxNotifyPeriod = convmgrnotification.__defaultMaxNotifyPeriod__

        lastNotifyTime = self.statusFile.getData( convmgrnotification.__lastNotifyTime_Key__ )
        if lastNotifyTime:
            self.lastNotifyTime = datetime.datetime.strptime( lastNotifyTime, convmgrnotification.__datetimeFormat__ )
        else:
            self.lastNotifyTime = datetime.datetime.now( )
    
    def doNotify( self, watchCount, outCount ):
        if self.pb:
            currTime = datetime.datetime.now( )
            if ( currTime - self.lastNotifyTime ).total_seconds( ) >= self.maxNotifyPeriod:
                self.pb.push_note( 'Sync Files', 'Date: {}\nTime: {}\nWatch: {}\nOutput: {}'.format( 
                    currTime.strftime( '%Y/%m/%d' ), currTime.strftime( '%H:%M:%S'), watchCount, outCount ) )
                self.lastNotifyTime = currTime

