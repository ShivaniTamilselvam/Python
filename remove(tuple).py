tuplex="w","3","r","s","0","u","r","c","e"
print(tuplex)
tuplex=tuplex[:2]+tuplex[3:]
print(tuplex)
listx=list(tuplex)
listx.remove("c")
tuplex=tuple(listx)
print(tuplex)
