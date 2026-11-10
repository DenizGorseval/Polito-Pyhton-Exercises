friends = ["Alice", "Carl", "Bob", "Andrew"]
nums = [4, 3, 7, 9, 5, -2]

friends.sort() #this changes the list in hand 

friends_sortedrev = sorted(friends, reverse=True) #this assigns a new list 
friends_sorted = sorted(friends)

nums2 = nums #this assigns a new reference for the same list
nums2 = nums[:] #this creates a new list

print(nums.count(9)) # tells how many tmes the number occurs in the list