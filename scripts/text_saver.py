text = input("Enter some text: ")

with open("saved_input.txt", "a") as file:
    file.write(text+ "\n")
print("Your input has been saved to saved_input.txt")
