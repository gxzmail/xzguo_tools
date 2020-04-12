from os import  path
import  re

file_path = path.dirname(path.abspath(__file__))
class FileTextUtils(object):
    list = []

    def __init__(self, file_name, file_mode, file_encode="utf-8"):
        self.file_name = file_name
        self.file_mode = file_mode
        self.file_encode = file_encode
    '''
    transfer 
    def function(self, param1, param2,..
                    param3,....
                    ....
                    paramN):
    to 
    param1: "param1"
    param2: "param2"
    ...
    paramN: "paramN"
    '''
    def wangyang(self):
        with open(self.file_name, self.file_mode, encoding = \
                self.file_encode) as texter:
            list = texter.readlines()
        for line_context in list:
            function_prototype = str.join(line_context)
        param_one_line = function_prototype.split('(')[1].split(')')[0]
        self.oneline_2_multilines(param_one_line, ',')
        #     print("the line is :%s" %line_context)
        return

    def oneline_2_multilines(self, oneLine, splitor):







def debug():
    # print("-----%s\n%s\n" %(path.abspath(__file__),
    #                      path.dirname( path.abspath(__file__))))
    util = FileTextUtils(file_path + r"\a.txt", "r")
    util.wangyang()
    return


if __name__ ==  '__main__':
    debug()