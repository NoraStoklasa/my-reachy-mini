from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose

with ReachyMini() as reachy:
    tilt_pose = create_head_pose(roll=15)
    return_tilt_pose = create_head_pose(roll=0)

    reachy.goto_target(head=return_tilt_pose, antennas=[0, 0], duration=0.5)
    reachy.goto_target(
        head=tilt_pose, antennas=[0.5, -0.5], duration=0.5, body_yaw=0.17
    )
    reachy.goto_target(
        head=tilt_pose, antennas=[-0.5, 0.5], duration=0.5, body_yaw=-0.17
    )
    reachy.goto_target(head=return_tilt_pose, antennas=[0, 0], duration=0.5)
