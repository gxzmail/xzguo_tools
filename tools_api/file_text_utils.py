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
    def function(self, token, param1, param2,..
                    param3,....
                    ....
                    paramN):
    to 
    param1: "param1"
    param2: "param2"
    ...
    paramN: "paramN"
    '''
    def format_wayang_type(self):
        with open(self.file_name, self.file_mode, encoding = \
                self.file_encode) as texter:
            list = texter.readlines()
        for line in list:
            if 'def' in line:
                self._format_request_body(list)
                break
            elif ':' in line:
                self._format_request_content(list)
                break


    def _format_request_body(self, list):
        function_prototype = ''.join(list)
        function_prototype = function_prototype.replace('\n', '')
        function_prototype = function_prototype.replace(' ', '')
        if ')' in function_prototype:
            param_one_line = function_prototype.split('(')[1].split(')')[0]
        else:
            param_one_line = function_prototype.split('(')[1]
        param_list = param_one_line.split(',')
        if param_list[0] == 'self':
            param_list = param_list[1:]
        if param_list[0] == 'token':
            param_list = param_list[1:]
        for param in param_list[:-1]:
            print("'%s': %s," % (param, param))
        print("'%s': %s" % (param_list[-1], param_list[-1]))
        return

    def _format_request_content(list):
        pass

def debug():
    util = FileTextUtils(file_path + r"\a.txt", "r")
    util.format_wayang_type()
    return


if __name__ ==  '__main__':
    debug()