import copy
def serverFarm(jobs, servers):

    def return_min(min, array):
        for i in array :
            if i == min : 
                return array.index(i)
    
    def return_first(elem, array):
        for index, item in enumerate(array) :
            if item == elem : 
                return index
    
            

    def min_load(assigned_jobs) :
        min_procs = []
        for proc in assigned_jobs:
            print("proc: " + str(proc))
            print("sum proc " + str(sum(proc)))
            min_procs.append(sum(proc))
        print("min procs: " + str(min_procs))
        return return_min(min(min_procs), min_procs)


    original_jobs = copy.deepcopy(jobs)
    jobs.sort(reverse = True)
    
    assigned_jobs = []
    for server in range(0, servers): 
        assigned_jobs.append([]) 

    for job in jobs: 
        print("job: ", + job)
        assigned_jobs[min_load(assigned_jobs)].append(return_first(job, original_jobs))
    
    return assigned_jobs


jobs = [15, 30, 15, 5, 10]
servers = 3

print(serverFarm(jobs, servers))       
