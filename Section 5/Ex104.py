data = []

num = int(input('Enter any number (0 to quit): '))

while num != 0:
     data.append(num)
     num = int(input('Enter number (0 to quit): '))
     
data.sort()
print('The values sorted in ascending data are: ')

for num in data:
    print(num)
