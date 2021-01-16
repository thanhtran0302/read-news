import json


class Logger:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def dict_to_string(message) -> str:
        text = message
        if type(message) is dict:
            text = json.dumps(message, indent=3)
        return text

    @staticmethod
    def print_with_end(color, message):
        print(color + message + Logger.ENDC)

    @staticmethod
    def warn(message):
        Logger.print_with_end(
            Logger.WARNING,
            '[WARNING]: ' + Logger.dict_to_string(message)
        )

    @staticmethod
    def info(message):
        Logger.print_with_end(
            Logger.OKBLUE,
            '[INFO]: ' + Logger.dict_to_string(message)
        )

    @staticmethod
    def error(message):
        Logger.print_with_end(
            Logger.FAIL,
            '[ERROR]: ' + Logger.dict_to_string(message)
        )

    @staticmethod
    def success(message):
        Logger.print_with_end(
            Logger.OKGREEN,
            '[SUCCESS]: ' + Logger.dict_to_string(message)
        )

    @staticmethod
    def important(message):
        Logger.print_with_end(
            Logger.BOLD,
            '[IMPORTANT]: ' + Logger.dict_to_string(message)
        )

    @staticmethod
    def underline(message):
        Logger.print_with_end(
            Logger.UNDERLINE,
            '[UNDERLINE]: ' + Logger.dict_to_string(message)
        )
