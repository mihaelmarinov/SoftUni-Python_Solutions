phonebook = {}

while True:
    command = input()
    if command.isdigit():
        for _ in range(int(command)):
            search = input()
            if search in phonebook:
                value = phonebook[search]
                print(f'{search} -> {value}')
            else:
                print(f'Contact {search} does not exist.')
        break
    else:
        name, number = command.split("-")
        phonebook[name] = number

