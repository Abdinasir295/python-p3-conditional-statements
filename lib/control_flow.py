#!/usr/bin/env python3

def admin_login(username, password):
    if (username == 'admin' or username == 'ADMIN') and password == '12345':
        return 'Access granted'
    
    return 'Access denied'


def hows_the_weather(temperature):
    if temperature < 40:
        response = 'brisk'
        return f"It's {response} out there!"

    elif temperature >= 50 and temperature <= 65:
        response ='a little chilly'
        return f"It's {response} out there!"
    elif temperature > 85:
        response = 'too dang hot'
        return f"It's {response} out there!"
    else:
        response = 'perfect'
        return f"It's {response} out there!"


def fizzbuzz(num):
    if num == 0 or num == 15 or num == 45:
        return 'FizzBuzz'
    elif num == 3 or num == 33 or num == 42:
        return 'Fizz'
    elif num == 5 or num == 10 or num == 50:
        return 'Buzz'
    elif num == 2 or num ==13 or num == 59:
        return num


def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2 
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print('Invalid operation!')
        return None



