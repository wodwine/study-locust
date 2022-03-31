from locust import User, task, constant


# 1. Introduction to Locust

class MyFirstTest(User):
    weight = 2
    wait_time = constant(1)

    @task
    def launch(self):
        print("Launching the URL")

    @task
    def search(self):
        print("Searching...")


class MySecondTest(User):
    weight = 2
    wait_time = constant(1)

    @task
    def launch(self):
        print("Launching the second URL")

    @task
    def search(self):
        print("Searching for second...")

# locust -f 01_introduction/Task/app.py
