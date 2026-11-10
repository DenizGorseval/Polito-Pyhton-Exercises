n = int(input("What is the triangle size? "))

#row = 0
#while row < n:
 #   col = 0
  #  while col < (row+1):
   #     print("*", end="")
    #    col += 1
    #print()
    #row += 1

for row in range(0,n):
    for col in range(0,(2*(row+1))):
        print("*", end="")
    print()
