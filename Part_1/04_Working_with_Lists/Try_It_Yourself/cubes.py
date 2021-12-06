'''
a number raised to the third powewr is called a cube. for example, the cube of
2 is written as 2**3 in python. make a list of the first 10 cubes (that is, the
cube of each integer from 1 through 10), and use a for loop to print out the 
value of each cube.
'''

cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)
print(cubes)
