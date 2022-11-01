def main():
    display_main_menu()
    num_list = get_user_input()


def display_main_menu():
    print("Enter value with commas (eg. 5,6,7):")
    return (get_user_input())

#display_main_menu()

def get_user_input():
    number = input()
    num_list = number.split()
    print(num_list)
    return (display_main_menu())

#get_user_input()

if __name__ == "__main__":
    main()