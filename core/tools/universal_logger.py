import os
import logging
from datetime import datetime


class UniversalLogger:
    def __init__(self, log_dir: str):
        self.log_dir = "logs/" + log_dir
        self._current_day_dir = None
        self._create_log_dir()
        self.loggers = {}

    def _create_log_dir(self):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def _create_day_dir(self):
        # Создаём директорию для текущего дня
        day_dir = os.path.join(self.log_dir, datetime.now().strftime("%Y-%m-%d"))
        if not os.path.exists(day_dir):
            os.makedirs(day_dir)
        return day_dir

    def _switch_day_directory(self):
        # Проверяем, нужно ли обновить текущий день
        today = datetime.now().strftime("%Y-%m-%d")
        if today != self._current_day_dir:
            self._current_day_dir = self._create_day_dir()
            self._setup_loggers()  # Обновляем все логгеры при смене дня

    def _setup_logger(self, logger_name, log_level=logging.DEBUG):
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)

        # Удаляем существующие хэндлеры, чтобы избежать дублирования
        if logger.hasHandlers():
            logger.handlers.clear()

        # Добавляем новый хэндлер для нового дня
        handler = logging.FileHandler(
            os.path.join(self._current_day_dir, f"{logger_name}.log")
        )
        handler.setLevel(log_level)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        self.loggers[logger_name] = logger

    def _setup_loggers(self):
        # Перенастраиваем все логгеры на новый день
        for logger_name in self.loggers:
            self._setup_logger(logger_name)

    def get_logger(self, logger_name):
        # Проверяем, нужно ли переключить директорию для нового дня
        self._switch_day_directory()
        if logger_name not in self.loggers:
            self._setup_logger(logger_name)
        return self.loggers[logger_name]

    def info(self, msg, *args, **kwargs):
        logger_name = kwargs.pop("extra", None)
        if not logger_name:
            raise ValueError("Logger name must be provided as 'extra'")
        logger = self.get_logger(logger_name + "_info")
        logger.info(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        logger_name = kwargs.pop("extra", None)
        if not logger_name:
            raise ValueError("Logger name must be provided as 'extra'")
        logger = self.get_logger(logger_name + "_error")
        logger.error(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        logger_name = kwargs.pop("extra", None)
        if not logger_name:
            raise ValueError("Logger name must be provided as 'extra'")
        logger = self.get_logger(logger_name + "_warning")
        logger.warning(msg, *args, **kwargs)
