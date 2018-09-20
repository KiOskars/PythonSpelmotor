import  datetime
import inspect

class Log():
    def __init__(self):
        self.__setattr__('name', "Logger")
        self.__setattr__('description', "En logger för att printa ut information i konsolen")
        super(Log, self).__init__()

    @staticmethod
    def out(*args, **kwargs):
        date = "======== " + datetime.datetime.now().__str__() + " ========"
        endLine = "============================================"
        stack = inspect.stack()
        the_class = stack[1][0].f_locals["self"].__class__
        the_method = stack[1][0].f_code.co_name

        print(date)
        print("{}.{}() loggade följande information:".format(str(the_class), the_method))

        for arg in args:
            print(arg)

        for key, value in kwargs.items():
            print("{} : {}".format(key, value))

        print(endLine)