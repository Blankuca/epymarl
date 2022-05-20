#!/bin/bash

MAP="lbforaging:Foraging-8x8-2p-3f-v2"

for i in {0..10}
do
	#python3 src/main.py --config=iql --env-config=gymma with env_args.time_limit=50 env_args.key="lbforaging:Foraging-8x8-2p-3f-v2"
	python3 src/main.py --config=iql --env-config=gymma with env_args.time_limit=50 env_args.key=$MAP

done

python3 combine_data.py --map=$MAP
