from locust import HttpUser, task, constant


class MyLoadTest(HttpUser):
    wait_time = constant(1)

    @task
    def launch(self):
        self.client.get("/200")

# locust -f 01_introduction/CommandLineDemo/simple_test.py -u 1 -r 1 -t 10s
# --headless --print-stats --csv run1.csv --csv-full-history --host=https://http.cat
