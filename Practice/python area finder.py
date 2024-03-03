option = int(input("option 1 or 2? "))
if option == 1:
    r = float(input("enter a radius of a circle : "))
    area = 3.12*r*r
    print (area,"cm2 ","is the area")
else:
    side =  float(input("enter the side of a square"))
    area = (side*side)
    print (area,"cm2 ","is the area")
