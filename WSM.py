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
    