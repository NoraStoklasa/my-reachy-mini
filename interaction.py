while True:
    user_input = input("User: ").strip().lower()
    if user_input == "quit":
        print("Reachy: Goodbye!")
        break

    print(f"Reachy: I heard you say: {user_input}")
