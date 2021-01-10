intro = input("give your intro:")
count = 0
space = 0
for i in intro:
    count = count+1
    if(i == ' '):
        space= space+1
print('number of character in a string')
print(count)
print('number of space in a string')
print(space)