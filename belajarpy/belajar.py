print("=========================================================================================")

str_numbers = "456"
str_numbers_to_int = int (str_numbers)
print("Before casting : ", str_numbers, ", the data type is",type(str_numbers)) 
print("After casting : ", str_numbers_to_int, ", the data type is",type(str_numbers_to_int) )   

print("=========================================================================================")

intreger = 12345
intreger_to_str = str(intreger)
print("Before casting : ",intreger," The data type is ", type(intreger))
print("After casting : ",intreger_to_str," The data type is ", type(intreger_to_str))

print("=========================================================================================")

num_int = 1
num_bool = bool(num_int)
print(num_bool,type(num_bool))

num_int = 0
num_bool = bool(num_int)
print(num_bool,type(num_bool))

print("=========================================================================================")

a = True
b = True
print(a and b)
print(a or b)
print(not b)

print("=========================================================================================")

e = 8
f = 2
#Sumation
sum = e + f
print(f"the sum of e with f is : {sum}\n")

#Reduce
sum = e - f
print(f"the sum of e - f : {sum}\n")

print("=========================================================================================")

#multiplication
multi = e * f
print(f"The multipication of e with f is : {multi}\n")

#Division
divi = e / f
print(f"The quotient of e with f is : {divi}\n")

#Modulo
mod = e%f
print(f"The reminder of e and f is : {mod}\n")

#Power
pow = e ** f
print(f"The power of e adn f is : {pow}\n")

print("=========================================================================================")

name = str (input("What is your name : "))
age = int (input("What is your age : "))

print("name : ", name)
print("Age : ", age)

# normal print
print('Hi all! I am', name, 'age', age, 'years old')

# format print
print(f'Hi all! I am {name} age {age} years old')

# format print
print(f'Hi all! I am %s age %d years old'%(name, age))

# fortmat output
print(40*"=")
print(f'Welcome {name} Selamat Ulangtahun Yang ke {age}')
print(40*"=")

print("=========================================================================================")

your_GPA = float(input("Enter your GPA : "))
if 4.0 >= your_GPA >= 0.0:
    if 4.0 >= your_GPA >= 3.80:
        print(f"Damm you've got a magna cumlaude with your {your_GPA} GPA")
    elif 3.50 <= your_GPA <3.80:
        print(F"Cool You've got a cumlaude with your {your_GPA} GPA")
    elif 3.00 <= your_GPA <3.50:
        print(f"You've got stable GPA tho")
    elif your_GPA < 3.0:
        print(f"You need a stable GPA")
else:
    print(f"Sorry, your GPA {your_GPA} is out of range and invalid")
    
print("=========================================================================================")

status_code = int (input("Enter your status code : "))
print("your code means")
match status_code:
    case 200:
        print("Succes")
    case 400:
        print("Bad request")
    case 401:
        print("Unauthorized")
    case 402:
        print("Payment request")
    case 404:
        print("Not found")
    case 500:
        print("Internal server eror")
        
print("=========================================================================================")

a = 3
b = "even Numebers" if a % 2 == 0 else "odd numbers"
print (b)
        
print("=========================================================================================")

for i in range (5):
    print("Data science is easy")

print(50*"=")
for i in range (1,5,2):
    print("Data science is easy")

for i in range (1,5,1):
    print("Coba")

print("=========================================================================================")

word = "I want to master data science"
for letter in word:
    print(letter)

print("=========================================================================================")

for m,n in enumerate (word):
    print(f"index {m}. {n} ")

for i in range(5,1,-1):
    print("I want big data's")

print("=========================================================================================")

for i in range (5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)

print("=========================================================================================")

count = 0
while count < 4:
    print ("Keep the spirits up interns! ")
    count += 1 