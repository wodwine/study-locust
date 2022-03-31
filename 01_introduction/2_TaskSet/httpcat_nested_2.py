from locust import TaskSet, constant, task, HttpUser


# 5. Use Locust to test with the nested 2_TaskSet

class MyHTTPCat(TaskSet):

    @task
    def get_200_status(self):
        self.client.get("/200")
        print("Get status of 200")
        self.interrupt(reschedule=False)


class MyAnotherHTTPCat(TaskSet):

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Get status of 500")
        self.interrupt(reschedule=False)


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHTTPCat, MyAnotherHTTPCat]
    wait_time = constant(1)

# locust -f 01_introduction/2_TaskSet/httpcat_nested_2.py
