#!/usr/bin/python3
"""
Extend the python script from exercise 0 to export data in CSV format.
Record all tasks that are owned by the employee.
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import csv
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
            temp = []
            temp.extend((ID,
                         username,
                         task.get("completed"),
                         task.get("title")))
            all_tasks.append(temp)

    with open("{}.csv".format(ID), 'w+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(all_tasks)
