heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
print(heros)
heros.remove('black panther')
print(heros)
heros.insert(3,'black panther')
print(heros)
heros[1:3] = ['doctor strange']
print(heros)

# heros.sort()
# print(heros)

def sorting(elements):
    size = len(elements)
    for i in range(size-1):
        swapping = False
        for j in range(size-1-i):
            if heros[j] > heros[j+1]:
                temp = heros[j]
                heros[j] = heros[j+1]
                heros[j+1] = temp
                swapping = True
        if swapping != True:
            break
    return elements


print(sorting(heros))
