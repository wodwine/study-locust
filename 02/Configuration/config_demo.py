from locust import HttpUser, task, constant


class LoadTest(HttpUser):
    wait_time = constant(1)

    def __init__(self, parent):
        super().__init__(parent)
        self.hostname = self.host

    @task
    def home_page(self):
        res = self.client.get("/", name=self.hostname)
        print(res.text)

# locust -f 02/Configuration/config_demo.py
# locust -f 02/Configuration/config_demo.py --config 02/Configuration/mycustom.conf
# locust -f 02/Configuration/config_demo.py --config 02/Configuration/mycustom.yaml
