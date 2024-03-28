import gym
import metagym.quadrupedal

env = gym.make('quadrupedal-v0',render=1,task="ground")

s = env.reset()
for i in range(100):
    new, rew, done, _ = env.step(env.action_space.sample()) 