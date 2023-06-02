import os
import sys
import uuid

empty = '[Your Tasks] is currently empty. There are no tasks to complete.\n'

def fuel_check():
    with open('tasks.txt', 'r') as stream:
        tasks = [line.strip('\n') for line in stream.readlines()]
        if len(tasks) == 0:
            return empty
        else:
            return ['{0}\n'.format(task) for task in tasks]

def main_menu():
    return input('To-Do List\n[1] Show tasks.\n[2] Add a task.\n[3] Complete a task.\n[4] Exit.\nYour choice: ')

def show_tasks():
    print('\n[Your Tasks]')
    try:
        tasks = fuel_check()
        if tasks == empty:
            print(tasks)
        else:
            for task in tasks:
                print(task)
    except Exception as e:
        if e.errno == 2:
            print(empty)
        else:
            print('Something went wrong: {0}'.format(e))
            sys.exit()

def add_task():
    def ask_task():
        return input('\nWhat is the task? ')
    def ask_deadline():
        return input('What is the deadline? ')
    task_identifier = uuid.uuid4()
    task = ask_task()
    deadline = ask_deadline()
    output = '{0} | {1} | {2}'.format(task_identifier.urn.split(':')[2], task, deadline)
    print()
    try:
        with open('tasks.txt', 'a') as stream:
            stream.write(output)
    except Exception as e:
        print('Something went wrong: {0}'.format(e))
        sys.exit()

def complete_task():
    to_be_completed = []
    print('\n[Complete Task]\n[Your Tasks]')
    try:
        tasks = fuel_check()
        if tasks == empty:
            print(tasks)
        else:
            for task in tasks:
                print(task)
            complete = input('Enter the ID to complete: ')
            print()
            for task in tasks:
                if complete not in task:
                    to_be_completed.append(task)
            with open('tasks.txt', 'w') as stream:
                for task in to_be_completed:
                    stream.write(task)
    except Exception as e:
        if e.errno == 2:
            print(empty)
        else:
            print('Something went wrong: {0}'.format(e))

def main():
    choice = ''
    while choice != '4':
        choice = main_menu()
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            sys.exit()
        else:
            print()
            main()

if __name__ == "__main__":
    main()
