class SimpleAdder(object):
   def __init__(self, elements=[]):
       self._list = elements

   def __add__(self, other):
       return self._list + other._list

   def __str__(self):
       return str(self._list)
       
a = SimpleAdder(elements=[1,2,3,4])
b = SimpleAdder(elements=[2, 3, 4])
print(a + b)    
 