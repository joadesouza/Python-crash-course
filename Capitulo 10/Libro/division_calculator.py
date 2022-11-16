print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        print("----PROGRAMA FINALIZADO----")
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        print("----PROGRAMA FINALIZADO----")
        break
    
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("\nYou can't divide by zero")
    else:
        print(f"\n{first_number}/{second_number} = {answer}")