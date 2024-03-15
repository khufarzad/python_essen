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



