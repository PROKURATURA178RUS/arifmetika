input_data = open('input.txt','r')
data = input_data.read ()
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
d = print
if a >= 10**2:
    print('Неверно')
if b >= 10**2:
    print('Неверно')
if c >= 10**6:
    print('Неверно')
if a * b == c :
    print('yes')
else:
    print('no')
output_data = open('output.txt','w')
output_data.write()
input_data.close()
output_data.close()