#!/usr/bin/env python

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
from log import log
from db_utils import does_database_exist, verify_schema, create_database, initialize_database

if __name__ == '__main__':
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

    log.info("Starting smtp listener on as " + smtp_server_domain + ":" + str(smtp_server_port)) 
    smtp_server.start();

