# Types:
#   int
#   str
#   float
#   bool

# Functions:
#   print()
#   input()
#   type()
#   round()
#   int()
#   str()
#   float()
#   bool()

# If Conditions:
# if condition:
#   statements
# elif condition:
#   statements
# elif condition:
#   statements
# else:
#   statements

# Built-in Collections in Python:
# 1. list
# 2. tuple
# 3.
# 4.


# list()
# l1 = list()
l1 = []
print('l1:', l1)
print('type(l1):', type(l1))


l2 = [
      1, # index = 0
      1.3, # index = 1
      True, # index = 2
      [3, 3.14], # index = 3
      'Farzad', # index = 4
     ]

print('l2:', l2)
print('type(l2):', type(l2))


# indexing in lists

print('l2[1]:', l2[1])
print('l2[4]:', l2[4])
# print('l2[8]:', l2[8]) --> Error
print('l2[3]:', l2[3])
print('l2[3]:', l2[3][1])

print('==============================')

l3 = [8, 1, 5, 7, 1, 9, 2, 3, 1, 8, 6, 4, 5]
print('l3:', l3)
print('l3[8]:', l3[8])
# Negative Indexing
print('l3[-1]:', l3[-1])
print('l3[-8]:', l3[-8])

print('==============================')

# Slicing
print('l3[2:6]:', l3[2:6])
print('l3[5:10]:', l3[5:10])
print('l3[-8:-2]:', l3[-8:-2])
print('l3[-8:8]:', l3[-8:8])
print('l3[:5]:', l3[:5])
print('l3[8:]:', l3[8:])
print('l3[:]:', l3[:])

print('==============================')

# Steps
print('l3[::2]:', l3[::2])
print('l3[-8:8:2]:', l3[-8:8:2])
print('l3[::-1]:', l3[::-1])

print('==============================')

# List Methods
l4 = [3, 3.14, True, 'Python']
x = l4[1]
print('x = l4[1]:', x)
length = len(l4)
print('length = len(l4):', length)
l4.append(False)
print('l4 after append:', l4)
l3.sort()
print('l3 after sort:', l3)
l4.insert(2, 'Madari')
print('l4 after insert:', l4)
y = l4.pop()
print('l4 after pop:', l4)
print('y = l4.pop():', y)
l4.remove('Madari')
print('l4 after remove:', l4)
l4.clear()
print('l4 after clear:', l4)
del l4
# print('l4 after del:', l4) --> Error
l3[0] = 23
print('l3 after change:', l3)
l3[1:4] = [16, 16, 16]
print('l3 after change:', l3)

print('==============================')

# Check if Element Exists
l5 = [2, 6, 4]
if 7 in l5:
    print('7 Does Exist in list l5.')
else:
    print('7 Does NOT Exist in list l5.')

l6 = [4, 8, 9]
l7 = l5 + l6
print('l7:', l7)
print('==============================')

# strings
s1 = 'Python'
s2 = 'Programming'
s3 = 'Language'
s4 = s1 + ' ' + s2 + ' ' + s3
print('s4:', s4)

s5 = ' Python'
print('len(s1):', len(s1))
print('len(s5):', len(s5))
print('s1[0]:', s1[0])
print('s1 * 2:', s1 * 2) # s1 + s1

print('==============================')

if 'th' in 'Python':
    print('th Does Exist in string Python.')
else:
    print('th Does NOT Exist in string Python.')

print('==============================')

s6 = 'Python'
s6 = s6.replace('P', 'J')
print('s6:', s6)

name = 'Sahar'
s7 = f'My Name is {name}' # formatting
print('s7:', s7)

print('==============================')

s8 = 'python and JAVASCRIPT are the BEST'
print('s8.upper():', s8.upper())
print('s8.lower():', s8.lower())
print('s8.capitalize():', s8.capitalize())
print('s8.title():', s8.title())
print('s8.isupper():', s8.isupper())
print('s8.islower():', s8.islower())
print('s8.endswith():', s8.endswith('T'))

s9 = 'Jamshid.pSD'
if s9.upper().endswith('.PSD'):
    print('The File Format is OK.')
else:
    print('Wrong File Type.')

print('==============================')

# \

print('farzad\'s')
print("farzad\"s")
print("farzad\ts")
print("farzad\ns")
print("farzad\\s")

print('==============================')

# tuple()
t1 = tuple()
print('t1:', t1)
print('type(t1):', type(t1))

t2 = (5, 8.5, True, 'Python', [2, 3], (7, 9))
print('t2:', t2)
print('t2[-2]:', t2[-2])
print('t2[2:-2]:', t2[2:-2])
z = (5, 8.5, True, 'Python', [2, 3], (7, 9))[0]
print('z = [0]:', z)
print('len(t2):', len(t2))

print('==============================')


t3 = 4, 6, 8
print('t3:', t3)
print('type(t3):', type(t3))

a, b = 1, 2
print('a:', a)
print('b:', b)

print('==============================')

# Unpack

f, *g, c = (1, 3, 4, 6, 9)
print('f:', f)
print('g:', g)
print('c:', c)

print('==============================')

t4 = (1, 5, 6)
t5 = (7, 5, 3)
t6 = t4 + t5
t6 = list(t6)
t6.append(9)
t6 = tuple(t6)
print('t6:', t6)

print('==============================')




