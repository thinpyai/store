import json
import logging
import traceback


class FormatterJSON(logging.Formatter):
    """
    Formatter to output message in json format.

    Args:
        logging (str): Log output string in json format.
    """

    def format(self, record):
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)
        data = {
            'logLevel': record.levelname,
            'timestamp': '%(asctime)s.%(msecs)dZ' % dict(asctime=record.asctime, msecs=record.msecs),
            'message': record.getMessage(),
            'module': record.module,
            'filename': record.filename,
            'funcname': record.funcName,
            'levelno': record.levelno,
            'lineno': record.lineno,
            'traceback': {}
        }
        if record.exc_info:
            exception_data = traceback.format_exc().splitlines()
            data['traceback'] = exception_data

        return json.dumps(data, ensure_ascii=False)
