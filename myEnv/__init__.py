# For ME5418 Project submission_1
# Modified from the original __init__.py


"""
Franka-Cabinet environment.
"""

import gymnasium as gym

from . import agents
from .franka_cabinet_env import FrankaCabinetEnv, FrankaCabinetEnvCfg
from .manipulate_soft_direct import ManipulateSoftDirect, ManipulateSoftDirectCfg
##
# Register Gym environments.
##

gym.register(
    id="Isaac-Franka-Cabinet-Direct-v0",
    entry_point="omni.isaac.lab_tasks.direct.franka_cabinet:FrankaCabinetEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": FrankaCabinetEnvCfg,
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:FrankaCabinetPPORunnerCfg",
        "skrl_cfg_entry_point": f"{agents.__name__}:skrl_ppo_cfg.yaml",
    },
)

gym.register(
    id="ManipulateSoftDirect",
    entry_point="omni.isaac.lab_tasks.direct.franka_cabinet:ManipulateSoftDirect",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": ManipulateSoftDirectCfg,
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:FrankaCabinetPPORunnerCfg",
        "skrl_cfg_entry_point": f"{agents.__name__}:skrl_ppo_cfg.yaml",
    },
)
