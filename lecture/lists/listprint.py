my_list = [2, 3, 5, 5]
for i in my_list:
    print(i, end=" ")

for i in range(len(my_list)):
    print(my_list[i])

for i, elem in enumerate(my_list):
    print(f"Element at position {i} = {elem}")

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# listelerde values = my_list yapsan ve sadece values u degistirsen ikisi de degisiyo

# liste.insert(pozisyon, eleman)

friends = ["Harry","Emily", "John", "Jimmy"]
print(friends.index("Emily"))

friends.pop(len(friends)-1)
print(friends)
