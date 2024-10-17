# OPTIMIZE : MULTITASK MODE 
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
    Cloudlet(1, 50000, 0, 150, 29),
    Cloudlet(2, 70000, 0, 250, 46),
    Cloudlet(3, 30000, 20, 150, 20),
    Cloudlet(4, 20000, 20, 220, 15),
    Cloudlet(5, 100000, 40, 400, 70),
    Cloudlet(6, 80000, 40, 600, 45),
    Cloudlet(7, 60000, 50, 410, 35),
    Cloudlet(8, 40000, 60, 300, 26),
    Cloudlet(9, 150000, 70, 910, 55),
    Cloudlet(10, 120000, 80, 600, 67),
    Cloudlet(11, 35000, 40, 390, 30),
    Cloudlet(12, 25000, 40, 130, 17),
    Cloudlet(13, 45000, 80, 500, 28),
    Cloudlet(14, 20000, 80, 200, 25),
    Cloudlet(15, 60000, 80, 300, 40)
]
vms = [
    VM(1, 500, 0.3),
    VM(2, 400, 0.25),
    VM(3, 300, 0.2),
    VM(4, 200, 0.15),
    VM(5, 100, 0.1)
]

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