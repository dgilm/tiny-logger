#!/usr/bin/python

from distutils.core import setup

import glob
import os

data = [
    ('/usr/share/tiny-logger/TinyLogger',
        glob.glob(os.path.join('TinyLogger', '*.py'))),
    ('/etc/cron.hourly', ['cron.hourly/tiny-logger']),
    ('/etc/rsyslog.d', ['etc/syslog/tiny-logger.rsyslog.conf']),
]

setup (
    name = "tiny logger",
    version = "0.1",
    description = "Tiny Logger",
    author = "David Gil",
    author_email = "dgil@abadasoft.com",
    scripts = [ 'tiny-logger' ],
    data_files = data
)
