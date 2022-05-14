import pickle
import pandas as pd
from os import walk
from ast import literal_eval
import numpy as np
import argparse

def generate_trajectories(map, output_path):
    trajectories = []

    base_path = "results/replays"
    trajectories = []

    folder = f"{base_path}/{map}"
    for (subfolder, _, filenames) in walk(folder):
        for file in filenames:
            if ".gz" in file:
                    with open(f"{subfolder}/{file}", 'rb') as handle:
                        trajectory = pickle.load(handle)
                        trajectories.append(trajectory)

    with open(f'{output_path}/{map}.pkl', 'wb') as handle:
        pickle.dump(trajectories, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--map', type=str, default='Foraging-12x12-2p-3f-v2')
    parser.add_argument('--output_folder', type=str, default='/work3/s174437/Blankuca/decision-transformer/gym/data')
    
    args = parser.parse_args()
    generate_trajectories(args.map, args.output_folder)