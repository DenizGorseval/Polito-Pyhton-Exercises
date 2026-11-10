import random

def local_maxima(nums):
    extremums = []
    pos_extremum = []
    for i in range(1,len(nums) - 1):
        if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
            extremums.append(nums[i])
            pos_extremum.append(i)
    return extremums, pos_extremum

def rand_list():
    counter = 0
    num_list = []
    while counter < 10:
        num = random.randint(1,100)
        num_list.append(num)
        counter += 1
        num = 0
    return num_list

def ex_print(liste):
    if len(liste) != 0:
        print("These are the local extremums:")
        print(*liste, sep=", ")
    else:
        print("There are no local maxima")

def main():
   nums = rand_list()
   maxima_list, positions = local_maxima(nums)
   printer = ex_print(maxima_list)

   min_distance = float('inf')
   best_i = None
   if len(maxima_list) >= 2:
       for i in range(len(positions)-1):
           distance = positions[i+1] - positions[i]
           if distance < min_distance:
               min_distance = distance
               best_i = i
       if best_i is not None:
           print(f"The extremums that are the closest are {maxima_list[best_i]}, {maxima_list[best_i+1]}")
   
   print(maxima_list)

main()
