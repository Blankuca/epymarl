import matplotlib.pyplot as plt
import pickle
import os
import numpy as np
from collections import defaultdict

def moving_average(a, n=10) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret / n
    
rewards = []
losses = []
episodes = []
returns_agent = defaultdict(list)

for i in range(6,11):
    rewards_file = f"results/replays/{i}/returns.pkl"
    losses_file = f"results/replays/{i}/losses.pkl"
    episodes_file = f"results/replays/{i}/episodes.pkl"

    with open(rewards_file, 'rb') as f:
        returns = pickle.load(f)
        return_agent = list(zip(*returns))
        returns = [sum(x) for x in returns]
        rewards.append(returns)
        
        for i in range(2):
            returns_agent[i].append(list(return_agent[i]))

    with open(losses_file, 'rb') as f:
        losses.append(moving_average(pickle.load(f), n=100))

    with open(episodes_file, 'rb') as f:
        episodes.append(pickle.load(f))


std = np.std(rewards, axis= 0)
mean = np.mean(rewards, axis = 0)
plt.figure()
plt.plot(episodes[0], mean, '-', color="royalblue")
plt.fill_between(episodes[0], mean-std, mean+std, alpha=0.5, color="royalblue")
plt.xlabel("Episodes")
plt.ylabel("Returns")
plt.savefig(f"results/plots/returns_mean.png")
plt.show()


min_len = min(map(len,losses))
losses = [loss[100:min_len] for loss in losses]
std = np.std(losses, axis= 0)
mean = np.mean(losses, axis = 0)
plt.figure()
plt.plot(mean, '-', color="red")
#plt.fill_between(mean-std, mean+std, alpha=0.5, color="purple")
plt.xlabel("Episodes")
plt.ylabel("Losses")
plt.savefig(f"results/plots/losses_mean.png")
plt.show()


plt.figure()
for rewards in returns_agent.values():
    std = np.std(rewards, axis= 0)
    mean = np.mean(rewards, axis = 0)
    plt.plot(episodes[0], mean, '-')
    plt.fill_between(episodes[0], mean-std, mean+std, alpha=0.5)
plt.xlabel("Episodes")
plt.ylabel("Returns")
plt.savefig(f"results/plots/returns_mean_agents.png")
plt.show()

def mk_plots(i):

    rewards_file = f"results/replays/{i}/returns.pkl"
    losses_file = f"results/replays/{i}/losses.pkl"
    episodes_file = f"results/replays/{i}/episodes.pkl"
    os.mkdir(f"results/plots/{i}/")


    with open(rewards_file, 'rb') as f:
        returns = pickle.load(f)

    with open(losses_file, 'rb') as f:
        losses = pickle.load(f)

    with open(episodes_file, 'rb') as f:
        episodes = pickle.load(f)

    plt.figure()
    returns_agent = list(zip(*returns))
    for r in returns_agent:
        plt.plot(episodes,r)
    plt.xlabel("Episodes")
    plt.ylabel("Return")
    plt.savefig(f"results/plots/{i}/returns_agent.png")

    plt.figure()
    plt.plot(episodes,[sum(x) for x in returns])
    plt.xlabel("Episodes")
    plt.ylabel("Return")
    plt.savefig(f"results/plots/{i}/returns.png")

    plt.figure()
    plt.plot(moving_average(losses))
    plt.xlabel("Episodes")
    plt.ylabel("Return")
    plt.savefig(f"results/plots/{i}/losses.png")


