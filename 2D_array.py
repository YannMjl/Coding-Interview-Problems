# 2 - Dimmensional array
# Is implemented as array of array or list of list in python

# initialize an 2D array
array_2D = [[1, 2, 3, 4],
            ["a", "b", "c", "d"]]

# or 
array_2d = [[5,6,7,8],
            [3,5,2,9]]

# print the second item in the first row
print(array_2d[0][1])
print(array_2D[0][1])

# print the third item in the second row
print(array_2D[1][2])
print(array_2d[1][2])

# ierate offer a 2D array
for row in array_2D:
    for item in row:
        print(item)

# using in range of...method
for i in range(len(array_2d)):
    for j in  range(len(array_2d[i])):
        print(array_2d[i][j])
        
