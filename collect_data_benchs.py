#!/bin/python3
import os
import sys
import subprocess
from multiprocessing import Process

# 20 process better divided on 7, then on 8 (all logical CPUs)
# Configuration: i7-10510u, 4 physical CPUs, 8 logical CPUs
# 7 parallel ~19min, 4 parallel ~22min
NUM_PARALLEL = 7

def launch_sim(bench_path, output_path):
    cmd = "./bin/champsim --warmup_instructions 5000000 --simulation_instructions 20000000".split()
    cmd += [bench_path, ">", output_path]
    cmd = " ".join(cmd)
    print(cmd)
    subprocess.run(cmd, shell=True)

def launch_sim_from_queue(queue, path_to_benchs, path_to_output):
    for bench in queue:
        launch_sim(os.path.join(os.path.abspath(path_to_benchs), bench), os.path.join(os.path.abspath(path_to_output), bench+".log"))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Please, pass the path_to_benchs and path_to_output\n" +
            "Using: python3 collect_data_benchs.py path_to_benchs path_to_output")
        exit(1)
    path_to_benchs = sys.argv[1]
    path_to_output = sys.argv[2]

    counter_bench = 0
    for r, d, f in os.walk(path_to_benchs):
        # print(f)
        queues = [f[i::NUM_PARALLEL] for i in range(NUM_PARALLEL)]
        print(queues)
        process = []
        for idx in range(NUM_PARALLEL):
            p = Process(target=launch_sim_from_queue, args=(queues[idx], path_to_benchs, path_to_output))
            p.start()
            process.append(p)

        for idx in range(NUM_PARALLEL):
            process[idx].join()
