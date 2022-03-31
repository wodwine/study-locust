from locust import HttpUser, task, constant, TaskSet


class FirefoxBrowserTest(TaskSet):

    @task
    def launch(self):
        print("Firefox Browser Tests")
        self.client.get("/200", name=self.__class__.__name__)
        self.interrupt(reschedule=False)


class ChromeBrowserTest(TaskSet):
    @task
    def launch(self):
        print("Chrome Browser Tests")
        self.client.get("/300", name=self.__class__.__name__)
        self.interrupt(reschedule=False)


class EdgeBrowserTest(TaskSet):
    @task
    def launch(self):
        print("Edge Browser Tests")
        self.client.get("/400", name=self.__class__.__name__)
        self.interrupt(reschedule=False)


class MyLoadTest(HttpUser):
    wait_time = constant(1)
    tasks = [ChromeBrowserTest, FirefoxBrowserTest, EdgeBrowserTest]

    # locust -f 01_introduction/CommandLineDemo/simple_test_2.py -u 1 -r 1 -t 10s
    # --headless --print-stats --host=https://http.cat -L DEBUG --logfile mylog.log --html run1
