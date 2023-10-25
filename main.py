import sqlite3

#create a database
conn = sqlite3.connect('todolist.db')
c = conn.cursor()

def create_t():  #create a table in the database
    c.execute("""CREATE TABLE IF NOT EXISTS listss
        (
            id INTEGER PRIMARY KEY,
            tasks TEXT,
            comp INTEGER
        )
   """)
    print("Table created")
    conn.commit()


def add_task(task):
    c.execute("INSERT INTO listss (tasks, comp) VALUES (?, ?)", (task, 0))
    conn.commit()

def deletetask(tasksid):
    c.execute("DELETE FROM listss WHERE id = ?", (tasksid,))
    conn.commit()

def comp(tasksid):
    c.execute("UPDATE listss SET comp = 1 WHERE id = ?", (tasksid,))
    conn.commit()
pass

def display():
    c.execute("SELECT * FROM listss")
    tasks = c.fetchall()

    print("TO-DO list:")
    for task in tasks:
        # Check if the task is completed (task[2] is 1), and use a checkmark (✔️)
        # if the task is not completed (task[2] is 0), use a cross (❌)
        if task[2] == 1:
            status = "✔️"
        else:
            status = "❌"
        # Print the bullet point (•), status (✔️ or ❌), and the task description (task[1])
        print(f"•{task[0]} {status} {task[1]}")

create_t()

while True:
    print("--------------------------")
    print(".........Options........")
    print("--------------------------")
    print("1. ADD TASK")
    print("2. MARK COMPLETED")
    print("3. DELETE THE TASK")
    print("4. DISPLAY")
    print("5. EXIT")
    print("--------------------------")

    choice = int(input("ENTER YOUR CHOICE: "))

    print("--------------------------")

    if choice == 1:
        tasks = input("Enter your task: ")
        add_task(tasks)
        print(f"Added: {tasks}")
        print("--------------------------")
    elif choice == 2:
        display()
        task_id = int(input("Enter the task number to mark as completed: "))
        comp(task_id)
        display()
        print("--------------------------")
    elif choice == 3:
        display()
        task_id = int(input("Enter the task number to delete: "))
        deletetask(task_id)
        display()
        print(f"list deleted",task_id)
        print("--------------------------")
    elif choice == 4:
        display()
        print("--------------------------")
    elif choice == 5:
        print("YA you done!")
        print("--------------------------")
        conn.close()
        break
    else:
        print("Invalid choice. Please select a valid option.")
