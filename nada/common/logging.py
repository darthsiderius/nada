#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
from datetime import date
import uuid
# get from global configs
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
LOG_DIR = BASE_DIR + "/../../logs/"
# have default logging statements
# extract to configs
REQUEST_ID = None
ACTIVE_LOGFILE = None

def setupLogger():
    # assign request id
    REQUEST_ID = uuid.uuid4().hex[:6]

    os.makedirs(os.path.dirname(LOG_DIR), exist_ok=True)
    global ACTIVE_LOGFILE
    today = str(date.today())
    ACTIVE_LOGFILE = LOG_DIR + today + '.log'
    old_factory = logging.getLogRecordFactory()

    def record_factory(*args, **kwargs):
        record = old_factory(*args, **kwargs)
        record.request_id = REQUEST_ID
        return record

    logging.basicConfig(filename=ACTIVE_LOGFILE, format='%(asctime)-5s %(levelname)-6s @%(request_id)-7s [%(filename)s:%(lineno)d] %(funcName)s() -> %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)  
    logging.setLogRecordFactory(record_factory)
    logging.info("setupLogger() - logger started")

def listLogFiles():
    print("* Log Files:\n")
    os.system("ls " + LOG_DIR + "* -tla")
    print("\n")
    
def showLogs():
    print("* Active Log File: " + ACTIVE_LOGFILE)
    with open(ACTIVE_LOGFILE, 'r') as fin:
        print(fin.read())

def searchLogs():
    print("* Searching logs: ")


def deleteAllLogs():
    print("Are you sure you want to remove all NDA logs?")
    removeCmd = "rm " + LOG_DIR + "/*"
    os.system(removeCmd)
    print("All logs are removed")  