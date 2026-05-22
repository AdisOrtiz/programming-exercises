"""
Define una función que combine dos listas ordenadas en una sola lista ordenada
"""

def listas_ordenadas(l1,l2):
    return sorted(l1+l2)

l1 = [1,23,5,47,9]
l2 = [2,4,36,8,0]

print(listas_ordenadas(l1,l2))
    