x=lambda n:n+5
print(x(10))

def message():
    return 'welcome to college'
message()

l=[6,7,7,6,5,4,3]
s=set(l)
print(s)

def squares(n):
    for i in range(n,0,-1):
        a=i**2
        print(a)
squares(10)

for i in range(1,101):
    if i%7==0 or i%11==0:
        print(i,end=",")
print()

s="venugopal"
for i in s:
    print(i,end=",")

def rev_sentence(sentence): 
  
    # first split the string into words 
    words = sentence.split(' ') 
  
    # then reverse the split string list and join using space 
    reverse_sentence = ' '.join(reversed(words)) 
  
    # finally return the joined string 
    return reverse_sentence 
  
if __name__ == "__main__": 
    input = 'geeks quiz practice code'
    print (rev_sentence(input))

def fohrenheit(n):
    return (n-32)*5/9
def celcius(n):
    return (n*1.8)+32
n=float(input("enter a number: "))
print(fohrenheit(n))
print(celcius(n))

factorial of a number:
def fact(n):
    if n<0:
        return "only for possitive numbers"
    elif n in (0,1):
        return "1"
    else:
        i=n
        fact=1
        while i>0:
            fact=fact*i
            i-=1
        return fact
n=int(input("enter a number: "))
a=fact(n)
print(a)

def fun(a,b,c):
    x=(-b+((b**2-4*a*c)**1/2))/2*a
    y=(-b-((b**2-4*a*c)**1/2))/2*a
    return x,y
print(fun(1,2,3))
print(fun(3,5,1))

from genericpath import exists


def fact(n):
    if n<0:
        return "not exist"
    elif n in (0,1):
        return "1"
    else:
        return n*fact(n-1)
print(fact(5))