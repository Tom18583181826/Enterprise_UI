import sys
from logging import FileHandler
from logging import Formatter
from logging import Logger
from logging import StreamHandler


class GetLog:
    def get_log(self, log_path):
        log_obj = Logger("test.log")
        logformat = Formatter("[%(asctime)s]:%(message)s")
        filepath = FileHandler(log_path)
        filepath.setFormatter(logformat)
        log_obj.addHandler(filepath)

        console = StreamHandler(sys.stdout)
        console.setFormatter(logformat)
        log_obj.addHandler(console)

        return log_obj
