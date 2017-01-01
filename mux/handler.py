"""
    mux
    ```

    an elegant handler for python terminal logging
"""
import logging
import chalk
import time

class muxStreamHandler(logging.StreamHandler):

    def format(self, record):
        if self.formatter:
            formatter = self.formatter
        else:
            formatter = muxFormatter()
        return formatter.format(record)


class muxFormatter(logging.Formatter):

    default_time_format = "%H:%M:%S"

    def format(self, record):
        level = record.levelno
        if level >= logging.ERROR:
            self._fmt = chalk.format_magenta('%(asctime)s', opts=('underscore')) + \
                        chalk.format_red(' %(levelname)-9s', opts=('bold')) + \
                        ' :: ' + '%(message)s'
        elif level >= logging.WARNING:
            self._fmt = chalk.format_magenta('%(asctime)s', opts=('underscore')) + \
                        chalk.format_yellow(' %(levelname)-9s', opts=('bold')) + \
                        ' :: ' + '%(message)s'
        elif level >= logging.INFO:
            self._fmt = chalk.format_magenta('%(asctime)s', opts=('underscore')) + \
                        chalk.format_green(' %(levelname)-9s', opts=('bold')) + \
                        ' :: ' + '%(message)s'
        elif level >= logging.DEBUG:
            self._fmt = chalk.format_magenta('%(asctime)s', opts=('underscore')) + \
                        chalk.format_blue(' %(levelname)-9s', opts=('bold')) + \
                        ' :: ' + '%(message)s'

        return super(muxFormatter, self).format(record)

    def formatException(self, ei):
        return super(muxFormatter, self).formatException(ei)

    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created) # current time tuple
        if datefmt:
            s = time.strftime(datefmt, ct)
        else:
            s = time.strftime(self.default_time_format, ct)
        return s
