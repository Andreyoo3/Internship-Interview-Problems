#Given the binary tree in the image below, use a built in python data structure
#to represent the binary tree and easy to find any nodes within a given
#interval (say: find all nodes that have a value between 23 and 68).

from collections import defaultdict
from pprint import pprint

def tree():
    return defaultdict(tree)

def stddict(t):
    return {k: stddict(t[k]) for k in t}

def find_value(myDict, sought_value, current_path, result):   
    for key,value in myDict.items():
        current_path.pop()
        current_path.append(key)
        if sought_value in key:
            result.append(current_path[:])
        if type(value) == type(''):
            if sought_value in value:
                result.append(current_path+[value])
        else:
            current_path.append(key) 
            result = find_value(value, sought_value, current_path, result)
    current_path.pop()
    return result

#============================================================================
#main:

giventree = tree()

giventree['50']['17']['12']['9']
giventree['50']['17']['12']['14']
giventree['50']['17']['23']['19']
giventree['50']['72']['54']['67']
giventree['50']['72']['76']

foundValues = []

print ("Enter the interval for the search: ")
valmin = int(input())
valmax = int(input())

for val in range (valmin, valmax): 
    result = find_value(giventree, str(val), ['START_KEY'], [])
    if len(result) == 1:
        foundValues.append(val)
        
print (foundValues)

#============================================================================
#This function, if not commented, prints the whole given tree
#pprint(stddict(giventree))
