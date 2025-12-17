lst = ["Apple",'Guava', "Mango", 'Banana', "Watermelon"]


print("Length of List:", len(lst))
print("first element:", lst[0])
print("last element:", lst[-1])

lst.append('peaches')
print("Updated List:", lst)


lst.remove('Apple')
print("Updated List:", lst)


lst.sort()
print("Sorted List:", lst)


lst.pop(1)
print("Updated List:", lst)

lst.reverse()
print("reversed List:", lst)

print("Multipication on List :", lst*2)


lst = lst[:4]
print("Sliced List:", lst)

lst.clear()
print("Updated List:", lst)






