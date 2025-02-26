from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def view_courses(self):
        self.client.get("/api/courses/")
    
    @task
    def enroll_course(self):
        self.client.post("/api/enrollments/", json={"course_id": 1})