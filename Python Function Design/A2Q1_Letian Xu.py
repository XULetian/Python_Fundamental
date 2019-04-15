# Letian Xu
# 01-28-2019
# I have not given or received any unauthorized assistance on this assignment.

import pandas as pd
import string

all_letters = list(string.ascii_lowercase)
# print(all_letters)

 #Create name lists from data file
boys = pd.read_csv('namesBoys.txt',header=None)
girls = pd.read_csv('namesGirls.txt',header=None) 
b_list = list(boys[0])
g_list = list(girls[0])

def last_count():
    '''
    Argument: the data file with 1000 boys' and girls' names;
    Return: return two dictionary that contain the frequency of a name ends in a particular letter.
    '''
    #Create dictionaries for boys and girls
    b_dict = {}
    g_dict = {}

    #Get last letter of boy names
    for boy in b_list:
        b_last_letter = list(boy)[-1]
        # counter for last letter exists
        if b_last_letter in b_dict:
            b_dict[b_last_letter] += 1
        # counter for last letter doesn't exist
        else: 
            b_dict[b_last_letter] = 1

    #Get last letter of girl names
    for girl in g_list:
        g_last_letter = list(girl)[-1]
        # counter for last letter exists
        if g_last_letter in g_dict:
            g_dict[g_last_letter] += 1
        # counter for last letter doesn't exist
        else: 
            g_dict[g_last_letter] = 1

    #Wrap two dictionary into a dataframe
    df = pd.DataFrame(columns = ['Letter','Boys','Girls'])
    df.Letter = all_letters
    #Map dictionary to columns
    df.Boys = df.Letter.map(b_dict)
    df.Girls = df.Letter.map(g_dict)
    #Filling NA with 0
    df.fillna(0, inplace = True)

    return b_dict, g_dict

b_dict, g_dict = last_count()

#Wrap two dictionary into a dataframe
df = pd.DataFrame(columns = ['Letter','Boys','Girls'])
df.Letter = all_letters
#Map dictionary to columns
df.Boys = df.Letter.map(b_dict)
df.Girls = df.Letter.map(g_dict)
#Filling NA with 0
df.fillna(0, inplace = True)

print(df)

# Compare to the boy's name, it looks like that girls's name were tend to be more limited;
# the majority of the ending letter in girls' name was a, and lots of letters was not used in the end of girls' names,
# it is speculated that boys' name show more diversity than girls name based on the observation.