def add(*args):  #any arguments will be accepted as tuple
    return sum(args)
print(add(10,20))
print(add(10,20,30))

def max_fun(*args):
    return max(args)
def min_fun(*ar):
    return min(ar)
print(min_fun(10,55,25,1,89))
