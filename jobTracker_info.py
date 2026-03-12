class Id():
    def __init__(self):
        self.value = 1
    
    def increment_id(self):
        self.value += 1

class job():

    def __init__(self, title, company, id):
        self.title = title
        self.company = company
        self.status = "Applied"
        self.id = id
    
    def print_job(self):
        print(f"Id: {self.id}")
        print(f"Company: {self.company}")
        print(f"Title: {self.title}")
        print(f"Status: {self.status}")

