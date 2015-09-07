__author__ = "Willy Nguessan"

""" Part-1 Functions and Exceptions  """

class ListDivideException(Exception):
        pass
def listDivide(number,divide=2):
        response=0

        try:
                for num in number:#iterate through the list
                        if num % divide==0:
                                response = response+1
        except:
                raise ListDivideException()
        print response
        return response
def testListDivide():

        try:
                listDivide([1,2,3,4,5])
                listDivide([2,4,6,8,10])
                listDivide([30, 54, 63,98, 100], divide=10)
                listDivide([])
                listDivide([1,2,3,4,5], 2)
        except TypeError:
                raise ListDivideException()
testListDivide()