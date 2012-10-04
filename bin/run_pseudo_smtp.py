#!/usr/bin/env python

from argparse import ArgumentParser
import os
import sys

base = os.path.dirname(os.path.abspath(sys.argv[0]))
modules = [ '', 'server', 'utils', 'agents', 'modules' ]
for m in modules:
    path = os.path.abspath(os.path.join(base, '../src', m))
    if not path in sys.path:
        sys.path.insert(0,path)

import smtp_server
from config import smtp_server_domain, smtp_server_port
from log import log, set_foreground_logger
from db_utils import does_database_exist, verify_schema, create_database, initialize_database
import daemon

class PseudoSMTPDaemon(daemon.Daemon):
    def run(self):
        smtp_server.start()


def _setup_db():
    if not does_database_exist():
        log.info("Database missing. Attempting to create")
        if create_database():
            if initialize_database():
                log.info("Database successfully initialized")
            else:
                log.error("Error encountered initalizing database")
        else:
            log.error("Error encountered creating database")
    else:
        if not verify_schema():
            if initialize_database():
                log.info("Database successfully initialized")



if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-d", "--daemon", help="run as a daemon")
    parser.add_argument("-a", "--address", default=smtp_server_domain, help="bind address")
    parser.add_argument("-p", "--port", type=int, default=smtp_server_port, help="bind port")
    args = parser.parse_args()

    if not args.daemon:
        set_foreground_logger()
        _setup_db()
        # not daemon, just run in foreground.
        log.info("Starting smtp listener on as %s:%s", smtp_server_domain, str(smtp_server_port))
        smtp_server.start()
    else:
        daemon = PseudoSMTPDaemon('/tmp/pseudo_smtp.pid')
        if args.daemon == 'start':
            _setup_db()
            daemon.start()
        elif args.daemon == 'stop':
            daemon.stop()
        elif args.daemon == 'restart':
            daemon.restart()
        elif args.daemon == 'status':
            daemon.status()

