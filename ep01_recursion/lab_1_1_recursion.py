# lab 1.1 => Recursion
"""
Recursion : คือการวนการทำงานของตัวเอง ซ้ำๆ เช่น function การหาค่า factorial ของตัวเลข
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# แปลงข้อมูลที่รับค่ามาเป็นตัวเลข
number = int(input('Enter factorial number >> '))
print(factorial(number))
