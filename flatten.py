def flatten(item):
    newlist=[]
    for i in item:
        if type(i)!= type([]):
            newlist.append(i)
        else:
            newlist.extend(flatten(i))