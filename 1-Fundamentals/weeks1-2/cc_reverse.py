def reverse(name):
    reversed_name = name[::-1]
    return reversed_name
    
name = input("What is your name? ")
print("Your name reversed is:", reverse(name))