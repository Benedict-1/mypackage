def sum_array(array):

    '''Return sum of all items in array'''
    import numpy as np
    if len(array)==1:
        return array[0]
    else:
        return array[0] + sum_array(np.delete(array,[0]))

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):

    '''Return n!'''
    if n==1:
        return n
    else:
        return n*factorial(n-1)

def reverse(word):

    '''Return word in reverse'''
    s=list(word)
    if len(s)==1:
        return s[0]
    else:
        return s.pop(-1)+reverse(s)
