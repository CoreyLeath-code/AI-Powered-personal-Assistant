"""
main.py — Entry Point
---------------------
Launch the AI-Powered Personal Assistant interactively.
Delegates to assistant/main.py for core logic.
"""

from assistant.main import process_user_input

if __name__ == "__main__":
    print("🤖 AI Assistant (type 'exit' to quit)")
    print("--------------------------------------")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        response = process_user_input(user_input)
        print(f"Assistant: {response}")
