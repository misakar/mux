"""
    mux
    ```

    an elegant handler for python terminal logging
"""
import os
import time
import logging
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter


class muxStreamHandler(logging.StreamHandler):
    def format(self, record):
        if self.formatter:
            formatter = self.formatter
        else:
            formatter = MuxFormatter()
        return formatter.format(record)


class MuxFormatter(logging.Formatter):
    """
    class MuxFormatter:
        formatter class for mux:)
        let the magic begin!
    """
    magic_colors = {
        'DEBUG': '\033[34m\033[1m',
        'INFO': '\033[92m\033[1m',
        'WARNING': '\033[93m\033[1m',
        'ERROR': '\033[31m\033[1m',
        'CRITICAL': '\033[31m\033[1m',
        'TIME': '\033[35m\033[4m'
    }
    default_time_format = "%H:%M:%S"
    default_message_format = magic_colors.get('TIME')+\
        '%(asctime)s\033[0m'+' {levelname_fmt}'+' :: '+'%(message)s'
    exc_temp_file = './__exc_info__.txt'

    def format(self, record):
        level = record.levelno
        if level >= logging.ERROR:
            self._fmt = self.default_message_format.format(
                levelname_fmt=self.magic_colors.get('ERROR')+'%(levelname)-9s'+'\033[0m')
        elif level >= logging.WARNING:
            self._fmt = self.default_message_format.format(
                levelname_fmt=self.magic_colors.get('WARNING')+'%(levelname)-9s'+'\033[0m')
        elif level >= logging.INFO:
            self._fmt = self.default_message_format.format(
                levelname_fmt=self.magic_colors.get('INFO')+'%(levelname)-9s'+'\033[0m')
        elif level >= logging.DEBUG:
            self._fmt = self.default_message_format.format(
                levelname_fmt=self.magic_colors.get('DEBUG')+'%(levelname)-9s'+'\033[0m')

        return super(MuxFormatter, self).format(record)

    def formatException(self, exc_info):
        result = None
        _result = []
        code = super(MuxFormatter, self).formatException(exc_info)
        if code:
            highlight_code = highlight(code, PythonLexer(), TerminalFormatter())
            for line in highlight_code.split('\n'):
                _result.append('  '+line)
            result = '\n'+'\n'.join(_result)
        return result

    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created) # current time tuple
        if datefmt:
            s = time.strftime(datefmt, ct)
        else:
            s = time.strftime(self.default_time_format, ct)
        return s