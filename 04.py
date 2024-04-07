st = 'Sedigheh'
print('st.endswith():', st.endswith('fa'))

file = 'Sedigheh.PDF'
if file.lower().endswith('.pdf'):
    print('File Is PDF')
else:
    print('Wrong File Format')

print('=======================================')

# Collections
# 1. list --> []
# 2. tuple --> ()
# 3. set --> {}
# 4. dictionary --> {}

# *. string --> '' ""

print('=======================================')

s1 = set()
print('s1:', s1)
print('type(s1):', type(s1))
s2 = {5, 6, 5, 1, 3, 1, 4, 4, 4, 5}
print('s2:', s2)
s3 = {1, 2, 3}
s4 = {3, 4, 5}
print('s3 - s4:', s3 - s4)
print('s3 | s4:', s3 | s4)
print('s3 & s4:', s3 & s4)
print('s3 ^ s4:', s3 ^ s4)
s3.add(7)
s3.add(5)
s3.add(5)
print('s3 after add:', s3)
s3.remove(5)
print('s3 after remove:', s3)

print('=======================================')

d1 = dict()
print('d1:', d1)
print('type(d1):', type(d1))

d2 = {
    "Hello": "Salam",
    "Pickles": "Khiyarshoor",
    "Voice": "Seda"
    }

print('d2:', d2)
v1 = d2["Hello"]
print('v1 = d2["Hello"]:', v1)

person = {
    'First_Name': 'Farzad',
    'Last_Name': 'Asgari',
    'Height': 184, # Cm
    'Weight': 77, # Kg
    'Skills': ['Python', 'PHP', 'Matlab'],
    'Languages': ('Persian', 'Chinese'),
    }

print('person:', person)
skills = person['Skills']
print('skills:', skills)
print('type(skills):', type(skills))

person['Height'] = 185 # Cm
print('person:', person)
person['Birthday'] = '1375/06/15'
print('person:', person)
get_data = person.get('First_Name', 'Undefined')
print('get_data:', get_data)

print('=======================================')

# Nested Dictionary
customer_data = {
    "1001": {
        "name": "Sara Saeidi",
        "email": "Sara_Saeidi@gmail.com",
        "phone": "91421841364",
        "purchase": [
            {"product_id": "A123", "price": 10.0, 'quantity': 2},
            {"product_id": "B456", "price": 5.5, 'quantity': 1}
            ]
        }
    }
cust1001 = customer_data['1001']
print('cust1001.get("name"):', cust1001.get("name"))
print('cust1001.get("purchase"):', cust1001.get("purchase"))

customer_data.update({
    "1002": {
        "name": "Hiva Yarandi",
        "email": "Hiva_Yarandi@gmail.com",
        "phone": "65413156165",
        "purchase": []
        },
    "1003": {
        "name": "Mahsa Hormozani",
        "email": "Mahsa_Hormozani@yahoo.com",
        "phone": "54487415189",
        "purchase": []
        }
    })
print('customer_data:', customer_data)
customer_data.clear()
print('customer_data:', customer_data)
del customer_data

print('=======================================')

ks = person.keys()
print('ks:', ks)
print('type(ks):', type(ks))
vs = person.values()
print('vs:', vs)
print('type(vs):', type(vs))
it = person.items()
print('it:', it)
print('type(it):', type(it))

print('=======================================')

height = person.pop('Height')
print('height:', height)
print('person after pop:', person)

print('=======================================')

st1 = "Shahid Beheshti University Python Course"
ls1 = st1.split() # st1.split(' ')
print('ls1:', ls1)
st2 = ' '.join(ls1)
print('st2:', st2)

st3 = '+++Hiva++++++'
print('st3:', st3)
print('len(st3):', len(st3))
st4 = st3.strip('+')
print('st4:', st4)
print('len(st4):', len(st4))
st5 = '   Mahsa   '
st6 = st5.strip() # st5.strip(' ')
print('st5:', st5)
print('len(st5):', len(st5))
print('st6:', st6)
print('len(st6):', len(st6))

print('=======================================')

x = 3
for i in range(4):
    x = x * 2
print('x:', x)
print('After For Loop!')

print('=======================================')

ls2 = [7, 8, 1, 2]
y = 0
for i in ls2:
    y = y + i
j = ls2[-1]
print('sum(ls2):', sum(ls2))
print('i:', i)
print('y:', y)

print('=======================================')

for char in 'Sara Saeidi':
    print('char:', char)
    
print('=======================================')

ls3 = list(range(1, 10, 2)) # [1, 3, 5, 7, 9]
ls4 = []
for i in ls3:
    ls4.append(i**2)
print('ls4:', ls4)

print('=======================================')

member = 1
for k in person:
    print(f'member #{member} key:{k} --> value:{person[k]}')
    member += 1

print('=======================================')

fibo = [1, 1] # Fibonacci
# n = int(input('How Many of Fibonacci Siquence: '))
n = 7
for moji in range(n-2):
    fibo.append(fibo[-1]+fibo[-2])
    
print('Fibonacci:', fibo)

print('=======================================')

main_pass = 'Jimi'

for i in range(3):
    user_pass = input('Enter Your Password: ')
    if user_pass == main_pass:
        print('Welcome!')
        break
    else:
        if i == 2:
            print('Profile Locked!')
        else:
            if 2 - i == 1:
                pol = ''
            else:
                pol = 's'
            print(f'Wrong Password. {2-i} Attempt{pol} Left. Try Again.')

print('End Program!')
