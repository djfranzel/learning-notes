
import sys
import os
import uuid

# todo list program, stores data to todo_list.txt

class todo_list():

    file_name = 'todo_list.txt'

    def __init__(self):
        self.welcome_message()

    def welcome_message(self):

        choice = input('''  
== TODO LIST ==
[1] show tasks
[2] add task
[3] complete task
[4] exit
Your choice: ''')
        if not choice in ['1','2','3','4']:
            print('Invalid entry')
            self.welcome_message()

        if choice == '1':
            self.show_tasks()
        elif choice == '2':
            self.add_task()
        elif choice == '3':
            self.complete_task()
        elif choice == '4':
            sys.exit()

    def show_tasks(self):
        print('[YOUR TASKS]')
        if self.check_if_empty():
            print('Empty list')
        else:
            print(open(self.file_name, 'r+').read())
        self.welcome_message()

    def add_task(self):
        print('[ADD TASK]')
        task = input('What is the task? ')
        deadline = input('What is the deadline? ')
        id = str(uuid.uuid1())
        try:
            stream = open(self.file_name, 'a')
            stream.write(id+' | '+task+' | '+deadline+'\n')
        except Exception as e:
            print(e)
        stream.close()
        self.show_tasks()
        

    def complete_task(self):
        print('[COMPLETE TASK]')
        print(open(self.file_name).read())

        if self.check_if_empty():
            print('Empty list\n')
            print('No tasks to complete')
            self.welcome_message()
        
        id = input('Enter id to complete: ')
        if self.valid_id(id):
            with open(self.file_name, "r") as f:
                lines = f.readlines()
            with open(self.file_name, 'w') as file:
                for line in lines:
                    if not id in line:
                        file.write(line)
        else:
            print('Invalid entry')
        self.welcome_message()
    
    def check_if_empty(self):
        return os.stat(self.file_name).st_size == 0

    def valid_id(self, id):
        stream = open(self.file_name)
        for line in stream.readlines():
            if line.split()[0] == id:
                return True
        return False


if __name__ == '__main__':
    todo_list()