from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose

with ReachyMini() as reachy:

    def movement_no():
        right = create_head_pose(yaw=17)
        left = create_head_pose(yaw=-17)
        return right, left

    # the initial position
    reachy.goto_target(head=create_head_pose(), antennas=[0, 0])

    # NO
    right, left = movement_no()

    # move head to the right and then to the left
    reachy.goto_target(head=right, antennas=[0.5, -0.5])
    reachy.goto_target(head=left, antennas=[-0.5, 0.5])
    reachy.goto_target(head=right, antennas=[0.5, -0.5])

    # return to the initial position
    reachy.goto_target(head=create_head_pose(), antennas=[0, 0])
