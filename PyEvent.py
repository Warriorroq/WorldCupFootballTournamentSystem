class Event:
    __functions = []

    def invoke(self, *args):
        for i in self.__functions:
            i(args)

    def add(self, func):
        self.__functions.append(func)

    def remove(self, func):
        self.__functions.remove(func)