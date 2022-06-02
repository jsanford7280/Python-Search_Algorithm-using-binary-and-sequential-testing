from search_algorithm import BinaryStringList
import timeit

code2='''
from __main__ import BinaryStringList
ob=BinaryStringList()
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
t3=timeit.timeit("ob.find('Red')",code2,number=1)
print('Binary search,string "Red" found: ',t3)

t4=timeit.timeit("ob.find('basic')",code2,number=1)
print('Binary Search, string "basic" not found:',t4)
