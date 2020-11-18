from abc import ABC, abstractmethod


class Template(ABC):
    
    def __init__(self):
        pass
    
    @abstractmethod
    def function1(self):
        pass
    
    @abstractmethod
    def function2(self):
        pass
    
    @staticmethod
    def comm_fun():
        print('Run function1 and function2')
        
    def execute(self):
        self.comm_fun()
        self.function1()
        self.function2()


class TemplateImplement1(Template):
    def function1(self):
        print('TemplateImplementation1.function1() called.')
        
    def function2(self):
        print('TemplateImplementation1.function2() called.')        


class TemplateImplement2(Template):
    def function1(self):
        print('TemplateImplementation2.function1() called.')
        
    def function2(self):
        print('TemplateImplementation2.function2() called.')     
        
        

        
# 출처: https://niceman.tistory.com/183        
