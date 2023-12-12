'''
Objectives: 

Install Psutil.

Create a Python script that fetches this information using Psutil:

Time spent by normal processes executing in user mode
Time spent by processes executing in kernel mode
Time when system was idle
Time spent by priority processes executing in user mode
Time spent waiting for I/O to complete.
Time spent for servicing hardware interrupts
Time spent for servicing software interrupts
Time spent by other operating systems running in a virtualized environment
Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel

'''

import psutil

def get_cpu_times():
    cpu_times = psutil.cpu_times()

    def makespace():
        print("\n###################\n###################\n")

    makespace()
    print(f"Time spent by normal processes executing in user mode: {cpu_times.user} seconds")
    makespace()
    print(f"Time spent by processes executing in kernel mode: {cpu_times.system} seconds")
    makespace()
    print(f"Time when the system was idle: {cpu_times.idle} seconds")
    makespace()
    print(f"Time spent by priority processes executing in user mode: {cpu_times.nice} seconds")
    makespace()
    print(f"Time spent waiting for I/O to complete: {cpu_times.iowait} seconds")
    makespace()
    print(f"Time spent for servicing hardware interrupts: {cpu_times.irq} seconds")
    makespace()
    print(f"Time spent for servicing software interrupts: {cpu_times.softirq} seconds")
    makespace()
    print(f"Time spent by other operating systems running in a virtualized environment: {cpu_times.steal} seconds")
    makespace()
    print(f"Time spent running a virtual CPU for guest operating systems: {cpu_times.guest} seconds")
    makespace()

if __name__ == "__main__":
    get_cpu_times()
    print("All CPU times have been saved.")