##input: list=[[1, 2], [3, 4], [5, 6, 7]]
#output:[[[7, 6, 5], [4, 3], [2, 1]]


def reverse(l):
    for i in l:
        sorted=i.sort(reverse=True)
    return sorted

l=[[1, 2], [3, 4], [5, 6, 7]]