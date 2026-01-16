# Reachy Mini – Conversational Robot (Python)

This project controls **Reachy Mini** using Python.
Reachy listens to text input, replies using GPT, speaks the reply out loud, and moves naturally while talking.

It currently works with:

- Reachy Mini SDK / simulator
- OpenAI API (for text + speech)

---

## What this project does

1. You type a message in the terminal
2. GPT generates a short, playful reply
3. Reachy:
   - speaks the reply
   - moves its head, body, and antennas while talking
   - returns to a neutral position afterwards

You can also trigger **emotions and gestures** such as:

- happy
- sad
- surprised
- yes / no
- listening
- unsure

---

## Project structure

```

.
├── main.py              # Main loop (conversation + movement + speech)
├── gpt_interaction.py   # GPT text responses
├── speech.py            # Text-to-speech playback
├── movement.py          # Head, body, antenna movements
├── feelings.py          # Emotional expressions
├── interaction.py       # Simple input/output test loop
├── .env                 # OpenAI API key (not committed)
└── README.md

```

---

## Requirements

- Python 3.10+
- Reachy Mini SDK (or simulator)
- OpenAI API key

Python libraries used:

- `openai`
- `python-dotenv`
- `sounddevice`
- `soundfile`

---

## Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:

```

pip install openai python-dotenv sounddevice soundfile

```

4. Create a `.env` file:

```

OPENAI_API_KEY=your_api_key_here

```

---

## Running the project

Start the main conversation loop:

```

python main.py

```

Type messages in the terminal.
Type `quit` to exit.

---

## Notes

- This project currently uses the **SDK simulator** until physical hardware is connected.
- Movements are intentionally subtle to look natural.
- GPT replies are short by design to match Reachy’s personality.

---

## Future ideas

- Voice input (speech recognition)
- Emotion selection based on GPT response
- Camera input
- Hardware deployment on physical Reachy Mini

```

```
