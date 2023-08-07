from functions import get_todos, write_todos
import time

# modules taught csv, glob, webbrowser, shutil

now = time.strftime("%b %d %Y %H:%M:%S")

print('It is', now)

while True:
    user_action = input('Type add, show, edit or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]+'\n'

        todos = get_todos()
        todos.append(todo)

        write_todos(todos)

    elif user_action == 'show':
        todos = get_todos()
        for index, item in enumerate(todos):
            print(f'{index+1}-{item.strip()}')
    elif user_action.startswith('edit'):
        try:
            slc = get_todos()
            le = int(user_action[5:])-1
            edt = input('enter word to replace with: ')+'\n'
            slc[le] = edt
            write_todos(slc)
        except IndexError:
            print('There is no such index, please enter another number')
            continue
    elif user_action.startswith('remove'):
        try:
            usr = int(user_action[7:]) - 1
            sl = get_todos()
            pl = sl.pop(usr)
            print(f'{pl} has been removed')
            write_todos(sl)
        except ValueError:
            print("Enter index number only")
            continue
    elif user_action == 'exit':
        break
    else:
        print('Unknown Command')
        continue
