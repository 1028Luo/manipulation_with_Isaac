import time

from omni.isaac.lab.app import AppLauncher

# when you want no render
# app_launcher = AppLauncher(headless=True)
app_launcher = AppLauncher()
simulation_app = app_launcher.app

"""Rest everything follows."""

import gymnasium as gym
import torch
import omni.isaac.lab_tasks  # noqa: F401
from omni.isaac.lab_tasks.utils import load_cfg_from_registry

# import myEnv


# creates base environment
#################### to do ####################
## register another env of my own
cfg = load_cfg_from_registry("Isaac-Lift-Soft-Franka-v0", "env_cfg_entry_point")

#################### to do ####################
cfg.scene.num_envs = 4 # overides num of envs

env = gym.make("Isaac-Lift-Soft-Franka-v0", cfg=cfg, render_mode="rgb_array")


# wrap environment to enforce that reset is called before step
env = gym.wrappers.OrderEnforcing(env)

observation, info = env.reset()

episode_over = False
while not episode_over:
    action = env.action_space.sample()  # agent policy that uses the observation and info
    action = torch.from_numpy(action)
    observation, reward, terminated, truncated, info = env.step(action)

    episode_over = False
    #episode_over = terminated[0] or truncated[0]

env.close()


print('aaa')

# env.close()
