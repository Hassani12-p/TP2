
L = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8]
index = 0
while index < len(L):
    element = L[index]
    if L.count(element) > 1:
        L.remove(element)
    else:
        index += 1

print("Liste après suppression des doublons :", L)
