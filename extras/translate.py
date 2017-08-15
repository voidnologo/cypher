python3

with open('ascii.txt', 'r') as f:
    ascii = f.read()

x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
y = 'HELOWARYUDINGTSVPFM.KC....'
trans_table = str.maketrans(x, y)

print(ascii.translate(trans_table))
