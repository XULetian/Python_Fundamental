# Letian Xu
# 03-01-2019
# I have not given or received any unauthorized assistance on this assignment.

import statistics

a = open ('avocado.csv','r')
avocado = a.readlines()
a.close()

attribute = avocado[0].split(',')
new_avocado = []
for row in avocado[1:]:
    new_avocado.append(row.split(','))

'''
a)	Define a function that takes a variable name in the form of a string (e.g. “Total Volume”), 
reads into memory the values for that variable (but just that variable) and computes the mean using the statistics module.
'''
def readAndComputeMean(column):
    index = attribute.index(column)
    mylist = []
    for row in new_avocado:
        mylist.append(float(row[index]))
    return statistics.mean(mylist)


'''
b)	Define a function that takes a variable name in the form of a string (e.g. “Total Volume”), 
reads into memory the values for that variable (but just that variable) and computes the standard deviation using the statistics module.
'''

def readAndComputeSD(column):
    index = attribute.index(column)
    mylist = []
    for row in new_avocado:
        mylist.append(float(row[index]))
    return statistics.stdev(mylist)


'''
c)	Define a function that takes a variable name in the form of a string (e.g. “Total Volume”), 
reads into memory the values for that variable (but just that variable) and computes the median using the statistics module.
'''

def readAndComputeMedian(column):
    index = attribute.index(column)
    mylist = []
    for row in new_avocado:
        mylist.append(float(row[index]))
    return statistics.median(mylist)


'''
d)	Repeat a-c, but instead of using the statistics module write your 
own “homegrown” code to compute the mean, standard deviation and median.
'''

def readAndComputeMean_HG(column):
    index = attribute.index(column)
    mylist = []
    for row in new_avocado:
        mylist.append(float(row[index]))
    mean_HG = sum(mylist)/len(mylist)
    return mean_HG


def readAndComputeSD_HG(column):
    index = attribute.index(column)
    mylist = []
    for row in new_avocado:
        mylist.append(float(row[index]))
    mean = sum(mylist)/len(mylist)
    sum_HG = []
    for i in mylist:
        sum_HG.append((i - mean)**2)
    n = len(mylist) - 1
    std_HG = (sum(sum_HG)/n)**(1/2)
    return std_HG


def readAndComputeMedian_HG(column):
    index = attribute.index(column)
    mylist = []
    for row in new_avocado:
        mylist.append(float(row[index]))
    n = len(mylist)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(mylist)[n//2]
    else:
            return sum(sorted(mylist)[n//2-1:n//2+1])/2.0


'''
e)	Repeat a-c, but your functions must be memoryless – 
you can hold in memory only a single value from the file at any given time.   
You may need to keep track of min, max, sum or a handful of counters.
'''

def readAndComputeMean_MML(column):
    index = attribute.index(column)
    mysum = 0
    count = 0
    for row in new_avocado:
        mysum += float(row[index])
        count += 1
    mean_HG = mysum/count
    return mean_HG


def readAndComputeSD_MML(column):
    index = attribute.index(column)
    mysum = 0
    count = 0
    for row in new_avocado:
        mysum += float(row[index])
        count += 1
    mean = mysum/count
    sum_HG = 0
    for row in new_avocado:
        sum_HG += (float(row[index]) - mean)**2
    count -= 1
    std_HG = (sum_HG/count)**(1/2)
    return std_HG


def readAndComputeMedian_MML(column):
    '''
    Useing the Binary search to get the closest number to the median without sorted whole list.
    As long as we can get the cloest number, we can use another for loop to get the median.
    '''
    index = attribute.index(column)
    n = len(new_avocado)
    
    #Get the min and max value
    low = float(new_avocado[0][index])
    high = float(new_avocado[-1][index])
    for row in new_avocado:
        if float(row[index]) <= low:
            low = float(row[index])
        elif float(row[index]) >= high:
            high = float(row[index])

    k = round(n/2)
    count = 0
    while count != k + 1:
        count = 0
        mid = low+(high-low)/2
        for row in new_avocado:
            if float(row[index]) <= mid:
                 count += 1
        
        if count < k+1:
            low = mid
        else:
            high = mid
    
    gap = mid - low
    
    for row in new_avocado:
        if mid - float(row[index]) < gap and float(row[index]) < mid:
            gap = mid - float(row[index])       

    return mid - gap

'''
f)	Write test code to demonstrate that the means, standard deviations and medians are the same across all three techniques.
'''

mean_SM = readAndComputeMean('Total Volume')
sd_SM = readAndComputeSD('Total Volume')
median_SM = readAndComputeMedian('Total Volume')

mean_HG = readAndComputeMean_HG('Total Volume')
sd_HG = readAndComputeSD_HG('Total Volume')
median_HG = readAndComputeMedian_HG('Total Volume')

mean_MML = readAndComputeMean_MML('Total Volume')
sd_MML = readAndComputeSD_MML('Total Volume')
median_MML = readAndComputeMedian_MML('Total Volume')

print("The statistics number for statistics module technique are mean: {}, standard deviation: {}, median: {}".format(mean_SM,sd_SM,median_SM))
print()
print("The statistics number for homegrown technique are mean: {}, standard deviation: {}, median: {}".format(mean_HG,sd_HG,median_HG))
print()
print("The statistics number for memoryless technique are mean: {}, standard deviation: {}, median: {}".format(mean_MML,sd_MML,median_MML))