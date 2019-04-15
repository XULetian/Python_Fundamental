# Letian Xu
# 01/10/2019
# I have not given or received any unauthorized assistance on this assignment.

def overlap(s1,s2):
    '''
    Arguments: s1 and s2 represent two lists, also represent a square. 
    Return: The area of the overlap of the two squares, if the squares do not overlap, return 0.
    '''
    # Use the range function to get a list for the horizontal side of a square;
    # and the set() method to get intersection of two lists;
    # this the lenth of two squares' overlap on x-axis.
    x1 = list(range(s1[0],s1[0]+s1[2]))
    x2 = list(range(s2[0],s2[0]+s2[2]))
    x = len(set(x1) & set(x2))

    # and this is the lenth of two squares' overlap on y-axis
    y1 = list(range(s1[1],s1[1]+s1[2]))
    y2 = list(range(s2[1],s2[1]+s2[2]))
    y = len(set(y1) & set(y2))

    # If the one of the lenth was 0, the result will return 0.
    return x*y

totalScore = 0

S1 = [1,5,3]
S2 = [5,6,2]
S3 = [2,1,2]
S4 = [9,6,2]
S5 = [7,2,3]
S6 = [3,2,5]
S7 = [5,3,1]

#---------- ---------- ---------- ---------- ----------
print( "Test 1: " + str(S1) + str(S6) )
print( "Correct Answer: 2" )
r1 = overlap(S1,S6)
r2 = overlap(S6,S1)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 2:
    s1 = s1 + 1
if r2 == 2:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 2: " + str(S2) + str(S6) )
print( "Correct Answer: 2" )
r1 = overlap(S2,S6)
r2 = overlap(S6,S2)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 2:
    s1 = s1 + 1
if r2 == 2:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 3: " + str(S3) + str(S6) )
print( "Correct Answer: 1" )
r1 = overlap(S3,S6)
r2 = overlap(S6,S3)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 1:
    s1 = s1 + 1
if r2 == 1:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 4: " + str(S4) + str(S6) )
print( "Correct Answer: 0" )
r1 = overlap(S4,S6)
r2 = overlap(S6,S4)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 0:
    s1 = s1 + 1
if r2 == 0:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 5: " + str(S5) + str(S6) )
print( "Correct Answer: 3" )
r1 = overlap(S5,S6)
r2 = overlap(S6,S5)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 3:
    s1 = s1 + 1
if r2 == 3:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 6: " + str(S6) + str(S6) )
print( "Correct Answer: 25" )
r1 = overlap(S6,S6)
r2 = overlap(S6,S6)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 25:
    s1 = s1 + 1
if r2 == 25:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 7: " + str(S7) + str(S6) )
print( "Correct Answer: 1" )
r1 = overlap(S7,S6)
r2 = overlap(S6,S7)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 1:
    s1 = s1 + 1
if r2 == 1:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print ( "Total Score: " + str(totalScore) )
print ( "Percentage: " + str(100*totalScore/14) )






