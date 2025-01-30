import sys #CLI
import os  #manipulating files
import json #json files
from datetime import datetime 

file_name = "file.json"

#check if the file already exists, if not create a new one
if not os.path.exists(file_name):
    with open(file_name, 'w') as file:
        json.dump([], file)
        
def addTask(describtion):
    with open(file_name, 'r') as file:
        tasks = json.load(file)
    
    new_task = {
        "ID": len(tasks) + 1,
        "Describtion": describtion,
        "Status": "todo",
        "CreatedAt": datetime.now().isoformat(),
        "UpdatedAt": datetime.now().isoformat()
    }
    
    tasks.append(new_task)
    
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)
        
    print(f"Data success at (id:{new_task['ID']}, date:{new_task['CreatedAt']})")
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
       print("Usage: mina <Command> [Option]")
       sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "add":
        describtion = " ".join(sys.argv[2:])
        addTask(describtion)
    else:
        print("Unknown Command")