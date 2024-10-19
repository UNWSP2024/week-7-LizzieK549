# Program #4: Coordinates
import math

def coordinates():
    coordinate1 = x1, x2, x3
    coordinate2  = y1, y2, y3
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


#Program #4: Coordinates

#Write a distance function that will take two 3-dimensional
#coordinates (as input) and will return (as output) the distance
#between those points in space. The 3-dimensional coordinates must be
#stored as tuples.
#The mainline calls the distance function and stores the
#distance in a variable. The mainline then displays the distance.
# Also include exception handling to deal
#with faulty input.
# The distance between two points (x1,y1,z1)
#and (x2, y2, z2) is
#given by:

#sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 -z2)^2)'''

import math

def coordinates(coordinate1, coordinate2) :   #remember to take both positional arguments here
    x1, y1, z1 = coordinate1
    x2, y2, z2 = coordinate2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) #math for formula

def main():
    try:
        #Now write a mainline that has the user enter the two tuples.
        x1 = float(input("Enter the X1 for the first coordinate: "))
        y1 = float(input("Enter the Y1 for the first coordinate: "))
        z1 = float(input("Enter the Z1 for the first coordinate: "))

        x2 = float(input("Enter the X2 for the second coordinate: "))
        y2 = float(input("Enter the Y2 for the second coordinate: "))
        z2 = float(input("Enter the Z2 for the second coordinate: "))

        coordinate1 = (x1, y1, z1)  #stores distance in a variable
        coordinate2 = (x2, y2, z2)

        answer = coordinates(coordinate1, coordinate2)
        print("The distance between the 3D coordinates is ", answer)

    except ValueError:    #deals with non-number inputs
        print("Invalid input. Place enter numbers")

    except Exception as e:  #handles all other errors
        print("Error, please try again.😢")

if __name__ == '__main__':
    main()
