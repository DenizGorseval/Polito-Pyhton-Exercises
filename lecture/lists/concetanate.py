friends = ["Bob", "alice", "Carl"]
"""
cat_str = ""
for i in range(len(friends)):
    if i > 0:
        cat_str = cat_str + ","
    cat_str = cat_str + friends[i]
    """

cat_str = ",".join(friends)

print(cat_str)