def input_variations(type:str, command) -> int or float or str:
    if type == "int":
        command = int(command)
        return command * 2
    elif type == "real":
        command = float(command)
        return f"{(command * 1.5):.2f}"
    elif type == "string":
        return f"${command}$"

data_type = input()
command_as_string = input()

result = input_variations(data_type, command_as_string)

print(result)