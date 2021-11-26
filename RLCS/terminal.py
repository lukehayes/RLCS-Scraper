class Terminal(object):
    """Output helpers for the terminal"""
    def __init__(self):
        pass

    @staticmethod
    def vert_line():
        print("\t |")

    @staticmethod
    def arrow():
        print("\n \t ↳", end=' ')
