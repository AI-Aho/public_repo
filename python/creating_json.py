#! /usr/bin/python3

import os
import json

def main():
    '''This file creates and edits projects in the folder called projects'''
    print("hello world")

    #Check if diretory exists and if not then create it
    dir_path = "./projects"
    
    check_dir = os.path.isdir(dir_path)

    if check_dir == False:
        os.mkdir(dir_path)

    else:
        None

    # Asking what user wants to do, check current projects, check all projects, create new project.
    while True:
        user_ask = input("What do you want to do? 1. check all projects, 2. Check current projects, 3. create a new project, 4. check and update project budget")
        whole_project_count = 0
        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, path)):
                whole_project_count += 1

        if user_ask == "1":
            project_count = 0
            #Check a file for number of how many projects have been created. Then use that to loop trough the project files.
            #file_path = "./animal.py"
            #check_file = os.path.isfile(file_path)
            #print(check_file)

            print("searching all projects:")

            #Go through all projects
            for path in os.listdir(dir_path):
                if os.path.isfile(os.path.join(dir_path, path)):
                    project_count += 1
                    with open(f"./projects/project{project_count}.json") as f:
                        data = f.read()
                        js = json.loads(data)
                        #print("Data type after reconstruction : ", type(js))
                        print(js["project"])

            break

        elif user_ask == "2":
            print("searching current projects:")

            current_project_count = 1
            for path in os.listdir(dir_path):
                if os.path.isfile(os.path.join(dir_path, path)):
                    with open(f"./projects/project{current_project_count}.json") as f:
                        data = f.read()
                        js = json.loads(data)
                        #print("Data type after reconstruction : ", type(js))
                        if js["current_budget"] > 0:
                            print(js["project"])
                            current_project_count += 1
            break

        elif user_ask == "3":
            the_project = {}

            print("You chose to create a new project")

            # Ask questions to create a new project
            project_name = input("What will be the project name?")

            while True:
                try:
                    total_budget = int(input("What will be the projects budget?"))
                    break
                
                except ValueError:
                    print("Try again and give a number")
                    continue

            if total_budget < 0:
                status = "active"

            else:
                status = "inactive"

            the_project.update({"project": project_name})
            the_project.update({"status": status})
            the_project.update({"total_budget": total_budget})
            the_project.update({"current_budget": total_budget})
            print(the_project)

            # Add employees
            print("Next you will be adding employees to your project!")

            employees = {}
            emp_count = 1

            while True:
                current_employee = {}
                emp_name = input("Enter employees name: ")
                while True:
                    try:
                        emp_salary = int(input("Enter employees salary: "))
                        break
                    
                    except ValueError:
                        print("Try again and give a number")
                        continue

                emp_position = input("Enter employees position: ")

                current_employee.update({"name": emp_name})
                current_employee.update({"salary": emp_salary})
                current_employee.update({"position": emp_position})

                more_emp = input("Do you want to add another employee, yes or no?")
                
                employees[f"employee{emp_count}"] = current_employee
                emp_count += 1
                #print(employees)

                if more_emp == "yes":
                    continue

                elif more_emp == "no":
                    break

            the_project["Employees"] = employees
            #print(the_project)

            json_project = json.dumps(the_project)

            # Make a file for the project and save things in it.
            f = open(f"./projects/project{whole_project_count+1}.json", "w")
            f.write(f"{json_project}")
            f.close()

            #open and read the file after the appending:
            f = open(f"./projects/project{whole_project_count+1}.json", "r")
            print(f.read())


            break

        elif user_ask == "4":
            print("You chose to check / update an existing project")
            search_project = input("What project are you looking for?")

            search_count = 0

            editing_project = "no_project"

            for path in os.listdir(dir_path):
                if os.path.isfile(os.path.join(dir_path, path)):
                    search_count += 1
                    with open(f"./projects/project{search_count}.json") as f:
                        data = f.read()
                        js = json.loads(data)
                        #print("Data type after reconstruction : ", type(js))
                        #print(js["name"])

                        if (js["project"]) == search_project:
                            editing_project = data
                            break

                        else:
                            continue
            
            if editing_project == "no_project":
                print("Could not find project with that name")
                break

            else:
                print("Found project!:")

            print(editing_project)
            print("---")
            print("Current budget:")
            print((js["current_budget"]))
            
            while True:
                try:
                    new_budget = int(input("Enter new budget: "))
                    break

                except ValueError:
                    print("Must be a number")
                    continue
            
            
            js["current_budget"] = new_budget


            
            json_project = json.dumps(js)

            f = open(f"./projects/project{search_count}.json", "w")
            f.write(f"{json_project}")
            f.close()

            break

        else:
            print("Try again")
            continue



if __name__ == "__main__":
    main()