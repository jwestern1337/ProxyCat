import sys, datetime

LOG_LEVELS = {
    'info': {
        'color': '\033[36m',
        'style': '\033[1m'
    },
    'warning': {
        'color': '\033[33m',
        'style': '\033[1m'
    },
    'error': {
        'color': '\033[31m',
        'style': '\033[1m'
    },
    'critical': {
        'color': '\033[31m',
        'style': '\033[7m'
    },
    'debug': {
        'color': '\033[35m',
        'style': '\033[1m'
    },
    'success': {
        'color': '\033[32m',
        'style': '\033[1m'
    }
}

def log(message: str, level: str = 'info', end: str = '\n') -> None:
    """
    Logs a message to the terminal.

    Params:
        message (str): The message to log.
        level (str): The level of the message. Defaults to 'info'.
    """

    if level not in LOG_LEVELS:
        raise ValueError('Invalid log level.')

    now = datetime.datetime.now().strftime('%H:%M:%S')
    level_color = LOG_LEVELS[level]['color']
    level_style = LOG_LEVELS[level]['style']
    message = ' ' * int(8 - len(level)) + message
    sys.stdout.write(f'  {now} {level_color}{level_style}{level.upper()}\033[0m {message}{end}')
    sys.stdout.flush()