# Slide 9
#import streamlit as st

#with st.chat_message("user"):
#    st.write("Hello 👋")

# Slide 12
#import streamlit as st
#import numpy as np

#with st.chat_message("assistant"):
#    st.write("Hello human")
#    st.bar_chart(np.random.randn(30, 3))

# Slide 15 for input
#import streamlit as st

#prompt = st.chat_input("Say something")
#if prompt:
#    st.write(f"User has sent the following prompt: {prompt}")

#Slide 19 Echo Lab
import streamlit as st

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# Slide 21
# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})




