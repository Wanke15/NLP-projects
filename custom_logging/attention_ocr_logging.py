import os
import logging

from utils.common import get_base_dir


class AttentionOCRLogging:
    def __init__(self, logger_name=__name__, logger_level=logging.INFO):
        # Create a logger
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logger_level)

        self.log_path = os.path.join(get_base_dir(), "conf/attention_ocr.log")
        
        # Create a handler to write log into file
        fh = logging.FileHandler(self.log_path, 'a', encoding='utf-8')
        fh.setLevel(logger_level)
        
        # Create a handler to write log into cmd
        ch = logging.StreamHandler()
        ch.setLevel(logger_level)

        # define log format
        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add hadlers to logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        fh.close()
        ch.close()

    def getLogger(self):
        return self.logger


if __name__ == '__main__':
    t_l = AttentionOCRLogging().getLogger()

    def test_logger():
        t_l.info("info test")
        t_l.warning("warning test")
        t_l.error("error test")

    test_logger()

# [2019-11-19 15:51:38,979] attention_ocr_logging.py->test_logger line:42 [INFO]info test
# [2019-11-19 15:51:38,980] attention_ocr_logging.py->test_logger line:43 [WARNING]warning test
# [2019-11-19 15:51:38,980] attention_ocr_logging.py->test_logger line:44 [ERROR]error test
