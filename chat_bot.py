def bot(message):
    answer = "I'm not sure how to respond to that."
    return answer


def main():
    user_input = input("Ask me anything: ")
    bot_response = bot(user_input)
    print(bot_response)


if __name__ == "__main__":
    main()
