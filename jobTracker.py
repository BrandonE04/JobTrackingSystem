jobList = []

class job():
    def __init__(self, title, company):
        self.title = title
        self.company = company
        self.status = "Applied"

def createJob():
    title = input("Job Title: ")
    company = input("Company Name: ")
    newJob = job(title, company)



