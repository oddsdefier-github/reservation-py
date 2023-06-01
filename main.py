import file_handling
import sys

print("------------------------------")
print("System Menu".center(30))
print("------------------------------\n")
print("a. View all Reservations")
print("b. Make Reservation")
print("c. Delete Reservation")
print("d. Generate Report")
print("e. Exit")
print("\n------------------------------\n")


user_select = input("Select: ").lower()
print("------------------------------\n")

if user_select == "b":
    file_handling.make_reservation()
elif user_select == "a":
    file_handling.view_reservation()
elif user_select == "c":
    file_handling.del_reservation()
elif user_select == "d":
    file_handling.generate_reports()
elif user_select == "e":
    sys.exit("Thank You!")
else:
    print("Invalid Selection")
