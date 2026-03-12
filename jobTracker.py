import database_setup
import jobTracker_info

jobList = {}
curId = jobTracker_info.Id()

def create_job():
    title = input("Job Title: ")
    company = input("Company Name: ")

    newJob = jobTracker_info.job(title, company, curId.value)
    curId.increment_id()

    jobList[newJob.id] = newJob

def delete_job():
    deleteId = input("Enter the id of the entry you would like to delete: ")
    if deleteId in jobList:
        del jobList[int(deleteId)]
    else:
        print("Invalid id")

def update_job():
    job = int(input("Enter job id of the job you would like to update: "))

    if job not in jobList:
        print("Invalid id")
        return

    print("1. Update company")
    print("2. Update title")
    print("3. Update application status")
    print("X. Go back")
    category = input("Enter: ")

    match category:
        case '1':
            company = input("Enter new company name: ")
            jobList[job].company = company
        case '2':
            title = input("Enter new job title: ")
            jobList[job].title = title
        case '3':
            update_job_status(job)
        case 'X':
            return
        case _:
            print("invalid category")

def update_job_status(job):
    print("1. Applied")
    print("2. Rejected")
    print("3. Need to complete OA")
    print("4. OA completed")
    print("5. Interview Stage")
    print("X. Go back")
    status = input("Enter: ")

    match status:
        case '1':
            jobList[job].status = "Applied"
        case '2':
            jobList[job].status = "Rejected"
        case '3':
            jobList[job].status = "Need to complete OA"
        case '4':
            jobList[job].status = "OA completed"
        case '5':
            jobList[job].status = "Interview stage"
        case 'X':
            return
        case _:
            print("Invalid status")

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
            update_job()
        case '4':
            print_jobs()
        case 'X':
            break
        case _:
            print("invalid command")