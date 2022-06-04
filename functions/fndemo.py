def cube(num):
    res=num**3
    return res
print(cube(3))

def addnumbers(n1,n2):
    return n1+n2
print(addnumbers(10,30))

def sub_number(n1,n2):
    return n1-n2
print(sub_number(10,15))

def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1
def num_chk(num):
    return "even" if num%2==0 else "odd"
print(smart_sub(30,10))
print(num_chk(16))

def is_starts_witha(name):
    return name.startswith("a")
print(is_starts_witha("aibin"))
name="technolab"
print(name.endswith("lab"))

def validate_gmail(email):
    return email.endswith("@gmail.com")
print(validate_gmail("xyz@gmail.com"))

#create a function that will return factorial of a given number

def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return(fact)
print(fact(5))

#HW 31/05/2022
# Create a function is_prime(num) will return true if number is prime else return false
def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
            break
    return True
print(is_prime(17))

# Create a function prime_range(low,upp) return all prime numbers between low to upp
def prime_range(low,upp):
    for i in range(low,upp+1):
        if is_prime(i):
           print(i,end=" ")

prime_range(5,37)

#LAMBDA FUNCTIONS
add=lambda n1,n2:n1+n2
sub=lambda n1,n2:n1-n2
smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
cube=lambda n1:n1**3
max=lambda n1,n2:n1 if n1>n2 else n2
sumofrange=lambda low,upp:sum(range(low,upp))
print(sumofrange(1,10))
print(cube(10))