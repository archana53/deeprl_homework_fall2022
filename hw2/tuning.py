import os

for lr in [1e-4, 5e-4, 1e-3, 5e-3, 1e-2]:
    for b in [100, 500, 1000, 2000, 3000]:
        os.system(
            f"python cs285/scripts/run_hw2.py --env_name InvertedPendulum-v4 -b {b} -lr {lr} --exp_name q2_b{b}_r{lr}  --ep_len 1000 --discount 0.9 -n 100 -l 2 -s 64 -rtg"
        )
