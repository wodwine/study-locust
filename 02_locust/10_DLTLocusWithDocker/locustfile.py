from locust import HttpUser, task, constant


class HelloWorld(HttpUser):
    wait_time = constant(1)
    host = "https://petstore.octoperf.com"

    @task
    def test(self):
        self.client.get("/")

# docker run -p 8089:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py
# docker run -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py --html /mnt/locust/myrun1.html
# --headless --only-summary -r 1 -u 1 -t 5s
