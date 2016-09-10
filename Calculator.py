while True:
    while True:
        try:
            num1 = int(input('Enter first number: '))
            break
        except ValueError:
            print ('Can you enter correct a number?')
    while True:
        try:
            num2 = int(input('Enter second number: '))
            break
        except ValueError:   
            print ('Can you enter correct a number?')
    while True:
        sign = input('What do you want to do?(+,-,*,/): ')
        if sign == '+' or sign == '-' or sign == '*' or sign == '/' : 
            break
        else :
            sign = input('What do you want to do?(+,-,*,/): ')
    if sign == '+':
        result = num1 + num2
    elif sign == '-':
        result = num1 - num2
    elif sign == '*':
        result = num1 * num2
    elif sign == '/':
        result = num1 / num2
    print(result)
    continiue = input('If you want go on this program enter Y: ')
    if continiue != 'Y':
        break


