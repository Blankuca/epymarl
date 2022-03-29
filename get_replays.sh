#!/bin/bash

for i in {0..5}
do
	python3 src/main.py --config=iql --env-config=gymma with env_args.time_limit=50 env_args.key="lbforaging:Foraging-8x8-2p-3f-v2"

done
