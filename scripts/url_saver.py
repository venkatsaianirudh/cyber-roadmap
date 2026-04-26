url = input("Enter a URL: ")

with open("saved_urls.txt", "a") as file:
    file.write(url + "\n")

print("URL saved.")
