from shutil import copyfile
import os
import fileinput


class VarDispatcher:
    __variables = {}

    def set(self, var, val):
        self.__variables[var] = val
        return self

    def append(self, var, val):
        val = "%s%s" % (self.get(var), val)
        return self.set(var, val)

    def get(self, var):
        if var not in self.__variables:
            raise Exception("Undefined variable <%s>" % var)
        return self.__variables[var]

    def exec_str(self, s):
        for k, v in self.__variables.items():
            s = s.replace('%'+str(k)+'%', str(v))
        return s

    def exec(self, files):
        for filename in files:
            with fileinput.FileInput(filename, inplace=True) as file:
                for line in file:
                    print(self.exec_str(line), end='')


class FileDispatcher:
    __files = []
    __var_dispatcher = object()

    def __init__(self, vd):
        self.__var_dispatcher = vd

    def add(self, fn):
        if type(fn) is str:
            self.__files.append(fn)
            return

        if type(fn) is list:
            self.__files += fn
            return

        raise Exception("Only str and list are supported")

    def cp(self, dist):
        for fn in self.__files:
            fn = os.path.normpath(fn)
            path = fn.split(os.sep)
            relpath = ''
            for elm in path[::-1]:
                if elm != 'root':
                    relpath = os.path.join(elm, relpath)
                if elm == 'root':
                    break
            dest = os.path.normpath(os.path.join(dist, relpath))
            os.makedirs(os.path.split(dest)[0], exist_ok=True)
            copyfile(fn, self.__var_dispatcher.exec_str(dest))
            # print("%s -> %s" % (path, os.path.normpath(os.path.join(dist, relpath))))


class StrFormat:
    @staticmethod
    def camel_case(s):
        words = [word.capitalize() for word in s.split('_')]
        return "".join(words)
