#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    pass

def greet(name):
    print(f"Hello, {name}!")
    pass

print(greet("Guido"))

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    pass
print(greet_with_default())
print(greet_with_default("Sunny"))


def add(num1, num2):
    return num1 + num2
    pass
assert(add(45, 55))



def halve(number):
    return number/2
    pass
assert(halve(4))
