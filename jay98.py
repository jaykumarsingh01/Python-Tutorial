import multiprocessing
import time
import os

def worker_function(name):
    print(f"Process {name} (PID: {os.getpid()}) started")
    time.sleep(2)
    print(f"Process {name} (PID: {os.getpid()}) finished")

if __name__ == "__main__":
    multiprocessing.set_start_method("fork" if hasattr(os, "fork") else "spawn")  # Ensures compatibility
    processes = []
    num_processes = 4  # Number of parallel processes
    
    # Creating processes
    for i in range(num_processes):
        process = multiprocessing.Process(target=worker_function, args=(i,))
        processes.append(process)
        process.start()
    
    # Waiting for all processes to complete
    for process in processes:
        process.join()
    
    print("All processes completed.")
