n = int(input("Enter the number: "))


for row in range(0,n):
    a = ""
    for col in range(0,n):
        a += "*"
    print(a)
print(" ")

# Upper half
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

# Lower half
for i in range(n - 1, 0, -1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)


    


    
    

    
