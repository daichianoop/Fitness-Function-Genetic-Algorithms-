import math

# Deadline Fitness <F1> with <weight factor (a) = 0.7> and <k = 1>
def calculate_F1(endTime, deadline):
    if endTime <= deadline:
        return 100 * endTime / deadline
    else:
        k = 1
        return math.exp(-k * (endTime - deadline))
    
# Deadline Fitness <F2> with <weight factor (b) = 0.3> and <k = 1>
def calculate_F2(endCost, budget):
    if endCost <= budget:
        return 100 * endCost / budget
    else:
        k = 1
        return math.exp(-k * (endCost - budget))

# Final Calculation
def calculate_X(endTime, deadline, endCost, budget):
    F1 = calculate_F1(endTime, deadline)
    F2 = calculate_F2(endCost, budget)
    
    X = 0.7 * F1 + 0.3 * F2
    # XX Debugging Section 1 XX
    # print(F1 , F2)
    
    return round(X,3)

# Assigning Lists of Values
endTimes = [100, 125, 167, 250, 500]
deadlines = [150, 150, 150, 150, 150]
endCosts = [30, 31, 34, 38, 50]
budgets = [29, 29, 29, 29, 29]

# Array to store "X" values
VM_FitnessValues = []

# Calculating X for each set of values
for i in range(5):
    X = calculate_X(endTimes[i], deadlines[i], endCosts[i], budgets[i])
    VM_FitnessValues.append((i, X))

# XX Debugging Section 2 XX
# print(VM_FitnessValues)

# Final Output
print("The calculated VM Fitness Scores:")

for index, value in VM_FitnessValues:
    print(f"[VM {index + 1}] - {value}")

# Finding the highest value of X and its index
max_X_value = max(VM_FitnessValues, key=lambda x: x[1])
print(f"[VM {max_X_value[0] + 1}] with [FScore {max_X_value[1]}] is the Ideal VM.")