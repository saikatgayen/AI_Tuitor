from ollama import chat

print("AI Study Helper")
print("Type 'exit' to quit.\n")

while True:
    question = input("Ask a study question: ")

    if question.lower() == "exit":
        print("Good luck with your studies! ")
        break

    response = chat(
        model="llama3",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    answer = response["message"]["content"]
    print("\n Answer:\n")
    print(answer)
    print("\n" + "-" * 147 + "\n")

