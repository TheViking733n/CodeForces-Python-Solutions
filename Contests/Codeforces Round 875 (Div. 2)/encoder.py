encoded = []
with open ('data.py', 'r') as file:
    for line in file:
        for char in line:
            encoded.append(chr(1+ord(char)) if char != '\n' else '\n')
with open ('data2.py', 'w') as file:
    # decoder = f"exec(''.join([chr(ord(i)-1) for i in '{''.join(encoded)}']))"
    decoder = f"exec(''.join([(chr(ord(i)-1) if i!='\n') for i in '''{''.join(encoded)}''']))"
    file.write(decoder)

