from locust import SequentialTaskSet, HttpUser, constant, task


# 6. 1_Task the test with 3_SequentialTaskSet in a sequential way


class MySeqTask(SequentialTaskSet):

    @task
    def get_200_status(self):
        self.client.get("/200")
        print("Status of 200")

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Status of 500")


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MySeqTask]
    wait_time = constant(1)

# locust -f 01_introduction/3_SequentialTaskSet/sequential_taskset.py
