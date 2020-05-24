# Define the operations
def addition(first_number, second_number):
    answer = first_number + second_number
    return answer


def subtraction(first_number, second_number):
    answer = first_number - second_number
    return answer


def multiplication(first_number, second_number):
    answer = first_number * second_number
    return answer


def division(first_number, second_number):
    answer = first_number / second_number
    return answer


#  Defining function to perform switch-case
def switch(case):
    if case < 1 or case > 4:
        return "Invalid Entry"
    else:
        num_1 = float(input("Enter the first number: "))
        num_2 = float(input("Enter the second number: "))
        operations = [addition(num_1, num_2), subtraction(num_1, num_2),
                      multiplication(num_1, num_2), division(num_1, num_2)]
        index = int(case) - 1
        function = operations[index]
        print("\nThe result is")
        return function


print("Below are the operations you can perform:- ")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
user_input = int(input("Enter choice: -  "))
solution = switch(user_input)
print(solution)
