#!/usr/bin/python3
"""
Write a script that hits a REST api that has data on employees and tasks
and filters the data based on an argument passed to the script.
The argument is the employee ID, and the output should display the employee
name and the tasks the employee completed.
"""
import requests
import sys

if __name__ == "__main__":
    ID = sys.argv[1]
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(ID)).json().get("name")
    total_tasks = 0
    done_tasks = []
    r = requests.get("http://jsonplaceholder.typicode.com/todos").json()

    for task in r:
        if (task.get("userId") == int(ID)):
            total_tasks += 1
            if (task.get("completed")):
                done_tasks.append(task.get("title"))           
    print("Employee {} is done with tasks({:d}/{:d}):"
          .format(response, len(done_tasks), total_tasks))
    for item in done_tasks:
        print("\t {}".format(item))
