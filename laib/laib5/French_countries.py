def main():
    country = input("Enter a country name in French: ")
    answer = article(country)
def article(country):
    country = country.lower()
    if country[0] in "aeiou":
        print("l'" + " " + country)
    elif country == "belize" or country == "cambodge" or country == "mexique" or country == "mozambique" or country == "zaïre" or country == "zimbabwe":
        print("le" + " " + country)
    elif country == "etats-unis" or country == "Pays-Bas":
        print("les" + " " + country)
    elif [-1] == "a":
        print("le" + " " + country)
    elif [-1] == "e":
        print("la" + " " + country)


main()