import socket
import ast


def sendData(data, functionNumber, id):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8888))
    s.send(str(data).encode())

    message = s.recv(1024)
    s.close()

    if(functionNumber == 1):
        data = ast.literal_eval(message.decode()) # ast.literal_eval raises an exception
        # if the input isn't a valid Python datatype, so the code won't be executed
        # if it's not.
        print("ID \t DESCRIPTION \t Priority")

        i=0
        for x in data:
            if i == 0:
                i += 1
                continue
            print(str(data[x]["id"]) + "\t" + data[x]["description"] + "\t" + str(data[x]["priority"]))
    elif functionNumber == 4:
        data = ast.literal_eval(message.decode())
        print("ID" + "\t" + "DESCRIPTION" + "\t" + "PRIORITY")

        i=0
        for x in data:
            if i == 0:
                i += 1
                continue
            if (data[x]["priority"] == int(id)):
                print(str(data[x]["id"]) + "\t" + data[x]["description"] + "\t" + str(data[x]["priority"]))
    else:
        print(message.decode())


def closeServ():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8888))
    s.send("EndOfData".encode())
    s.close()

functionNumber = -1
taskDscp = ""
taskPrio = -1
taskID = -1

while functionNumber != 0:
    print("1 - Show tasks")
    print("2 - Add task")
    print("3 - Delete task")
    print("4 - Show tasks with priority")
    print("0 - Exit")

    functionNumber = input("Select option: ")
    if (functionNumber.isnumeric()):
        functionNumber = int(functionNumber)
    else:
        print("Option must be a number! /n")
        continue
    if (functionNumber < 0 or functionNumber > 4):
        print("Incorrect option! /n")
        continue
    elif (functionNumber == 2):
        taskDscp = input("Type description of the task: ")
        taskPrio = input("Type priority of the task: ")
        if taskPrio.isnumeric() != True:
            print("Priority must be a number! /n")
            continue
        if (taskPrio < "0" or taskPrio > "10"):
            print("Priority must be from 1 to 9")
    elif (functionNumber == 3):
        taskID = input("Type ID to delete: ")
        if taskID.isnumeric() != True:
            print("ID must be a number! /n")
            continue
    elif (functionNumber == 4):
        id = input("Type priority: ")

    if (functionNumber != 0):
        self = "."
        seq = (str(functionNumber), taskDscp, str(taskPrio), str(taskID))
        sendData(self.join(seq), functionNumber, id)
        print()
    if (functionNumber == 0):
        closeServ()