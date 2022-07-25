class Entrypoint:
    """Base class for the decorators that provide the inversion control"""

    class __impl:
        """ Implementation of the singleton interface """
        def __init__(self, function=None):
            self._function = function

    # storage for the instances references
    __instance = None

    @classmethod
    def create_instance(cls, function):
        if cls.__instance is None:
            if function is None:
                raise Exception("No function passed on first execution.")

            cls.__instance = Entrypoint.__impl(function)

    def __init__(self, function=None, *args, **kwargs):
        """ Create singleton instance """
        self.create_instance(function)

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)
