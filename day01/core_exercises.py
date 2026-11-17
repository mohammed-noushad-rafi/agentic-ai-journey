# 1
def largest(numbers):
     large=numbers[0]

     for num in numbers:
        if num>large:
            large=num
     return large 

numbers=list(map(int,input("Enter a numbers:").split()))
print("largest number among is:",largest(numbers)) 

# # 2.
def count_words(words):
   return len(words.split())

words=input("enter the word:")
print(count_words(words))

def is_palindrome(word: str) -> bool:
       return word==word[::-1]
    
word=input("enter a word:") 
print(is_palindrome("Madam"))       # expect True
print(is_palindrome("nurses run"))  # expect Truemadam
print("yes or no:",is_palindrome(word))

# 4.
def count_letters(word):
  count={}
  for letter in word:
   count[letter]=count.get(letter,0)+1
  return count
word=input("enter word:")
print("prints letter counts:",count_letters(word))

# 5.
def evens_only(nums):
    even=[n for n in nums if n%2==0]
    return even

nums=list(map(int,input("Enter numbers:").split()))
print("even numbers",evens_only(nums))

def average(nums):
   if len(nums)==0:
       return 0
   else:
       total=len(nums)
       sum_of=sum(nums)
       return sum_of/total
nums=list(map(int ,input("Enter a numbers:").split())) 
print("average",average(nums)) 
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError :
        print("no division")
        return None

print(safe_divide(1,0))