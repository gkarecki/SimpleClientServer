import socket
import json

def showTasks():
    print("Showing tasks list")
    with open("task_list.json") as json_data:
        data = json.load(json_data)
    return data

def addTask(taskDesc, taskPriority):
    print("Adding task")
    with open("task_list.json") as json_data:
        data = json.load(json_data)

    global_ID = data["global_id"]
    self = ""
    seq = ("task", str(global_ID))
    name = self.join(seq)

    data[name] = {}
    data[name]={"id" : global_ID, "description": taskDesc, "priority": taskPriority}
    data["global_id"] = global_ID + 1

    with open("task_list.json", 'w') as json_data:
        json.dump(data, json_data)

    self = ""
    seq = ("Task added with ID: ", str(global_ID))
    return self.join(seq)

def deleteTask(taskID):
    print("Deleting task")
    with open("task_list.json") as json_data:
        data = json.load(json_data)

    self = ""
    seq = ("task", str(taskID))
    name = self.join(seq)

    try:
        del data[name]
    except KeyError:
        print("Key doesn't exist")
        return "Wrong ID!"

    with open("task_list.json", 'w') as json_data:
        json.dump(data, json_data)

    return "Task deleted"

def showTaskPrior():
    print("Showing tasks list with priority")
    with open("task_list.json") as json_data:
        data = json.load(json_data)

    i = 0
    for x in data:
        if i == 0:
            i += 1
            continue
        if (data[x]["priority"] == int(id)):
            output = str(data[x]["id"]) + "\t" + data[x]["description"] + "\t" + str(data[x]["priority"])

    return output

def msgFormat(arg, taskDesc, taskPriority, taskID):
    if(arg == 1):
        return showTasks()
    elif (arg == 2):
        return addTask(taskDesc, taskPriority)
    elif (arg == 3):
        return deleteTask(taskID)
    elif (arg == 4):
        return showTaskPrior()
    else:
        return "ERROR"

def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(("localhost", 8888))
    serv.listen(1)
    return serv

stillListen = True
while stillListen:
    client, addr = server().accept()
    print("Connected with", addr)

    clientMsg = client.recv(64).decode()

    print("Client msg: ", clientMsg)
    if (clientMsg == "EndOfData"):
        client.close()
        stillListen = False
        print()
    else:
        clientMsg = clientMsg.split(".")

        i = 0
        functionNumber = -1
        taskDesc = ""
        taskPriority = -1
        taskID = -1
        for x in clientMsg:
            if(i == 0):
                functionNumber = int(x)
            if (i == 1):
                taskDesc = x
            if (i == 2):
                taskPriority = int(x)
            if (i == 3):
                taskID = int(x)
            i += 1

        client.send(str(msgFormat(functionNumber, taskDesc, taskPriority, taskID)).encode())
        client.close()
        print()