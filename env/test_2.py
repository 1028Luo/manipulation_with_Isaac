"""Launch Isaac Sim Simulator first."""


from omni.isaac.lab.app import AppLauncher

# launch omniverse app in headless mode with off-screen rendering
app_launcher = AppLauncher(headless=True, enable_cameras=True)
simulation_app = app_launcher.app

"""Rest everything follows."""

import gymnasium as gym

# adjust camera resolution and pose
env_cfg.viewer.resolution = (640, 480)
env_cfg.viewer.eye = (1.0, 1.0, 1.0)
env_cfg.viewer.lookat = (0.0, 0.0, 0.0)
# create isaac-env instance
# set render mode to rgb_array to obtain images on render calls
env = gym.make(task_name, cfg=env_cfg, render_mode="rgb_array")
# wrap for video recording
video_kwargs = {
    "video_folder": "videos/train",
    "step_trigger": lambda step: step % 1500 == 0,
    "video_length": 200,
}
env = gym.wrappers.RecordVideo(env, **video_kwargs)