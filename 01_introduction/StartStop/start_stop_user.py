from locust import User, task, constant


class MyTest(User):
    wait_time = constant(1)

    @staticmethod
    def on_start():
        print("Starting")

    @task
    def task_1(self):
        print("My task 1")

    @staticmethod
    def on_stop():
        print("Stopping")

# locust -f 01_introduction/StartStop/start_stop_user.py -r 1 -u 1 -t 10s
# --headless --only-summary
