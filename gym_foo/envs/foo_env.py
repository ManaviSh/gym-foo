import gym
from gym import error, spaces, utils
from gym.utils import seeding

class FooEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.state = []
		for i in range(3):
		  self.state += [[]]
			for j in range(3):
				self.state[i] += ["-"]
		self.counter = 0
		self.done = 0
		self.add = [0, 0]
		self.reward = 0
  def step(self, action):
    ...
  def reset(self):
    ...
  def render(self, mode='human', close=False):
    ...
