from locust import HttpUser, task, constant, SequentialTaskSet
from read_test_data import CsvRead


# 3. Pass parameter name and data


class MyScript(SequentialTaskSet):

    @task
    def place_order(self):
        test_data = CsvRead("02/DataParameterization/customer-data.csv").read()
        print(test_data)

        data = {
            "custname": test_data['name'],
            "custtel": test_data['phone'],
            "custemail": test_data['email'],
            "size": test_data['size'],
            "topping": test_data['toppings'],
            "delivery": test_data['time'],
            "comments": test_data['instructions']
        }

        name = "Order for " + test_data['name']

        with self.client.post("/post", catch_response=True, name=name, data=data) as response:
            if response.status_code == 200 and test_data['name'] in response.text:
                response.success()
            else:
                response.failure("Failure in processing the order")


class MyLoadTest(HttpUser):
    host = "https://httpbin.org"
    wait_time = constant(1)
    tasks = [MyScript]

# locust -f 02/DataParameterization/data_parameterization.py
# -u 3 -r 1 -t 5s --only-summary --headless
