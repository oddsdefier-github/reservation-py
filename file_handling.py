import sys

filename = "reservation.txt"


def make_reservation():
    name = input("Enter your name: ").lower().title()
    for i in name:
        if i.isdigit():
            sys.exit("Enter non-numeric characters!")
    num_adults = input("Number of adults: ")
    for j in num_adults:
        if j.isalpha():
            sys.exit("Enter non-alphabet characters!")
    num_children = input("Number of children: ")
    for k in num_children:
        if k.isalpha():
            sys.exit("Enter non-alphabet characters!")

    input_date = input("Date: ").lower().title()
    input_time = input("Time: ")

    with open(filename, "a") as file:
        file.write(f'{name},{input_date},{input_time},{num_adults},{num_children}\n')
        print(f"Reservation Added Successfully!")
        sys.exit()


def view_reservation():
    with open(filename, "r") as file:
        line = "true"
        counter = 0
        while line:
            line = file.readline()
            if line == "":
                break
            line_text = line.split(",", 5)
            counter += 1

            print(f' Reservation ID: {counter}')
            print(f' Name: {line_text[0]}')
            print(f' Date: {line_text[1]}')
            print(f' Time: {line_text[2]}')
            print(f' Adults: {line_text[3]}')
            print(f' Children: {line_text[4]}')
            print("+----------------------------+")


def del_reservation():
    view_reservation()
    del_id = int(input("Enter ID to Delete: "))
    with open(filename, "r") as file:
        lines = file.readlines()

        if 1 <= del_id <= len(lines):
            del lines[del_id - 1]

        with open(filename, "w") as file_1:
            file_1.writelines(lines)
            sys.exit(f"Deleted Successfully! Reservation No. {del_id} was removed completely.")


def generate_reports():
    adult_fees = 500
    children_fees = 300
    with open(filename, "r") as file:

        lines = file.readlines()

        sum_children = 0
        sum_adults = 0
        for line in lines:
            line_data = line.strip().split(",")

            children = ''.join(line_data[-1:])
            children = int(children)
            sum_children += children

            adults = ''.join(line_data[-2])
            adults = int(adults)
            sum_adults += adults

        children_fees = sum_children * children_fees
        adult_fees = sum_adults * adult_fees
        grand_total = children_fees + adult_fees

        view_reservation()
        print("------------------------------")
        print("REPORT".center(30))
        print("------------------------------")
        print(f"Total number of Adults: {sum_adults}")
        print(f"Total number of Kids: {sum_children}")
        print(f'Grand Total: PHP {grand_total}')
        print("------------------------------")

