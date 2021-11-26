
class Color(object):
    """Output text to terminal with colors"""
    def __init__(self):
        pass

    @staticmethod
    def end():
        print("\n")

    @staticmethod
    def red(text):
        print(f"\033[31m{text}\033[0m", end=' ')

    @staticmethod
    def green(text):
        print(f"\033[32;1m{text}\033[0m", end=' ')

    @staticmethod
    def yellow(text):
        print(f"\033[33m{text}\033[0m", end=' ')

    @staticmethod
    def blue(text):
        print(f"\033[34m{text}\033[0m", end=' ')

    @staticmethod
    def magenta(text):
        print(f"\033[35m{text}\033[0m", end=' ')

    @staticmethod
    def cyan(text):
        print(f"\033[36m{text}\033[0m", end=' ')
