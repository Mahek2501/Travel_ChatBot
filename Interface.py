import streamlit as st

# Load and execute the code from App.py
with open("App.py", "r") as file:
    exec(file.read())

# Streamlit Application
st.title("TravelBot Chat")

# Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display Chat History
st.markdown("### Chat History")
for sender, message in st.session_state.chat_history:
    if sender == "User":
        st.markdown(f"**{sender}:** {message}")
    else:
        st.markdown(f"_{sender}:_ {message}")

# User Input
user_message = st.text_input("Type your message below:", key="user_message")

if st.button("Submit"):
    if user_message:
        # Append user message to chat history
        st.session_state.chat_history.append(("User", user_message))
        # Generate a response and append it to chat history
        bot_response = get_response(user_message)
        st.session_state.chat_history.append(("TravelBot", bot_response))

# Button to Clear Chat History
if st.button("Reset Chat"):
    st.session_state.chat_history.clear()
