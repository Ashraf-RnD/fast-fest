import logging


class Logger:
    log = None

    def __init__(self,
                 LOG_FORMAT='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                 LOG_NAME='',
                 LOG_FILE_INFO='../fast-fest/logs/fast-fest.log',
                 LOG_FILE_ERROR='../fast-fest/logs/fast-fest-ERROR.log'):
        Logger.log = logging.getLogger(LOG_NAME)
        log_formatter = logging.Formatter(LOG_FORMAT)

        # comment this to suppress console output
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(log_formatter)
        Logger.log.addHandler(stream_handler)

        file_handler_info = logging.FileHandler(LOG_FILE_INFO, mode='w')
        file_handler_info.setFormatter(log_formatter)
        file_handler_info.setLevel(logging.INFO)
        Logger.log.addHandler(file_handler_info)

        file_handler_error = logging.FileHandler(LOG_FILE_ERROR, mode='w')
        file_handler_error.setFormatter(log_formatter)
        file_handler_error.setLevel(logging.ERROR)
        Logger.log.addHandler(file_handler_error)

        Logger.log.setLevel(logging.INFO)

    @staticmethod
    def get_log():
        if Logger.log is None:
            Logger()
        return Logger.log
