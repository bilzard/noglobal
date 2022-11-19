import builtins
import types


class NoGlobal:
    def __init__(self, _globals):
        self.globals = _globals

    def __imports(self):
        for name, val in self.globals.items():
            # module imports
            if isinstance(val, types.ModuleType):
                yield name, val

            # functions / callables
            if hasattr(val, "__call__"):
                yield name, val

    def noglobal(self, f):
        return types.FunctionType(
            f.__code__,
            dict(self.__imports()),
            f.__name__,
            f.__defaults__,
            f.__closure__,
        )
