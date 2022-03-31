from locust import HttpUser, constant, task


# 2. Use Locust to test the http request with Task


class MyReqRes(HttpUser):
    # host = "https://reqres.in"
    wait_time = constant(1)

    @task
    def get_users(self):
        res = self.client.get("/api/users?page=2")
        print(res.text, res.status_code, res.headers)

    @task
    def create_users(self):
        res = self.client.post("/api/users",
                               data="""
                                   {"name":"Wine","job":"ML Engineer"}
                                    """)
        print(res.text, res.status_code, res.headers)

# locust -f 01_introduction/Task/app.py  --host=https://reqres.in
