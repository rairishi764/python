def power(base, exponent):
    if (exponent == 0):
        return 1
    if (exponent > 0):
        return base* power(base, exponent-1)
    else:
        return -1    
    

def factorial(n):
    if(n>0):
        return n* factorial(n-1)
    else:
        return 1

def productOfArray(arr):
    if (len(arr)>0):
        print(arr)
        return arr.pop(0)*productOfArray(arr) 
    else:
        return 1

def recursiveRange(num):
    if (num<0):
        return 0
    return num + recursiveRange(num-1)

def fib(num):
    if (num < 2):
        return num
    return fib(num - 1) + fib(num - 2)

def reverse(strng):
    #print(len(strng)>0)
    if(len(strng)>0):
        return (reverse(strng[1:])+strng[0])
    else:
        return ''

def isPalindrome(strng):
    reverseStr = reverse(strng)
    if (reverseStr==strng):
        return True
    else:
        return False

obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
             sum+=nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key]%2==0:
             sum+=obj[key]
        
    return sum


def capitalizeWords(arr):
    farr = []
    if len(arr)==0:
        return farr
    else:
        farr.append(arr[0].upper())
        return farr+capitalizeWords(arr[1:])
                
words = ['i', 'am', 'learning', 'recursion']
#print(capitalizeWords(words)) # ['I', 'AM', 'LEARNING', 'RECURSION']

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}
def stringifyNumbers(obj):
    numbers=''
    for k,v in obj.items():
        if isinstance(v, dict):
            for k1,v1 in v.items():
                numbers = numbers+' '+stringifyNumbers(v)
        elif isinstance(v, int):
            numbers = numbers+' '+str(v)
    return numbers            

print(stringifyNumbers(obj))
    # TODO

    
    # TODO

#print(nestedEvenSum(obj2))
#print(reverse('python')) # 'nohtyp'
#print(reverse('appmillers')) # 'srellimppa'

#print(recursiveRange(6)) # 21
#print(recursiveRange(10)) # 55 

#print(power(2,4))
#print(power(2,0))
#print(power(2,2))

#print(factorial(1))
#print(factorial(2))
#print(factorial(4))

#print(productOfArray([1,2,3])) #6
#print(productOfArray([1,2,3,10])) #60