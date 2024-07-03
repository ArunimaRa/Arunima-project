# A simple to-do list application.

todo_list = []

def add_item(item):
  todo_list.append(item)

def remove_item(item):
  todo_list.remove(item)

def show_list():
  for item in todo_list:
    print(item)

while True:
  print("1. Add item")
  print("2. Remove item")
  print("3. Print list")
  print("4. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    item = input("Enter the item to add: ")
    add_item(item)
  elif choice == "2":
    item = input("Enter the item to remove: ")
    remove_item(item)
  elif choice == "3":
    show_list()
  elif choice == "4":
    break
  else:
    print("Invalid choice. Please try again.")

print("Exiting program.")