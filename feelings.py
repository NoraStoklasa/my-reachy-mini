from reachy_mini.utils import create_head_pose

from movement import neutral_position
import time


def happy(reachy):
    smile_pose = create_head_pose(pitch=-10, roll=10, mm=True)

    for i in range(2):
        reachy.goto_target(
            head=smile_pose, antennas=[0.5, -0.5], duration=0.4, body_yaw=0.17
        )

        reachy.goto_target(
            head=smile_pose, antennas=[-0.5, 0.5], duration=0.4, body_yaw=-0.17
        )

    # return to the initial position
    neutral_position(reachy)


def sad(reachy):
    frown_pose = create_head_pose(pitch=15, roll=-15, mm=True)

    reachy.goto_target(
        head=frown_pose, antennas=[-1.0, 1.0], duration=2.0, body_yaw=0.17
    )

    time.sleep(2.0)

    # return to the initial position
    neutral_position(reachy)


def surprised(reachy):
    wide_eyes_pose = create_head_pose(pitch=-18, degrees=True)

    reachy.goto_target(head=wide_eyes_pose, antennas=[-1.0, 1.0], duration=0.4)

    time.sleep(1.5)

    # return to the initial position
    neutral_position(reachy)
