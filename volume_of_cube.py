# Write a user defined funcion to find to find the volume of cube
def volume_cube():
    s = float(input("Enter the side of the cube: "))
    v = s**3
    print("Volume of cube with side", s,"units is",round(v,2),"cube units")
volume_cube()
'''
Output:
Enter the side of the cube: 25
Volume of cube with side 25.0 units is 15625.0 cube units
'''