from _collections import deque

end_command = "End"
paid_command = "Paid"

names_queue = deque()

while True:
    command = input()
    if command == end_command:
        print(f'{len(names_queue)} people remaining.')
        break
    elif command == paid_command:
        while names_queue:
            print(names_queue.popleft())
    else:
        names_queue.append(command)
