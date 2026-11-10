from math import ceil

def bar_charts(num_list):
    star_list = []
    the_range = max(num_list)
    if min(num_list) < 0:
        the_range += abs(min(num_list))

    if the_range <= 40:
        star_value = ceil(40/the_range)
    else:
        star_value = ceil(the_range/40)

    for i in num_list:
        if i == the_range:
            star_list.append(40)
        else:
            star_list.append(star_value*i)

    return star_list



def main(): 
    int_list = []
    countries = []

    country = input("Enter a country name: ")
    num_of_stars = input("Enter the number of asteriks: ")

    while num_of_stars != "" and country != "":
        
        int_list.append(int(num_of_stars))
        countries.append(country)
        country = input("Enter a country name: ")
        num_of_stars = input("Enter the number of asteriks: ")
       
    chart = bar_charts(int_list)

    for i in range(len(chart)):
        print(countries[i], chart[i] * "*")
    
    

    
main()