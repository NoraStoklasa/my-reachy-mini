from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose

from movement import look_up, look_down, unsure
from feelings import happy, sad, surprised

with ReachyMini() as reachy:

    surprised(reachy)
