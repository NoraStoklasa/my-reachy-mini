from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose


with ReachyMini() as reachy:

    def movement_yes():
        return create_head_pose(pitch=17)

    # the initial position
    reachy.goto_target(head=create_head_pose(), antennas=[0, 0])

    # YES
    reachy.goto_target(head=movement_yes(), antennas=[0.3, 0.3])

    # return to the initial position
    reachy.goto_target(head=create_head_pose(), antennas=[0, 0])
