from locust import User, task, constant, between, constant_pacing
import time


# 7. Use wait time

class MyUser(User):
    # wait_time = constant(1)  # 1 minute
    # wait_time = between(2, 5)  # Between 2-5 second
    wait_time = constant_pacing(3)

    @task
    def launch(self):
        time.sleep(2)
        print("Constant Pacing Demo")

# locust -f 01_introduction/4_WaitTime/wait_time.py
