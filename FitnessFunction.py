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

cloudlets = [
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
    Cloudlet(sr no., task length, arrival time, deadline, budget),
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

fitness_scores = []

for cloudlet in cloudlets:
    scores = []
    for vm in vms:
        urgency_factor = 1 / (cloudlet.deadline - cloudlet.deployment_time)
        cost_efficiency = cloudlet.max_cost / vm.cost_per_second
        fitness_score = 0.5 * urgency_factor + 0.3 * (vm.mips / cloudlet.length) + 0.2 * cost_efficiency
        scores.append(round(fitness_score, 2))
    fitness_scores.append(scores)

print("Fitness Scores for each Task on each VM:")
for index, (cloudlet, scores) in enumerate(zip(cloudlets, fitness_scores), start=1):
    print(f"Task {cloudlet.cloudlet_id}:")
    for vm_index, score in enumerate(scores, start=1):
        print(f" [VM {vm_index}] : {score}")
    print()
    
