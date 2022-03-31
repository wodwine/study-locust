from locust import TaskSet, constant, task, HttpUser


# 4. Use Locust to test with the nested TaskSet

class MyHTTPCat(TaskSet):

    @task
    def get_200_status(self):
        self.client.get("/200")
        print("Get status of 200")

    @task
    class MyAnotherHTTPCat(TaskSet):

        @task
        def get_500_status(self):
            self.client.get("/500")
            print("Get status of 500")
            self.interrupt(reschedule=False)  # Switch back to the above


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHTTPCat]
    wait_time = constant(1)
