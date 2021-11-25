class FuncDetail(object):
    """Class represents each part of a single line of documentation"""
    def __init__(self,):
        self._return_type = None
        self._fn_name = None
        self._description = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def return_type(self):
        return self._return_type

    @return_type.setter
    def return_type(self, return_type):
        self._return_type = return_type

    @property
    def fn_name(self):
        return self._fn_name

    @fn_name.setter
    def fn_name(self, fn_name):
        self._fn_name = fn_name
