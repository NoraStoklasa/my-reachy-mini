from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose

from movement import look_up, look_down

with ReachyMini() as reachy:

    look_up(reachy)
    look_down(reachy)
