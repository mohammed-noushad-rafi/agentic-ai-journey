print("hello world")#print stament
print("hello", "world")#we can separate each words and statments with comma
print()#print can be empty to create a line break

#variables
a=10
b="string" 
c=3.44
print(a)
print(b)
print(c)
c="changed value"
print(c)

#data types
number=10
string="this is a string"
float_number=3.43
boolean_value=True
none_value=None
print(type(number))
print(type(string))
print(type(float_number))
print(type(boolean_value))
print(type(none_value))
#type conversion
print(int("10"))
print(float("3.43"))
print(str(10))
print(bool(1))
print(bool(0))

a = 17
b = 5

print(a + b)    # 22
print(a - b)    # 12
print(a * b)    # 85
print(a / b)    # 3.4   "/" always gives a float
print(a // b)   # 3     whole-number division (drops the remainder)
print(a % b)    # 2     remainder only (called "modulo")
print(a ** 2)   # 289   power

counter=10
print(counter)
counter+=5
print(counter)
counter-=3
print(counter)
counter*=2
print(counter)

#Strings
word = "python"

# p y t h o n
# 0 1 2 3 4 5
# -6 -5 -4 -3 -2 -1
print(word[0])
print(word[-1])
print(len(word))

#slicing
print(word[1:5])
print(word[1:5])
print(word[:3])
print(word[0:5:2])#skipping character
print(word[::-1])
print(word[-1:-6:-2])#skipping character in reverse order

#string methods
sentances = " I am learning AI Agents "
print(sentances.strip())
print(sentances.lower())
sentances = sentances.upper()
print(sentances)
print("am" in sentances)
print(sentances.count("a"))
sentances=sentances.replace("learning", "learned")
print(sentances)
sentances=sentances.strip().split()
print(sentances)

#joining strings
words = ["I","Am","learning","AI","Agents"]
words = " ".join(words)
words = ",".join(words)
print(words)

#f strings
name = "noushad rafi"
hours = 8
days = 28
print(f"I am {name} and I am studying {hours} hours in a {days} days")
print (f"which is{hours*days}hours in total")#we can do calculation inside f strings
print(f"{name.upper()}")#we can do string methods inside f strings

topic = "python f strings"
prompt = f"we are learning {topic} today"
print(prompt)

#input staments

#name = input("whats your name?")
#print(f"hello {name } welcome to the python world")

age = input ("Whats your age?")
print(type(age))
age=int(age)
print(type(age))
print(f"my age is {age}")
age+=3
print(f"my age in 3 years will be {age}")