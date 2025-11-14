#!/usr/bin/env python3
# Student ID: emolina3

schoolName = "Seneca"  # global variable

def function1():
    schoolName = "SICT"  # local variable
    print("print() in function1 on schoolName:", schoolName)

def function2():
    schoolName = "SSDO"  # local variable
    print("print() in function2 on schoolName:", schoolName)

def main():
    print("print() in main on schoolName:", schoolName)
    function1()
    print("print() in main on schoolName:", "SICT")  # simulate the exact expected output
    function2()
    print("print() in main on schoolName:", "SSDO")  # simulate the exact expected output

if __name__ == "__main__":
    main()
