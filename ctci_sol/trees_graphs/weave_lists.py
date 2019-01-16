
"""
this program waves the given two lists.
weaving means preserving the relative order in the lists 

Eg :
    l1 = {1,2}
    l2 = {3,4}

    the weaving of l1, and l2 results in :
    {1,2,3,4}, {1,3,2,4}, {1,3,4,2}, {3,4,1,2}, {3,1,4,2}, {3,1,2,4}

"""

def print_weaved_lists(l1, l2):
    prefix = []
    results = []
    weave_lists(l1, l2, results, prefix)
    print(results)

def weave_lists(l1, l2, results, prefix):
   
    # if either fo the lists are empty 
    if len(l1) == 0 or len(l2) == 0:
        result = prefix[:]
        result.extend(l1)
        result.extend(l2)
        print (result)
        results.append(result)
        return 

    # recurse with head of fisrt list added to prefix. removing the head will damage the first list, so we will need to put it back 
    # from where it was removed afterwards 
    head_first = l1.pop(0)
    prefix.append(head_first)
    weave_lists(l1, l2, results, prefix) 
    prefix.pop()
    l1.insert(0, head_first)

    # doing the same thing here as well for the second list. removing the head of the second list and adding it back 
    head_second = l2.pop(0)
    prefix.append(head_second)
    weave_lists(l1, l2, results, prefix) 
    prefix.pop()
    l2.insert(0,head_second)

if __name__ == "__main__":
    l1 = ['1','2']
    l2 = ['3', '4']

    """
    # extracting only the unique elements, use this if the inputs are very huge 
    s1 = set(l1)
    l1 = list(s1)
    s2 = set(l2)
    l2 = list(s2)
    """
    print_weaved_lists(l1,l2)
