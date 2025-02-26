def ex4_1_calculator():
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    print(f'a+b = {a+b}\na*b = {a*b}\na**b = {a**b}\na-b = {a-b}')

def ex4_2_drawing():
    def subtask1():
        print("  *\n"*4, " *")

    def subtask2():
        print("*"*5)
    def subtask3():
        print("*****\n ***\n  *")

    subtask1()
    subtask2()
    subtask2()
    subtask2()
    subtask2()
    subtask3()

def ex4_3_check_five_numbers():
    num1 = int(input("number 1: "))
    num2 = int(input("number 2: "))
    num3 = int(input("number 3: "))
    num4 = int(input("number 4: "))
    num5 = int(input("number 5: "))
    
    print((num1%2)*num1, (num2%2)*num2, (num3%2)*num3, (num4%2)*num4, (num5%2)*num5)

def ex4_4_is_it_true():
    number1 = int(input("number 1: "))
    number2 = int(input("number 2: "))
    print(f'is number1 > number2: {number1>number2}')
    print(f'is number1 odd?: {bool(number1%2)}')
    print(f'is number2 odd?: {bool(number2%2)}')
    print(f'is number1 between 0 and 100? {0<number1<100}')
    print(f'is number2 between 0 and 100? {0<number2<100}')

ex4_1_calculator()
ex4_2_drawing()
ex4_3_check_five_numbers()
ex4_4_is_it_true()