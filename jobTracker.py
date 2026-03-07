jobList = {}

class job():

    def __init__(self, title, company):
        self.title = title
        self.company = company
        self.status = "Applied"
    
    def printJob(self):
        print(f"Company: {self.company}")
        print(f"Title: {self.title}")
        print(f"Status: {self.status}")

def createJob():
    title = input("Job Title: ")
    company = input("Company Name: ")
    newJob = job(title, company)




