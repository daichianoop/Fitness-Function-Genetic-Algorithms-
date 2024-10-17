# OPTIMIZE : MULTITASK MODE 
# original code by Anoop Kumar 
import math

class Cloudlet:
    def __init__(self, cloudlet_id, length, deployment_time, deadline, max_cost):
        self.cloudlet_id = cloudlet_id
        self.length = length
        self.deployment_time = deployment_time
        self.deadline = deadline
        self.max_cost = max_cost

class VM:
    def __init__(self, vm_id, mips, cost_per_second):
        self.vm_id = vm_id
        self.mips = mips
        self.cost_per_second = cost_per_second

#TODO : Function to calculate end time and end cost for each cloudlet and VM 
def calculate_end_time_and_cost(cloudlet, vm):
    end_time = math.ceil((cloudlet.length / vm.mips) + cloudlet.deployment_time) 
    end_cost = round(end_time * vm.cost_per_second,2) 
    # Debugging Slot 1
    # print(end_time ,end_cost)
    return end_time, end_cost

#TODO : Deadline Fitness calculation function (*F1*) 
def calculate_F1(endTime, deadline):
    if endTime <= deadline:
        return 100 * endTime / deadline
    else:
        k = 1
        return math.exp(-k * (endTime - deadline))

#TODO : Cost Fitness calculation function (*F2*)  
def calculate_F2(endCost, budget):
    if endCost <= budget:
        return 100 * endCost / budget
    else:
        k = 1
        return math.exp(-k * (endCost - budget))

#TODO : Final Fitness Calculation 
def calculate_fitness(cloudlet, vm):
    end_time, end_cost = calculate_end_time_and_cost(cloudlet, vm)
    F1 = calculate_F1(end_time, cloudlet.deadline)
    F2 = calculate_F2(end_cost, cloudlet.max_cost)
    return 0.5 * F1 - 0.5 * F2

#FIX : Feeding the Dataset 
cloudlets = [
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget5),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget)
]
vms = [
    VM(vm no., MIPS, cost/sec),
    VM(vm no., MIPS, cost/sec),
    VM(vm no., MIPS, cost/sec),
    VM(vm no., MIPS, cost/sec),
    VM(vm no., MIPS, cost/sec)
]

# for data set contact : anoop2005ak@gmail.com

#TODO : Array to store fitness values for all VMs and cloudlets 
fitness_matrix = []

#TODO : Calculating fitness values for each combination of VM and cloudlet 
for cloudlet in cloudlets:
    cloudlet_fitness_values = []
    for vm in vms:
        fitness_value = calculate_fitness(cloudlet, vm)
        cloudlet_fitness_values.append(fitness_value)
    fitness_matrix.append(cloudlet_fitness_values)

#OPTIMIZE : Display the fitness values and the VM with the highest fitness below each task 
print("Fitness Values Matrix -->>" ,end="\n")
for i in range(len(cloudlets)):
    print(f"Task {cloudlets[i].cloudlet_id} ->>")
    max_fitness = -1
    best_vm = None
    for j in range(len(vms)):
        if fitness_matrix[i][j] > max_fitness:
            max_fitness = fitness_matrix[i][j]
            best_vm = vms[j]
        print(f"\b | [VM {vms[j].vm_id}] : {round(fitness_matrix[i][j], 2)} |", end="\n")
    print(f"\nBest VM for Task {cloudlets[i].cloudlet_id}: [VM {best_vm.vm_id}] with fitness: [{round(max_fitness, 2)}]\n")
