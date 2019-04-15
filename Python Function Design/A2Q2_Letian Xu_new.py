# Letian Xu
# 01-28-2019
# I have not given or received any unauthorized assistance on this assignment.


print('Welcome!')
print('This program will use random numbers to compute the area of an ellipse.')
'''
Arugument: input the position of F1 and F2, the length of major axis,
        and the number of random point to estimate the erea.
Return: the number of random points that satisfy the requirement of the equation:
        |PF1| + |PF2| = 2a.
Notes: from 100 to -100 is the random points' range.
        the return value, the number of random points, is a approximate number of the erea of ellipse.
'''

x1, y1 = input("Enter the position of F1 (format: x y): ").split(' ')
x2, y2 = input("Enter the position of F2 (format: x y): ").split(' ')

m_axis = int(input("Enter the length of the major axis (format: 1): "))
ran_number = int(input("Enter the number of random points (format: n): "))

print('Thinking…')

import random 

#Get the number of random points
coords = [(random.uniform(-100,100), random.uniform(-100,100)) for _ in range(ran_number)]

area = 0

for i in range(ran_number):
        #Get the random point data from coordinate list first
        point = coords[i]
        #Extract the x and y value of a random point
        p1 = point[0]
        p2 = point[1]
        #Calculte PF1 length 
        pf_1 = ((p1-float(x1))**2 + (p2-float(y1))**2)**0.5
        #Calculte PF1 length
        pf_2 = ((p1-float(x2))**2 + (p2-float(y2))**2)**0.5

        #Use the equation to estimate the area of ellipse
        if pf_1 + pf_2 <= m_axis:
                #Use number of random point to estimate the erea of ellipse
                area += 1


print('The area of the ellipse is approximately ',area,'.')
