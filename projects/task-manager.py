import psutil
import cpuinfo
import time
import wmi

def get_cpu_name():
    try:
        info = cpuinfo.get_cpu_info()
        return info['brand_raw']
    except KeyError:
        return "Unknown CPU"

def get_cpu_cores():
    return psutil.cpu_count(logical=False)

def get_gpu_name():
    try:
        c = wmi.WMI()
        for gpu in c.Win32_VideoController():
            if 'intel' in gpu.Caption.lower():
                return [gpu.Caption]
        return ["No integrated GPU detected"]
    except Exception as e:
        return ["Error detecting GPU:", str(e)]

def get_gpu_usage():
    try:
        gpu_usage = psutil.virtual_memory().percent
        return gpu_usage
    except Exception as e:
        return ["Error detecting GPU usage:", str(e)]

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def main():
    print("\nMy Task Manager\n")

    cpu_name = get_cpu_name()
    cpu_cores = get_cpu_cores()
    gpu_names = get_gpu_name()
    
    for i in range(cpu_cores):
        print("CPU Name:", cpu_name)

    for i, gpu_name in enumerate(gpu_names):
        print("GPU Name:", gpu_name)

    while True:
        cpu_usage = get_cpu_usage()
        gpu_usage = get_gpu_usage()
        
        print("\nCPU Usage: {}%".format(cpu_usage))
        print("GPU Usage: {}%".format(gpu_usage))
        
        time.sleep(1)

if __name__ == "__main__":
    main()