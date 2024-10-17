# OPTIMIZE: MULTITASK MODE  

This project implements a multitask optimization algorithm for cloudlet and virtual machine (VM) scheduling. The goal is to efficiently allocate resources by calculating fitness values based on execution time, cost, and deadlines.  

## Original Code by  

Anoop Kumar  

## Table of Contents  

- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Functions](#functions)  
- [Data Input](#data-input)  
- [Output](#output)  
- [Contributing](#contributing)  
- [Contact](#contact)  

## Features  

- Calculates end time and cost for cloudlets running on VMs.  
- Evaluates fitness based on deadline adherence and cost efficiency.  
- Displays the best VM for each cloudlet based on calculated fitness values.  

## Installation  

To run this project, ensure you have Python installed on your machine. You can clone the repository and run the script directly.  

1. Clone the repository:  
    ```bash  
    git clone https://github.com/yourusername/optimize-multitask-mode.git  
    ```  

2. Navigate to the project directory:  
    ```bash  
    cd optimize-multitask-mode  
    ```  

3. Run the script:  
    ```bash  
    python optimize_multitask.py  
    ```  

## Usage  

The script calculates the fitness values for each combination of cloudlet and VM. The results will display the fitness values and the best VM for each task.  

### Functions  

- `calculate_end_time_and_cost(cloudlet, vm)`: Computes the end time and cost for a given cloudlet and VM.  
- `calculate_F1(endTime, deadline)`: Calculates the fitness based on deadline adherence.  
- `calculate_F2(endCost, budget)`: Calculates the fitness based on cost efficiency.  
- `calculate_fitness(cloudlet, vm)`: Computes the overall fitness value for a cloudlet-VM pair.  

## Data Input  

The script contains sample data for cloudlets and VMs. You can modify the `cloudlets` and `vms` lists with your own data.  

```python  
cloudlets = [  
    Cloudlet(1, 1000, 10, 50, 200),  
    Cloudlet(2, 2000, 15, 60, 300),  
    # Add more cloudlets as needed  
]  

vms = [  
    VM(1, 1000, 0.1),  
    VM(2, 2000, 0.2),  
    # Add more VMs as needed  
]
