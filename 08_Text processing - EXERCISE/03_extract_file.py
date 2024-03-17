path_separated = input().split("\\")

name, extension = path_separated[-1].split(".")

print(f"File name: {name}")
print(f"File extension: {extension}")



