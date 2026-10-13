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

messages = []


def bot(message):
    messages.append({'role': 'user', 'content': message})

    response = llm.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        temperature=0.7,
        max_tokens=220,
    )


    response_text = response.choices[0].message.content
    messages.append({'role': 'assistant', 'content': response_text})

    return response_text


def chat():
    while True:
        try:
            user_input = input('Ask Something: ').strip()

            if user_input.lower() in {"exit", "quit", "q"}:
                print("Goodbye!")
                break

            if not user_input:
                continue

            print("Bot:", bot(user_input), "\n")

        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break


def main():
    chat()
    print("Groq AI Chatbot")
    print("Type 'exit' or 'quit' to stop.\n")
    # print(messages)


if __name__ == "__main__":
    main()
