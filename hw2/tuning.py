import os

for lr in [5e-3, 1e-2, 2e-2]:
    for b in [10000, 30000, 50000]:
        os.system(
            f"--env_name HalfCheetah-v4 --ep_len 150 \
--discount 0.95 -n 100 -l 2 -s 32 -b {b} -lr {lr} -rtg --nn_baseline \
--exp_name q4_search_b{b}_lr{lr}_rtg_nnbaseline"
        )
