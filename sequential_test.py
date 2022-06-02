from search_algorithm import SequentialStringList
import timeit

code='''
from __main__ import SequentialStringList
ob=SequentialStringList()
ob.add('Hi')
ob.add('Hello')
ob.add('World')
ob.add('How')
ob.add('Are')
ob.add('You')
ob.add('Wow')
ob.add('Zoo')
ob.add('Word')
ob.add('Tell')
ob.add('Speak')
ob.add('We')
ob.add('Can')
ob.add('Go')
ob.add('Home')
ob.add('We')
ob.add('Us')
ob.add('Basic')
ob.add('Smalltalk')
ob.add('Red')
'''

# finding the execution time for searching the list
t=timeit.timeit("ob.find('Go')",code,number=1)
print('Sequential Search, String "Go" found: ',t)

t2=timeit.timeit("ob.find('Simulate')",code,number=1)
print('Sequential Search, String "Simulate" not found: ',t2)
