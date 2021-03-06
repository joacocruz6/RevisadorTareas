"""
First some imports of useful libraries
"""
import os
import sys
from abc import *
from pathlib import Path
"""
We configure the pathing to resolve some of the imports
"""
my_path = Path('.').resolve().parent.parent #The project directory
src_path = Path('.').resolve().parent #The src directory
sys.path.append(str(my_path))
sys.path.append(str(src_path))
from options import TestCase, TestOptions

"""
AbstractTester class defines the base code for each of the tester of the different
languages.
It's the base for all other tester, to create a tester for another language, simply create
a subclass of this one.
:author: Joaquín Cruz
"""
class AbstractTester(ABC):
     """
     __init__: Constructor of the class, receive a list of test input, it's matching
     results of output and the name of the file to be tested. Creates an internal list
     of subprocess within it

     :self: Reference to the instance of the object
     :test_input: the input for the tests to be executed
     :test_output: list of correct outputs of the tests
     :homework: the name of the file to be executed
     :return: An instance of the class.
     """
     def __init__(self,test_options: TestOptions,homework: str):
          self._options = test_options
          self._homework = homework
          self._process = []
          self._cwd = os.getcwd()
     """
     setCwd: Setter method for the directory of the homework
     :self: The instance of the object
     :cwd: The string of the absolut path of the homework directory
     """
     def setCwd(self,cwd: str):
          self._cwd = cwd
     def setOptions(self,new_options: TestOptions):
          self._test_options = new_options
     def getOptions(self):
          return self._options
     """
     getHomework: Getter method of the homework propertie of the object
     :self: The instance of the object
     :return: The name of the file to be tested
     """
     def getHomework(self):
          return self._homework
     """
     getProcess: Getter method for the list of process

     :self: The instance of the object
     :return: The list of process done with the file
     """
     def getProcess(self):
          return self._process
     """
     compileFile: Abstract method for the class, compile the file to be 
     executed afterwards. Override it for tester of compiled languages
     (or transpiled ones).

     :self: The instance of the object

     """
     @abstractmethod
     def compileFile(self):
          pass
     """
     run: Abstract method to run the file of the tests. Override it 
     for creating a tester for other languages

     :self: The instance of the object
     """
     @abstractmethod
     def run(self):
          pass
     """
     mark: Method wich compare the output of the process with the real ones
     
     :self: The instance of the object
     """
     def mark(self):
          print("-------------------------------------")
          for i in range(len(self._process)):
               isCorrect = self._process[i].stdout[:-1] == self.getOptions()[i].getTestOutput()
               if isCorrect:
                    print("Correct test number {}! Answer: {}".format(i+1,self._process[i].stdout[:-1]))
                    print("-------------------------------------")
               else:
                    print("Failed test number {}".format(i+1))
                    print("Expected value: {}".format(self.getOptions()[i].getTestOutput()))
                    print("Homework returned: {}".format(self._process[i].stdout[:-1]))
                    print("-------------------------------------")