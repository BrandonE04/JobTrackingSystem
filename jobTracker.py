jobList = {}

class Id():
    def __init__(self):
        self.value = 1
    
    def incrementId(self):
        self.value += 1

curId = Id()

class job():

    def __init__(self, title, company, id):
        self.title = title
        self.company = company
        self.status = "Applied"
        self.id = id
    
    def printJob(self):
        print(f"Id: {self.id}")
        print(f"Company: {self.company}")
        print(f"Title: {self.title}")
        print(f"Status: {self.status}")

def createJob():
    title = input("Job Title: ")
    company = input("Company Name: ")
    newJob = job(title, company, curId.value)
    curId.incrementId()

