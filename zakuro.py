import sys
import argparse
import pickle
import random

# list tasks
# do tasks
# add a task
# change task
# delete a task
# delete all tasks

def main():
    try:
        with open("tasks.pkl", "rb") as f:
            unweighted_tasks = pickle.load(f)
            weighted_tasks = pickle.load(f)
    except:
        unweighted_tasks = []
        weighted_tasks = []

    while True:
        menu_choice = input("Please select an option:\n" \
                        "1. View list of tasks\n" \
                        "2. Add a task\n" \
                        "3. Delete a task\n" \
                        "4. Delete all tasks\n" \
                        "5. Do tasks\n" \
                        "Press q to exit\n"
                        )
        if menu_choice == "1":
            list_tasks(unweighted_tasks)
        elif menu_choice == "2":
            weighted_tasks = add_task(unweighted_tasks)
            write_pickle(unweighted_tasks, weighted_tasks)
        elif menu_choice == "3":
            weighted_tasks = delete_task(unweighted_tasks)
            write_pickle(unweighted_tasks, weighted_tasks)
        elif menu_choice == "4":
            unweighted_tasks, weighted_tasks = delete_all_tasks(unweighted_tasks, weighted_tasks)
            write_pickle(unweighted_tasks, weighted_tasks)
        elif menu_choice == "5":
            do_tasks(unweighted_tasks, weighted_tasks)
        elif menu_choice == "q":
            write_pickle(unweighted_tasks, weighted_tasks)
            sys.exit(0)

def write_pickle(unweighted_tasks, weighted_tasks):
    with open("tasks.pkl", "wb") as f:
        pickle.dump(unweighted_tasks, f)
        pickle.dump(weighted_tasks, f)

def list_tasks(unweighted_tasks):
    if not unweighted_tasks:
        print("\nNo tasks in list.\n")
    for i, pair in enumerate(unweighted_tasks):
        print(f"{i+1}. Task Name: {pair[0]} Task Priority: {pair[1]}\n")

def add_task(unweighted_tasks):
    task_name = input("What is the name of your task? ")
    while True:
        try:
            task_priority = int(
                input("What is your task's priority? Please enter a number (the higher, the more important): ")
            )
            break
        except:
            print("Please enter a number!")

    task_tuple = (task_name, task_priority)
    unweighted_tasks.append(task_tuple)
    weighted_tasks = generate_weighted_tasks(unweighted_tasks)
    return weighted_tasks

def delete_task(unweighted_tasks):
    weighted_tasks = []
    if not unweighted_tasks:
        print("\nNo tasks in list.\n")
        return weighted_tasks
    for i, pair in enumerate(unweighted_tasks):
        print(f"{i+1}. Task Name: {pair[0]} Task Priority: {pair[1]}")
    while True:
        delete = input("Please enter the number of the task you wish to delete or press q to return to main menu: ")
        if delete == 'q':
            break
        try:
            delete_int = int(delete)
            del unweighted_tasks[delete_int - 1]
            break
        except:
            print("Please enter a number\n")
    weighted_tasks = generate_weighted_tasks(unweighted_tasks)
    return weighted_tasks

def delete_all_tasks(unweighted_tasks, weighted_tasks):
    confirm = input("Are you sure you want to delete all tasks? Y/N\n")
    if confirm == "Y":
        return [], []
    else:
        return unweighted_tasks, weighted_tasks


def do_tasks(unweighted_tasks, weighted_tasks):
    if not unweighted_tasks:
        print("\nNo tasks in list.\n")
    print("Press Enter to go to next task. Type q and press Enter to return to main menu.\n")
    while True:
        keypress = input(f"{random.choice(weighted_tasks)} ")
        if keypress == "q":
            break

def generate_weighted_tasks(unweighted_tasks):
    weighted_tasks = []
    for item, weight in unweighted_tasks:
        weighted_tasks.extend([item] * weight)
    return weighted_tasks


if __name__ == "__main__":
    main()
