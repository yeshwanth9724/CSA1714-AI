rooms = {'A': 1, 'B': 1}
pos = 'A'

while 1:
    print("Room", pos)

    if rooms[pos] == 1:
        print("Cleaning room", pos)
        rooms[pos] = 0

    pos = 'B' if pos == 'A' else 'A'

    if rooms['A'] == 0 and rooms['B'] == 0:
        break

print("All rooms are clean")
