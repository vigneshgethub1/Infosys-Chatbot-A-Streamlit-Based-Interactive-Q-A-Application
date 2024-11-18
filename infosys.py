import streamlit as st

# Knowledge base for Infosys chatbot
infosys_data = {
    "what is infosys": "Infosys is a global leader in consulting, technology, outsourcing, and next-generation digital services. It was founded in 1981 and is headquartered in Bangalore, India.",
    "when was infosys founded": "Infosys was founded on July 2, 1981.",
    "who is the ceo of infosys": "As of the latest information, the CEO of Infosys is Salil Parekh.",
    "what services does infosys offer": "Infosys offers services in areas such as cloud, data and analytics, digital transformation, cybersecurity, and more.",
    "where is infosys headquartered": "Infosys is headquartered in Bangalore, India.",
    "infosys revenue": "Infosys reported annual revenue of over $16 billion USD for the financial year 2022-2023.",
    "infosys recent news": "Infosys has been focusing on expanding its digital services and recently made significant investments in AI and cloud technology.",
    "infosys achievements": "Infosys has received numerous awards for its innovation in digital transformation and has been recognized as a top employer globally.",
    "infosys clients": "Infosys works with clients in various sectors including finance, healthcare, manufacturing, and retail across over 50 countries."
}

# Enhanced response matching function
def get_infosys_response(user_input):
    # Standardize the user input
    user_input = user_input.lower().strip()
    
    # Attempt to find an exact or close match for the question
    for key in infosys_data:
        if key in user_input:
            return infosys_data[key]
    
    # Try to give a broader response if there's no exact match
    if "infosys" in user_input:
        return "Infosys is a globally recognized leader in technology, digital transformation, and consulting. Can I help you with something specific about their services or achievements?"
    if "achievements" in user_input:
        return "Infosys has received numerous awards for its innovation in digital transformation and has been recognized as a top employer globally."

    # Default response if no match is found
    return "I'm here to help with Infosys-related questions. Could you please clarify or ask about Infosys' services, history, or recent activities?"

# Streamlit app layout
st.title("Infosys Chatbot")
st.write("Ask me anything about Infosys! Type your question below and press Enter.")

# Store conversation history in session state
if "history" not in st.session_state:
    st.session_state.history = []

# Display chat history
for i, (user, bot) in enumerate(st.session_state.history):
    st.write(f"You: {user}")
    st.write(f"Chatbot: {bot}")

# User input text box
user_input = st.text_input("You:", "")

# Process user input
if user_input:
    # Get chatbot response
    response = get_infosys_response(user_input)
    
    # Append the current interaction to the session history
    st.session_state.history.append((user_input, response))
    
    # Display the chatbot response
    st.write("Chatbot:", response)
