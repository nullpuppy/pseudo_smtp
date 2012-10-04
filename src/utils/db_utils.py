from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

from models.mail import Base
from config import database_url, log_level, log_format, log_datefmt
import logging

logging.basicConfig(format=log_format,datefmt=log_datefmt)
log = logging.getLogger(__name__)
log.setLevel(log_level)

engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()

class QueryError:
    AccessDenied = 1044
    AccessDeniedUsingPassword = 1045
    UnknownDatabase = 1049

def create_database():
    database_uri, database_name = database_url.rsplit('?', 1)[0].rsplit('/', 1)
    try:
        tmpEngine = create_engine(database_uri)
        tmpEngine.execute("CREATE DATABASE " + database_name)
        tmpEngine.dispose()
    except OperationalError, e:
        log.exception(e)
        return False
    return True

def initialize_database():
    try:
        Base.metadata.create_all(bind=engine)
    except OperationalError, e:
        log.exception(e)
        return False
    return True

def does_database_exist():
    try:
        engine.execute("SELECT 1")
    except OperationalError, e:
        if e.message.find(str(QueryError.UnknownDatabase)) > -1:
            return False
        log.exception(e)
        return False
    except Exception, e:
        log.exception(e)
        return False
    return True

def verify_schema():
    """ Verify the schema of the existing DB.
        Currently just verifies that table_names match what is expected.

        TODO: Add full schema verification.
    """
    try:
        model_tables = map(unicode,Base.metadata.tables.keys())
        db_tables = engine.table_names()

        if model_tables == db_tables:
            return True
        else:
            return False
    except OperationalError, e:
        log.exception(e)

