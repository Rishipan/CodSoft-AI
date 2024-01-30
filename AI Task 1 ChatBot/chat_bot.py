import json

from difflib import get_close_matches


def load_library(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            data: dict = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or has invalid JSON, return an empty dictionary
        data = {"questions": []}
    return data


def save_to_library(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: list[str], questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_answer_for_question(question: str, library: dict) -> str | None:
    for q in library["questions"]:
        if q["question"] == question:
            return q["answer"]


def chat_bot():
    library: dict = load_library('library.json')

    while True:
        user_input: str = input("You: ")

        if user_input.lower() == 'quit':
            break

        best_match: str | None = find_best_match(user_input, [q["question"] for q in library["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, library)
            print(f'Bot: {answer}')
        else:
            print('Bot: Sorry but I dont\'t know the answer. Can you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip: ')

            if new_answer.lower() != 'skip':
                library["questions"].append({"question": user_input, "answer": new_answer})
                save_to_library('library.json', library)
                print('Bot: Thank you! I learned a new response!')


if __name__ == '__main__':
    chat_bot()
