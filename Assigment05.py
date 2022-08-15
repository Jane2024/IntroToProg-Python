# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# MBruce,08/07/2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None              # An object that represents a file
strFile = "ToDoList.txt"    # Data storage file
dicRow = {}                 # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []               # A list that acts as a 'table' of rows
strChoice = ""              # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code

objFile = open(strFile, "r")                                            # Opens "ToDolist.txt" for reading
for row in objFile:                                                     # Loops through each row in the ToDoList.txt
    task, priority = row.split(",")                                     # Unpacks and separates items via "," into "task" and "priority" variables
    dicRow = {"TaskValue": task, "PriorityValue": priority.strip()}     # creates a dictionary row of data
    lstTable.append(dicRow)                                             # adds row of data to list "lstTable"
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)

    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
                                                                                            # If we are here, user chose to show current list items
        print("Here is the current list of Tasks and their Priority in the ToDo list :")    # Print list header
        print()                                                                             # adding spacer line
        for row in lstTable:                                                                # Loop through rows in list
            print(row["TaskValue"] + "....." + row["PriorityValue"])                        # Print each dictionary object's task and priority
        print("=" * 35)                                                                     # Simple separator for aesthetic purposes

        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
                                                                                                    # If we are here, user wants to enter more tasks
        while(True):                                                                                # Start of loop while user wants to enter more tasks
            strTask = input("Please input a new task name:")                                        # Prompt user for new task- assign to string "strTask"
            strPriority = input("Please input its priority:")                                       # Prompt user for priority- assign to string "strPriority"
            lstTable.append({"TaskValue": strTask, "PriorityValue": strPriority})                   # Add it to the current task list of dictionary objects- "lstTable"

            strUserAction = input("Do you want to enter another task? Please enter 'y' or 'n':")    # Prompt user if they are done- assign response to string "strUserAction"
            if strUserAction.lower() == "n":                                                        # If they are done - exit loop, else it will prompt for another task
                break

        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here

        strRemoveTask = input("Enter name of task you want to remove?")                             # Prompt user for task to be removed

        lst_of_all_values = [value for elem in lstTable for value in elem.values()]                 # Utilized list comprehension to get all the TaskValues to help check if entered task was part of the list
        if strRemoveTask not in lst_of_all_values:                                                  # If this evaluates to true (task not in list), then notify user
            print("That task is not in current list. Here is the current list:")
            print()                                                                                 # Adding spacer row
            for row in lstTable:
                print(row["TaskValue"] + "....." + row["PriorityValue"])                            # Reprint list of Tasks and their Priorities for the user

        else:
            for row in lstTable:                                                                    # Loop through lstTable to find task match
                if row["TaskValue"].lower() == strRemoveTask.lower():                               # Check for match
                    lstTable.remove(row)                                                            # When match is found, Remove task
                    print(strRemoveTask + " has been removed")                                      # Inform user task is removed

        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here

        print("Here is the current list of tasks and priorities that will be saved to file " + strFile + ":")
        print()
        for row in lstTable:
            print(row["TaskValue"] + "....." + row["PriorityValue"])                                                    # Show list of Tasks and their Priorities that will be saved
        print("=" * 35)                                                                                                 # Simple separator for aesthetic purposes


        strChoice = str(input("Do you still want to save this data to the file? Please enter 'y' or 'n':")).lower()     # Prompt user if they still want to save after seeing current list
        if strChoice == "y":                                                                                            # Check for "y" response
            objFile = open(strFile, "w")                                                                                # Open file ToDoList.txt for write
            for dicRow in lstTable:                                                                                     # Loop through dictionary objects in list table
                objFile.write(dicRow["TaskValue"] + "," + dicRow["PriorityValue"] + "\n")                               # Write each one to file
            objFile.close()
            input("Data has been saved to ToDoList.txt. Press the [Enter] key to return to menu.")      # Inform user it has been saved and return to main menu
        else:
            input("No new data was saved to ToDoList.txt. Press the [Enter] key to return to menu.")    # Inform user No save was done and return to main menu
        continue


    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here

        print("Exiting program. Goodbye")                                                               # Inform user program is exiting

        break  # and Exit the program
