# gym-foo
Making a custom environment in GYM, from here: https://medium.com/@apoddar573/making-your-own-custom-environment-in-gym-c3b65ff8cdaa
This environment is meant to mirror an electric vehicle. 
This environment is designed for Reinforcement Learning purposes, thus it includes:
1. States - output
2. Rewards - output for ...
3. Actions - input

Gym is a toolkit for developing and comparing Reinforcement Learning algorithms. It is implemented in Python and R(though the former is primarily used) and can be used to make your code for training RL models short, simple and easy-to-read.


# Install Environment

To install the environment, just go to the gym-foo folder and run the command -

pip install -e .
This will install the gym environment. Now, we can use our gym environment with the following -

# To Use the Environnment

import gym
import gym_foo
env = gym.make('foo-v0')

This is still in making, suggestions appreciated.
