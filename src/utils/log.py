from config import log_level, log_format, log_datefmt, log_filename
import logging

_formatter = logging.Formatter(log_format, log_datefmt)

_streamHandler = logging.StreamHandler()
_streamHandler.setLevel(log_level)
_streamHandler.setFormatter(_formatter)

_fileHandler = logging.FileHandler(log_filename)
_fileHandler.setLevel(log_level)
_fileHandler.setFormatter(_formatter)

log = logging.getLogger(__name__)
log.addHandler(_fileHandler)
log.setLevel(log_level)

def set_foreground_logger():
    log.removeHandler(_fileHandler)
    log.addHandler(_streamHandler)

