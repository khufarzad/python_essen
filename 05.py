x = 4
while x > 0:
    print('x:', x)
    x = x - 1

print('End of Loop!')
print('==============================')

l1 = [4, 6, 7, 1]

for i in l1:
    print('i:', i)
    
print('++++++')

index = 0
while index < len(l1):
    print('l1[index]:', l1[index])
    index = index + 1
print('==============================')

sentence = 'Python is the best programming language'
# output: Ythonpay Siay Hetay Estbay Rogrammingpay Anguagelay.

words = sentence.split()
# words = ['Python', 'is', 'the', 'best', 'programming', 'language']

new_words = []
id_ = 0
while id_ < len(words):
    # word = '' + words[id_][1:] + words[id_][0] + 'ay'
    word = ''
    word = word + words[id_][1:]
    word = word + words[id_][0]
    word = word + 'ay'
    new_words.append(word.capitalize())
    id_ = id_ + 1

new_sentence = ' '.join(new_words)
print('new_sentence:', new_sentence)

print('==============================')

fibo = [1, 1] # Fibonacci
n = 7
niter = 0
while niter < n - 2:
    fibo.append(fibo[-1]+fibo[-2])
    niter += 1  # niter = niter + 1
print('Fibonacci:', fibo)

# x *= 3 --> x = x * 3

print('==============================')

import math
from math import factorial

x = 4.11616
y = math.floor(x)
print('y:', y)
n = factorial(4)
print('n:', n)

from random import uniform
r = uniform(1.5, 8.5)
print('r:', r)

from hashlib import *
h = sha256('Farzad'.encode('utf-8')).hexdigest()
print('h:', h)

print('==============================')


















