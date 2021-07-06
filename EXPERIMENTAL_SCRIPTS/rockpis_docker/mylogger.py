import logging
import colorlog


def init_logger() -> logging.Logger:

    formatter = colorlog.ColoredFormatter(
        "%(asctime_log_color)s%(asctime)s - %(log_color)s%(bold)s%(levelname)-8s%(reset)s %(white)s%(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red,bg_white', 
        },
        secondary_log_colors={
            'asctime': {
                'DEBUG':    'green',  
                'INFO':     'green',  
                'WARNING':  'green',  
                'ERROR':    'green',  
                'CRITICAL': 'green'      
            }
        },
        style='%'
    )

    handler = colorlog.StreamHandler()
    handler.setFormatter(formatter)

    logger = colorlog.getLogger('example')
    logger.addHandler(handler)

    logger.setLevel(logging.DEBUG)

    return logger
