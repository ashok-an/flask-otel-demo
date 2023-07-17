from locust import HttpUser, task

class TestUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/roll")
        self.client.get("/xkcd")
        self.client.get("/not-found")
