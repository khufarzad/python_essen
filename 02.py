x = 8
y = 5
print('x:', x, ', and y:', y)
print(f'x: {x}, and y: {y}')
r = x - y
print(
f"""
if x is equal to {x} and y is equal to {y},
x - y = {x} - {y} = {r},
x + y = {x} + {y} = {x+y},
x * y = {x} * {y} = {x*y},
x / y = {x} / {y} = {x/y},
x ^ y = {x} ^ {y} = {x**y},
x // y = {x} // {y} = {x//y},
x % y = {x} % {y} = {x%y}
"""
)

print('False:', False, ', type(False)', type(False))
print(f'True: {True} , type(True) {type(True)}')

print(f'x > y: {x} > {y}: {x > y}')
print(f'x < y: {x} < {y}: {x < y}')
print(f'x >= y: {x} >= {y}: {x >= y}')
print(f'x-3 <= y: {x}-3 <= {y}: {x-3 <= y}')
print(f'x == y: {x} == {y}: {x == y}')
print(f'x != y: {x} != {y}: {x != y}')

# False Booleans:
# False
# None
# ''
# 0
# ()
print('===============================')

# if condition:
#    statements


# if False:
#     print('Statement 1')
#     print('Statement 2')
x = 5
y = 5

if x > y:
    print('x is greater that y')
elif x < y:
    print('x is smaller that y')
else:
    print('x is equal to y')

print('===============================')

a = .1
b = .2
if a + b == .3:
    print('If!')
else:
    print('Else!')
    
print('===============================')

if round(a + b, 4) == .3:
    print('If!')
else:
    print('Else!')

print('===============================')

if a + b - 0.3 < 0.0000001:
    print('If!')
else:
    print('Else!')

print('===============================')

name = input('Please Enter Your Name: ')
print('Your Name Is:', name)
age = input('Please Enter Your Age: ')
print(f'Your Age is {age} Years, {age * 12} Months, {age * 12 * 365} Days.')

print('===============================')

fname = 'Hossein'
lname = 'Abazari'

full_name = fname + ' ' + lname


