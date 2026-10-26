import statistics

def display_main_menu():
    print("Enter some numbers separated by commas: ")
    return

def get_user_input():
   numInp = input ()
   numList = numInp.split (",")
   float_list = list(map(float, numList))
   return float_list

def calc_average(temp_list):
    total = sum(temp_list)
    count = len(temp_list)
    avg_temp = (total / count,2)
    return avg_temp

def find_min_max(temp_list):
    min_max_list =  [min(temp_list), max(temp_list)]
    return min_max_list 


def sort_temperature(temp_list):
    return sorted(temp_list)


def calc_median_temperature(temp_list):
    return statistics.median(temp_list)


def main():
    display_main_menu()
    temp_list = get_user_input()
    avg_temp = calc_average(temp_list)
    print("The average temperature ", avg_temp)
    min_max_list= find_min_max(temp_list)
    print("The min temp", min_max_list[0])
    print("The min temp", min_max_list[1])
    sorted_lsit = sort_temperature(temp_list)
    median_val = calc_median_temperature(temp_list)
    print("The median", median_val)