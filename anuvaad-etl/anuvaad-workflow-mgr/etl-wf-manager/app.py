#!/bin/python
import logging
import os
import threading

from flask import Flask
from logging.config import dictConfig
from kafkawrapper.wfmconsumer import consume
from controller.wfmcontroller import wfmapp

log = logging.getLogger('file')
app_host = os.environ.get('ANU_ETL_WFM_HOST', '0.0.0.0')
app_port = os.environ.get('ANU_ETL_WFM_PORT', 5000)



def start_consumer():
    print("Consumer starting")
    try:
        t1 = threading.Thread(target=consume, name='keep_on_running')
        t1.start()
    except Exception as e:
        print('ERROR WHILE RUNNING CUSTOM THREADS ' + str(e))


if __name__ == '__main__':
    start_consumer()
    wfmapp.run(host=app_host, port=app_port)




# Log config
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] {%(filename)s:%(lineno)d} %(threadName)s %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'info': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'default',
            'filename': 'info.log'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        }
    },
    'loggers': {
        'file': {
            'level': 'DEBUG',
            'handlers': ['info', 'console'],
            'propagate': ''
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['info', 'console']
    }
})