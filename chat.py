import openai
import os

# Установите ваш API-ключ OpenAI
openai.api_key = ""

def ask_openai(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": question}
            ],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"

def main():
    while True:
        question = input("Введите ваш вопрос (или 'exit' для выхода): ")
        if question.lower() == "exit":
            print("Выход из программы.")
            break
        answer = ask_openai(question)
        print("Ответ:", answer)

if __name__ == "__main__":
    main()
