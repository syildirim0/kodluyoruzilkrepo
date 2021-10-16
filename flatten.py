''' input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]'''



def flatten(item):
    newlist=[]
    for i in item:
        if type(i)!= type([]):
            newlist.append(i)
        else:
            newlist.extend(flatten(i))