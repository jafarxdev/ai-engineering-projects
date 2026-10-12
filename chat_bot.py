def bot(message):
    answer = "Hello dear user, still, I'm not sure how to respond to this question."
    return answer

def main():
    user_input = input("Ask me anything: ")
    bot_response = bot(user_input)
    print(bot_response)


if __name__ == "__main__":
    main()


