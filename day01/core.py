#list datatype
scores = [78,23,45,6,7,42,44]
print(scores[0])
print(scores[-7])
print(scores[::-1])
print(scores[1:5])
print(scores[:6])
print(scores[-1:-6:-2])
#methods of list
#append ,insert,pop,remove,sum,min,max,sort,reverse,in,len
print(scores)
print(len(scores))
scores.append(400)
print(scores)
scores.insert(0,200)
print(scores)
scores.remove(6)
print(scores)
scores.pop()
print(scores)
print(sum(scores))
print(min(scores))
print(max(scores))
print(sorted(scores))
print(sorted(scores, reverse=True))

#dictionary datatype
student={"name":"john","age":20,"marks":99}
print(student)
print(student["name"])
print(student["age"])
print(student["marks"])
print(student.keys())
print(student.get("name"))
print(student.get("class"))
print(student.get("class","not found"))
student["age"] = 23
print(student)
del student["marks"]
print(student)
for key,value in student.items():
    print(f"{key}: {value}")

word = "banana"
counts = {}
for letter in word:
    counts[letter]=counts.get(letter,0)+1
    print(counts)   

#if else statments
if 5>3:
    print("5 is greater than 3")    
elif 3>5:
    print("3 is greater than 5")
else:
    print("both are equal")

#combination 
if 5>3 and 1>3:
    print("5 is greater than 3 and 3 is greater than 1")
elif 5>3 or 3>1:
    print("either 5 is greater than 3 or 3 is greater than 1")
elif not (5>3 and 3>1):
    print("neither 5 is greater than 3 nor 3 is greater than 1")

#for loop
for score in [78,23,43,6,98]:
    print(score)

for score in range (5):
    print(score)

for score in range(1,10,2):
    print(score)

for i,value in enumerate(["JAVA","PYTHON","C"],start=1):
    print(i,value)

#while loop
count=0
while count<5:
    print(count)
    count+=1

#break and continue
for n in range(10):
    if n==3:
        continue
    elif n==7:
        break
        print(n)

#functions
def add(a,b):
    return a+b        

sum_of_numbers = add(2,56)
print(sum_of_numbers)

nums = [1, 2, 3, 4, 5, 6]
squares=[n*n for n in nums]
print(squares)
even=[n for n in nums if n%2==0]
print(even)
words=["love","peace","happiness"]
word= [w.upper() for w in words]
words = [w.upper() for w in ["rag", "llm", "agent"]]
print(word)
print(words)
