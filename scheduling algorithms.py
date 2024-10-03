from collections import deque

# Process data structure
class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

# Function to calculate and print results
def calculate_times(processes):
    total_tat = total_wt = 0
    print(f"{'PID':<10}{'Arrival':<10}{'Burst':<10}{'Priority':<10}{'Completion':<15}{'Turnaround':<15}{'Waiting':<10}")
    for p in processes:
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time
        total_tat += p.turnaround_time
        total_wt += p.waiting_time
        print(f"{p.pid:<10}{p.arrival_time:<10}{p.burst_time:<10}{p.priority:<10}{p.completion_time:<15}{p.turnaround_time:<15}{p.waiting_time:<10}")
    
    n = len(processes)
    print(f"\nAverage Turnaround Time: {total_tat / n:.2f}")
    print(f"Average Waiting Time: {total_wt / n:.2f}")

# First-Come First-Serve (FCFS)
def fcfs_scheduling(processes):
    processes.sort(key=lambda p: p.arrival_time)  # Sort by arrival time
    current_time = 0
    for p in processes:
        if current_time < p.arrival_time:
            current_time = p.arrival_time
        p.completion_time = current_time + p.burst_time
        current_time = p.completion_time
    
    print("\nFCFS Scheduling:")
    calculate_times(processes)

# Shortest Job First (SJF) - Non-preemptive
def sjf_scheduling(processes):
    processes.sort(key=lambda p: (p.arrival_time, p.burst_time))  # Sort by arrival time, then burst time
    current_time = 0
    completed = []
    while processes:
        available_processes = [p for p in processes if p.arrival_time <= current_time]
        if available_processes:
            shortest_process = min(available_processes, key=lambda p: p.burst_time)
            processes.remove(shortest_process)
            if current_time < shortest_process.arrival_time:
                current_time = shortest_process.arrival_time
            shortest_process.completion_time = current_time + shortest_process.burst_time
            current_time = shortest_process.completion_time
            completed.append(shortest_process)
        else:
            current_time += 1
    
    print("\nSJF Scheduling:")
    calculate_times(completed)

# Priority Scheduling - Non-preemptive
def priority_scheduling(processes):
    processes.sort(key=lambda p: (p.arrival_time, p.priority))  # Sort by arrival time, then priority
    current_time = 0
    completed = []
    while processes:
        available_processes = [p for p in processes if p.arrival_time <= current_time]
        if available_processes:
            highest_priority_process = min(available_processes, key=lambda p: p.priority)
            processes.remove(highest_priority_process)
            if current_time < highest_priority_process.arrival_time:
                current_time = highest_priority_process.arrival_time
            highest_priority_process.completion_time = current_time + highest_priority_process.burst_time
            current_time = highest_priority_process.completion_time
            completed.append(highest_priority_process)
        else:
            current_time += 1
    
    print("\nPriority Scheduling:")
    calculate_times(completed)

# Round Robin (RR)
def round_robin_scheduling(processes, quantum):
    processes = deque(sorted(processes, key=lambda p: p.arrival_time))  # Sort by arrival time
    current_time = 0
    ready_queue = deque()
    completed = []
    while processes or ready_queue:
        # Move processes that have arrived into the ready queue
        while processes and processes[0].arrival_time <= current_time:
            ready_queue.append(processes.popleft())

        if ready_queue:
            current_process = ready_queue.popleft()
            if current_process.burst_time > quantum:
                current_process.burst_time -= quantum
                current_time += quantum
                while processes and processes[0].arrival_time <= current_time:
                    ready_queue.append(processes.popleft())
                ready_queue.append(current_process)  # Reinsert into ready queue
            else:
                current_time += current_process.burst_time
                current_process.completion_time = current_time
                current_process.burst_time = 0
                completed.append(current_process)
        else:
            current_time += 1

    print("\nRound Robin Scheduling:")
    calculate_times(completed)

# Example Processes
process_list = [
    Process("P1", 0, 8, 2),
    Process("P2", 1, 4, 1),
    Process("P3", 2, 9, 4),
    Process("P4", 3, 5, 3)
]

if __name__ == "__main__":
    # First-Come First-Serve (FCFS)
    fcfs_scheduling([Process(p.pid, p.arrival_time, p.burst_time, p.priority) for p in process_list])

    # Shortest Job First (SJF)
    sjf_scheduling([Process(p.pid, p.arrival_time, p.burst_time, p.priority) for p in process_list])

    # Priority Scheduling
    priority_scheduling([Process(p.pid, p.arrival_time, p.burst_time, p.priority) for p in process_list])

    # Round Robin Scheduling with time quantum = 3
    round_robin_scheduling([Process(p.pid, p.arrival_time, p.burst_time, p.priority) for p in process_list], quantum=3)
