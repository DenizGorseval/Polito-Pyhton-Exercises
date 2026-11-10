def shiftList(num_list):
    output_list = []
    temp = num_list[-1]
    for i in range(len(num_list)):
      output_list.append(temp)
      temp = num_list[i]
    return output_list


def main():
    num = input("Enter a number: ")
    input_list = list()
    while num != "":
        input_list.append(num)
        num = input("Enter a number: ")
    i = 0
    output_list = shiftList(input_list)
    print(output_list)
    while i < (len(input_list)-1):

        output_list = shiftList(output_list)
        print(output_list)
        i += 1

main()