#!/usr/bin/env python
# Task Tracker in Command Line Interface
# build json file
# python monttcli.py add new task : mina nady is a programmer
#  ------> [
            # {
            #     'ID': 1,
            #     'Description': "mina is a programmer",
            #     'Status': "Todo",
            #     "Creation Date" 1-2-2000 T 23:34:4552, 
            #     "Modification Date" 1-2-2000 T 23:34:4552 
            # }
            # ]


import sys # CLI
import json # json file
import os # files
from datetime import datetime
jsonFile = "data.json"

if not os.path.exists(jsonFile):
    with open(jsonFile, 'w') as file:
        json.dump([], file)

def addTask(description):
    with open (jsonFile, 'r') as file:
        tasks = json.load(file)
        
    idOfNewTask = len(tasks) + 1
    
    newTask = {
        "ID": idOfNewTask,
        "Status": "in progress",
        "Description": description,
        "Created at": datetime.now().isoformat(),
        "Modified at": datetime.now().isoformat()
    }
    
    tasks.append(newTask)
    
    with open(jsonFile, 'w') as file:
        json.dump(tasks, file, indent=4)
        print(f"Data Success -> ID: {newTask['ID']}, Time:{newTask['Created at']}.")
    
    # except Exception as e:
    #     print(f"Data Failur With Exception {e} -> ID: {newTask['ID']}, Time:{newTask['Created at']}.")
        
def readTask(Id):
    with open(jsonFile, 'r') as file:
        tasks = json.load(file)
        id = int(Id)
        
    if id > len(tasks):
        print("Please enter valid id")
        sys.exit(1)
        
    task = tasks[id-1]
    print(f"ID: {task['ID']:<5}, \nDescription: {task['Description']:<15}, \nStatus: {task['Status']:<5}, \nCreated at: {task['Created at']}, \nModified at: {task['Modified at']}\n")
    
def deleteTask(id):
    with open(jsonFile, 'r') as file:
        tasks = json.load(file)
        
    id = int(id)
   
    for task in tasks:
        if task['ID'] == id:
            tasks.remove(task)
            
    with open(jsonFile, 'w') as file:
        json.dump(tasks, file, indent=4)
        print("Task has been deleted.")
            
def listAll():
    with open(jsonFile, 'r') as file:
        tasks = json.load(file)
        
    print(f"{'ID':<5} {'Description':<15} {'Status':<5}")
    print("-" * 60)
    for task in tasks:
        print(f"{task['ID']:<5} {task['Description']:<15} {task['Status']:<5}")
# python monttcli2.py delete 1
    
def markTask(id, status):
    with open (jsonFile, 'r') as file:
        tasks = json.load(file)
    
    id = int(id)
    
    for task in tasks:
        if task['ID'] == id:
            task['Status'] = status
    
    with open(jsonFile, 'w') as file:
        json.dump(tasks, file, indent=4)
        print("Status Updated!")
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please Enter Valid Equation! (Python minatt.py <Command> Operation)")
        sys.exit(1)
    
    if sys.argv[1] == "add":
        description = " ".join(sys.argv[2:])
        addTask(description)
    elif sys.argv[1] == "read":
        id = sys.argv[2]
        readTask(id)
    elif sys.argv[1] == "delete":
        id = sys.argv[2]
        deleteTask(id)
    elif sys.argv[1] == "update":
        id = sys.argv[2]
        status = sys.argv[3]
        markTask(id, status)
    elif sys.argv[1] == "listall":
        listAll()
    else:
        print("Please Enter Valid Command! (add, delete, update....)")
        