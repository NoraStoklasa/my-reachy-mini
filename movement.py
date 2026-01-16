from reachy_mini.utils import create_head_pose

# Explicit duration for clarity (default is 0.5)


def neutral_position(reachy):
    # Neutral position
    reachy.goto_target(head=create_head_pose(), duration=0.5, antennas=[0, 0])


def movement_yes(reachy):
    nod_down = create_head_pose(pitch=17)

    # YES
    reachy.goto_target(head=nod_down, duration=0.5, antennas=[0.3, 0.3])

    # return to the initial position
    neutral_position(reachy)


def movement_no(reachy):
    right = create_head_pose(yaw=17)
    left = create_head_pose(yaw=-17)

    # move head to the right and then to the left
    reachy.goto_target(head=right, antennas=[0.5, -0.5], duration=0.5)
    reachy.goto_target(head=left, antennas=[-0.5, 0.5], duration=0.5)
    reachy.goto_target(head=right, antennas=[0.5, -0.5], duration=0.5)

    # return to the initial position
    neutral_position(reachy)


def hello(reachy):
    tilt_pose = create_head_pose(pitch=-10, roll=15, mm=True)

    reachy.goto_target(
        head=tilt_pose, antennas=[0.5, -0.5], duration=0.5, body_yaw=0.17
    )

    reachy.goto_target(
        head=tilt_pose, antennas=[-0.5, 0.5], duration=0.5, body_yaw=-0.17
    )

    # return to the initial position
    neutral_position(reachy)


def look_up(reachy):
    up = create_head_pose(pitch=-15, roll=15, degrees=True)
    reachy.goto_target(head=up, antennas=[-0.3, 0.3], duration=1.2)
    neutral_position(reachy)


def look_down(reachy):
    down = create_head_pose(pitch=15, degrees=True)
    reachy.goto_target(head=down, antennas=[0.3, -0.3], duration=1.1)
    neutral_position(reachy)
