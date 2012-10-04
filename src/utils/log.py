from config import log_level, log_format, log_datefmt, log_filename
import logging

logging.basicConfig(
        format=log_format,
        datefmt=log_datefmt,
        filename=log_filename)
log = logging.getLogger(__name__)
log.setLevel(log_level)

