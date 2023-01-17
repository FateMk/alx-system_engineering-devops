#!/usr/bin/python3
"""
Extend the python script from exercise 0 to export data in JSON format.
Record all tasks that are owned by the employee.
Format must be: {"USER_ID": [ {"task": TASK_TITLE,
                               "completed": TASK_COMPLETED_STATUS,
                               "username": USERNAME"},
                               {...}
                            ]
File name must be: USER_ID.json
"""
import json
import requests
import sys

if __name__ == "__main__":
    ID = sys.argv[1]
    username = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                            .format(ID)).json().get("username")
    all_tasks = []
    r = requests.get("http://jsonplaceholder.typicode.com/todos").json()

    for task in r:
        if (task.get("userId") == int(ID)):
            temp = {}
            temp["task"] = task.get("title")
            temp["completed"] = task.get("completed")
            temp["username"] = username
            all_tasks.append(temp)

    with open("{}.json".format(ID), 'w+') as jsonfile:
        json.dump({ID: all_tasks}, jsonfile)
