import statistics


def display_main_menu():
    print("Enter temperature value with comma in between (eg. 5, 6, 7) :")

def get_user_input():
    number = input()
    num_list = number.split(", ")
    #print(num_list)
    float_numlist = []
    for item in num_list:
        float_numlist.append(float(item))
    #print(float_numlist)
    return float_numlist

def calc_average_temperature ():

    average = sum(list)/len(list) # len is to take the amt of array
    print ("the average : ")
    print(average)

def calc_minmax_temperature():
    x = max(list)
    y = min(list)
    print("the max : ")
    print ( x )
    print("the min : ")
    print(y)

def temperature_sort():
    tempsort = sorted(list)
    print("Sort temperature from min to max : ")
    print(tempsort)
    return tempsort

def calc_median_temperature():
    z = statistics.median(tempsort)
    print ("The temperature Median is : ")
    print(z)

display_main_menu()
list = get_user_input()
calc_average_temperature()
calc_minmax_temperature()
tempsort = temperature_sort()
calc_median_temperature()