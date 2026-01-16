import threading
import time
from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose

from gpt_interaction import ask_gpt
from movement import movement_talking
from speech import speak


with ReachyMini() as reachy:

    while True:
        user_input = input("You: ").lower().strip()
        if user_input == "quit":
            print("Reachy: Goodbye!")
            break

        reply = ask_gpt(user_input)
        print(f"Reachy: {reply}")

        # Speech runs in background
        speech_thread = threading.Thread(target=speak, args=(reply,))
        speech_thread.start()

        # Talking movement runs while speech is active
        while speech_thread.is_alive():
            movement_talking(reachy)
            time.sleep(0.05)  # small pause to avoid jitter

        # Small pause, then return to neutral
        time.sleep(0.2)
        reachy.goto_target(head=create_head_pose(), antennas=[0, 0])
