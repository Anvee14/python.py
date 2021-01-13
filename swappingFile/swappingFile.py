print('write the 1st file name to swap data ')
file_1 = input('File1:')
print('write the 2nd file name to swap data ')
file_2 = input('File2:')


def swapData(file1, file2):
    with open(file1, 'r') as a:
        data_a = a.read()
    with open(file2, 'r') as b:
        data_b = b.read()
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'w') as b:
        b.write(data_a)
    

print(swapData(file_1, file_2))
