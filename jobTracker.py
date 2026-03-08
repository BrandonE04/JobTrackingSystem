jobList = {}

class Id():
    def __init__(self):
        self.value = 1
    
    def increment_id(self):
        self.value += 1

curId = Id()

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

def create_job():
    title = input("Job Title: ")
    company = input("Company Name: ")

    newJob = job(title, company, curId.value)
    curId.increment_id()

    jobList[newJob.id] = newJob

def delete_job():
    deleteId = input("Enter the id of the entry you would like to delete: ")
    del jobList[int(deleteId)]

def print_jobs():
    print("----------Job-List---------")
    for job in jobList.values():
        job.print_job()
        print("---------------------------")


while True:
    print("1. Add application")
    print("2. Delete application")
    print("3. Update application")
    print("4. Print all applications")
    print("X. Exit")
    command = input("Enter: ")

    match command:
        case '1':
            create_job()
        case '2':
            delete_job()
        case '3':
            print("WIP")
        case '4':
            print_jobs()
        case 'X':
            break
        case _:
            print("invalid command")