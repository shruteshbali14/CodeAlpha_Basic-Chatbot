def get_bot_response(user_input):
   
    text = user_input.lower().strip()
    
    # if-elif structure for predefined replies
    if text == "hello":
        return "hi"
    
    elif text == "hi":
        return "hello"
    
    elif text == "how are you":
        return "Iam fine, thanks!"
    
    elif text == "bye":
        return "bye see you again"
    
    elif text == "how do you do":
        return "good doing well"
    
    elif text == "who are you": 
        return "I am a Python chatbot."
    
    elif text == "help":
        return "How can I help you?"    
    
    elif text == "good morning":
        return "Good morning"
    
    elif text == "good afternoon":
        return "good afternoon"
    
    elif text == "good evening":
        return "good evening"
    
    elif text == "good night":
        return "good night"
    
    elif text == "say about you":
        return "Iam a chatbot. I can communicate with humans"
    
    elif text == "what will you do":
        return "This chatbot made by humans \n    chatbot may do some mistakes"
    
    elif  text == "on which programming language will you work":
        return "I will work on any language \n    But now Iam desigined by Python programming language."
        
    
    else:
        return "I don't understand that yet. Try saying 'hello'!"

def start_chat():
    """
    Function to run the main chatbot loop.
    """
    print("Chatbot: Hello! I am a simple chatbot. (Type 'bye' to exit)")
    
    # Loop to keep the conversation going
    while True:
        # Input from user
        user_message = input("You: ")
        
        # Get the response based on the rules
        reply = get_bot_response(user_message)
        
        # Output to user
        print(f"Chatbot: {reply}")
        
        # Exit condition to break the loop
        if user_message.lower().strip() == "bye":
            break

# Run the chatbot
if __name__ == "__main__":
    start_chat()