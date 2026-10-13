import os

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
llm = OpenAI(
    api_key=API_KEY,
    base_url="https://api.groq.com/openai/v1",
)


def bot(message):
    response = llm.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": message}
        ],
        temperature=0.7,
        max_tokens=100,
    )

    return response.choices[0].message.content


def main():
    print("Groq AI Chatbot")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        try:
            user_input = input("Ask Something: ").strip()

            if user_input.lower() in {"exit", "quit"}:
                print("Goodbye!")
                break

            if not user_input:
                continue

            print("Bot:", bot(user_input), "\n")

        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()