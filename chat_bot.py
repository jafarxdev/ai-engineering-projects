import dotenv
import os

dotenv.load_dotenv()

os.getenv('GROQ_API_KEY')

def bot(message):
    answer = "bot: hello: how can I help you?"
    return answer

def main():
    user_input = input("Ask something: ")
    bot_response = bot(user_input)
    print(bot_response)


if __name__ == "__main__":
    main()


