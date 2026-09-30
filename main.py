import os
from google.colab import userdata
from groq import Groq

MY_API_KEY = userdata.get('GROQ_API_KEY')
client = Groq(api_key=MY_API_KEY)

def run_colab_chat():
    # 2. FIX: Dictionary keys and string values must be wrapped in quotes
    system_message = {
        "role": "system",
        "content": "you need to help in everything be kind and enjoy!."
    }
    
    conversation_history = []
    print("🤖 Google Colab Chatbot Ready! (Type 'exit' to quit)")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
            
        conversation_history.append({"role": "user", "content": user_input})
        
        # Floating window memory (keeps last 6 messages)
        if len(conversation_history) > 6:
            conversation_history = conversation_history[-6:]
            
        messages_to_send = [system_message] + conversation_history
        
        try:
            # FIX: Switched to a valid Groq Qwen model string
            chat_completion = client.chat.completions.create(
                messages=messages_to_send,
                model="qwen/qwen3.8-27b",  # Alternatively, use "qwen/qwen3-32b"
            )
            
            bot_response = chat_completion.choices[0].message.content
            print(f"\nBot: {bot_response}")
            conversation_history.append({"role": "assistant", "content": bot_response})
            
        except Exception as e:
            print(f"\nAPI Error: {e}")

# Run the function
run_colab_chat()
