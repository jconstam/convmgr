# Conversion Manager
## Overview
A simple manager tool for Handbrake or similar video conversion applications.
Designed to run as a cronjob.  Takes in requests of new paths of videos to convert and then monitors their progression through being queued, converted, and finished.
Supports Python 3.5, 3.6, 3.7, 3.8

[![Build Status](https://dev.azure.com/callmebob0963/GitHub%20Projects/_apis/build/status/jconstam.convmgr?branchName=master)](https://dev.azure.com/callmebob0963/GitHub%20Projects/_build/latest?definitionId=8&branchName=master)
[![Build Status](https://travis-ci.org/jconstam/convmgr.svg?branch=master)](https://travis-ci.org/jconstam/convmgr)

## Command Overview
`convmgr -i <workPath> -o <outputDir> -w <watchDir>`
workPath - The root directory where Handbrake is managing videos.
outputDir - The directory under the root where Handbrake stores video files after they are converted.  Optional - defaults to "Output"
watchDir - The directory under the root which Handbrake monitors to automatically convert video files.  Optional - defaults to "Watch"

## High-Level Design
1. Check for new requests
1. Copy any requests to the watch folder - set status to WAITING
1. Process files by status
    1. WAITING
        1. If a copy exists in a temporary folder inside the output folder - set status to IN_PROGRESS.
        1. Else if still in the watch folder - do nothing.
    1. IN_PROGRESS
        1. If a copy exists in a temporary folder inside the output folder - do nothing.
        1. Else if not in the watch folder - set status to DONE.
    1. DONE
        1. If a copy exists in the output folder - do nothing.
        1. Else - remove.

## Requests
Any requests can be added via a JSON snippet file.  This file should be a dictionary containing two key/value pairs:
1. rootPath - A string containing the path to the folder containing the videos.  Must be an absolute path.
1. extensions - A list containing the file extensions to grab.

## Configuration
In order to configure the system, a JSON file named "config.json" should be placed in the root directory.
The following values are supported:
Value Name|Description
----------------------
pbAPIKey|API Key for Pushbullet. If not specified, notifications are disabled.

## Notification
Notifications are managed through Pushbullet.

## Todo
- [x] Add status module
- [x] Add request module
- [ ] Add config module
- [ ] Add notification module
- [ ] Add state machine
- [ ] Setup to deploy on PyPi