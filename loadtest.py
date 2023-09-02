from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    # define wait time between tasks
    wait_time = between(1, 2.5)

    @task
    def get_tides(self):
        self.client.get("/apilinkhere")


# run the script with the following command
# locust -f loadtest.py --headless -u 1 -r 1 --run-time 70s --host=https://hosturlhere
