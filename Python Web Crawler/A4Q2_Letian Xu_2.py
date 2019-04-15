# Letian Xu
# 03-01-2019
# I have not given or received any unauthorized assistance on this assignment.
'''
This function takes the txt file as the input;
and return the word and its count number;
In the end, it will convert to a sorted txt file.
'''
import operator

def word_counter():
    filename = input('Enter name of file (example.txt): ')
    output_name = input('Enter name of output file (output_example.txt): ')
    print('Working...')

    counts = dict()
    bad_characters = '~`!@#$%^&*()_-+=1234567890{[}]|\\<,>.?/:;"\n'

    with open(filename, 'r') as f:
        lines = f.readlines()
        f.close()

    for line in lines:
        new_line = str()
        for character in line:
            if character not in bad_characters:
                new_line += character.lower()
        words = new_line.split(' ')
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1  
    
    del counts['']

    sort = sorted(counts.items(), key=operator.itemgetter(1))
    sort.reverse()

    with open(output_name, 'w') as o:
        for item in sort:
            o.write(item[0] + ' ' + str(item[1]) + '\n')
        o.close()

    print('Done!')

word_counter()

# top 25 results
'''
and 3620
to 2892
the 2645
rn 2149
px 1947
or 1673
for 1600
of 1544
is 1319
you 1062
not 1012
are 996
cdm 976
file 974
rntt 950
directory 936
in 931
about 927
will 926
ms 912
a 872
this 844
at 779
our 777
graduate 745
'''