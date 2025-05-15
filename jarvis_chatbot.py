import aiml


kernel = aiml.Kernel()
kernel.learn("jarvis.aiml")

print("=== Jarvis Chatbot ===")
print("Type something. Type 'exit' to quit.\n")

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    response = kernel.respond(user_input.upper())
    print("Jarvis:", response)
