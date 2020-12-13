# ------------------------------------------------------------------------ #
# Title: Main.py
# Description: Working with Modules
# Version: 3.9
# ChangeLog (Who,When,What):
#   RRoot,1.1.2030,Created started script
#   RRoot,1.1.2030,Added pseudo-code to start assignment 9
#   e4ster, 12.12.2020, Modified code to complete assignment 9
# ------------------------------------------------------------------------ #


if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from ProcessingClasses import DatabaseProcessor as Dp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")


# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable = []
for line in lstFileData:
    lstTable.append(Emp(line[0].strip(), line[1].strip(), line[2].strip()))

while True:

    # Show user a menu of options
    Eio.print_menu_items()

    # Get user's menu option choice
    choice = Eio.input_menu_options()

    # Show user current data in the list of employee objects
    if choice.strip() == '1':
        for each_object in lstTable:
            print(each_object)
        continue

    # Let user add data to the list of employee objects
    elif choice.strip() == '2':
        new_obj = Eio.input_employee_data()
        Dp.add_data_to_list(new_obj, lstTable)
        continue

    # let user save current data to file
    elif choice.strip() == '3':
        Fp.save_data_to_file("EmployeeData.txt", lstTable)
        print("Data has been saved.")
        continue

    # Let user exit program
    elif choice.strip() == '4':
        if input("Are you sure you want to exit? y/n: ").lower() == "y":
            break
        else:
            continue

    else:
        print("That's not an option, try again!")
