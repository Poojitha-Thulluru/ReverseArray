try:
    nums_array = list(map(int, input("Enter only Integers separated by space : ").split()))
    print("The Reversed array is : ", nums_array[::-1])
except ValueError:
    print("Invalid input. Enter Only Integers")