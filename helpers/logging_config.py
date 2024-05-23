import logging
import json_log_formatter

formatter = json_log_formatter.JSONFormatter()

json_file_handler = logging.FileHandler('paloozabot.log')
json_file_handler.setFormatter(formatter)

json_stream_handler = logging.StreamHandler()
json_stream_handler.setFormatter(formatter)

logging.basicConfig(level=logging.DEBUG,
                    handlers=[json_file_handler, json_stream_handler])

logger = logging.getLogger('discord')

def log_event(level, message, **kwargs):
    log_data = {
        'message': message,
        **kwargs
    }
    level = level.upper()
    if level == 'INFO':
        logger.info(log_data)
    elif level == 'ERROR':
        logger.error(log_data)
    elif level == 'DEBUG':
        logger.debug(log_data)
    elif level == 'WARNING':
        logger.warning(log_data)
    else:
        logger.log(level, log_data)  # fallback for other log levels