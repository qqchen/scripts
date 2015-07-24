file_object = open('positions.txt')
output = open('output.txt', 'w')
all_lines = file_object.readlines()

for line in all_lines:
    line = line.strip()
    x = line.split(' ')
    y = ''.join(x)
    print y
    output.write(y + '\n')

file_object.close()
output.close()