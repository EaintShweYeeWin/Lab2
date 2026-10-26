def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height ** 2)
    print("BMI = " + str(bmi))
    return bmi


bmi = calculate_bmi(weight=50, height=1.6256)
if bmi < 18.5:
    print("Under Weight")
elif 18.5<= bmi <=25.0:
    print("Normal Weight")
else:
    print("Over Weight")

def display_main_menu():
    print("Display main menu")

def get_user_input():
    print("user input")

def main(): 
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python") 
    display_main_menu() 
    num_list = get_user_input() 
