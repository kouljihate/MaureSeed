import os
import sys
import logging
import traceback
from datetime import datetime

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "log")
os.makedirs(LOG_DIR, exist_ok=True)

class AppLogger:
    def __init__(self, name="maureseed"):
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)
            fmt = logging.Formatter(
                "[%(asctime)s] %(levelname)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
            fh = logging.FileHandler(os.path.join(LOG_DIR, f"{name}.log"), encoding="utf-8")
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(fmt)
            self.logger.addHandler(fh)

            sh = logging.StreamHandler(sys.stdout)
            sh.setLevel(logging.INFO)
            sh.setFormatter(fmt)
            self.logger.addHandler(sh)

    def error_with_context(self, e: Exception):
        """Return structured error info from an exception."""
        tb = traceback.extract_tb(e.__traceback__)
        if tb:
            last = tb[-1]
            return {
                "script": last.filename,
                "function": last.name,
                "line": last.lineno,
                "code": last.line,
                "description": str(e),
                "timestamp": datetime.utcnow().isoformat(),
            }
        return {
            "script": "unknown",
            "function": "unknown",
            "line": 0,
            "code": "",
            "description": str(e),
            "timestamp": datetime.utcnow().isoformat(),
        }

    def log_error(self, e: Exception, context: str = ""):
        """Log an exception with full context."""
        info = self.error_with_context(e)
        msg = (
            f"{context} | "
            f"Script: {info['script']} | "
            f"Function: {info['function']} | "
            f"Line: {info['line']} | "
            f"Code: {info['code']} | "
            f"Error: {info['description']}"
        )
        self.logger.error(msg)
        return info

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)


app_logger = AppLogger()
