'''
Created on Feb 12, 2015

@author: vivek
'''

from __future__ import absolute_import

from celery import Celery

# instantiate Celery object
celery = Celery(include=[
                        'mytask'
                        ])

# import celery config file
celery.config_from_object('configuration')

if __name__ == '__main__':
    celery.start()
