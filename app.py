import time
from study_helper import ai_response, save_notes


#--------TERMINAL BANNER-------------


def print_banner():
     print("\033[96m")
     print("==============================================")
     print("      AI STUDY HELPER  |  LOCAL LLM TOOL       ")
     print("==============================================")
     print("        Powered by Ollama + LLaMA 3            ")
     print("\033[0m")

#----------BOOT SEQUENCE-----------------

def boot_message():
    messages = [
        "[✓] Initializing local LLM (Ollama)",
        "[✓] Loading short-term memory buffer",
        "[✓] Notes system ready",
        "[✓] AI Study Helper started successfully"
    ]

    for msg in messages:
        print("\033[92m" + msg + "\033[0m")
        time.sleep(0.4)

    print("\nType 'exit' to quit.\n")

#----------MAIN PROGRAM---------------

def main():
    print_banner()
    boot_message()

    conversation = []

    while True:
        question = input("Ask a question: ")
	
        if question.lower() == "exit":
                print("\nGood luck with your studies!")
                break

        #-----ADD USER MESSAGE TO MEMORY----------
        conversation.append({"role": "user", "content": question})
	
        #-----GET AI RESPONSE---------------------
        answer, conversation = ai_response(conversation)
	
        #-----ADD ASSSITANT RESPONSE TO MEMORY----
        conversation.append({"role": "assistant", "content": answer})

        #-----SAVE NOTES------------
        save_notes(question, answer)


        #----Print Answer-----------
        print("\n ANSWER:\n ")
        print(answer)
        print("-" * 50)

#-----------Entry point---------------------

if __name__ == "__main__":
    main()
