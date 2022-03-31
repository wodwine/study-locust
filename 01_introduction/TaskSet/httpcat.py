from locust import TaskSet, constant, task, HttpUser


class MyHTTPCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get status of 200")


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    wait_time = constant(1)
