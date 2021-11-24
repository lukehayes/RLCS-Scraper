class FuncDetail(object):
    """Class represents each part of a single line of documentation"""
    def __init__(self, return_type, fn_name, description):
        self.return_type = return_type
        self.fn_name = fn_name
        self.description = description


