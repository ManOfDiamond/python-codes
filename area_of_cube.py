# Write a user defined funcion to find to find the area of cube
def area_cube():
    s = float(input("Enter the side of the cube: "))
    a = s**2
    print("Area of cube with side", s,"units is",round(a,2),"sq. units")
area_cube()
'''
Output:
Enter the side of the cube: 14.5
Area of cube with side 14.5 units is 210.25 sq. units
'''