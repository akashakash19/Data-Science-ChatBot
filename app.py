import streamlit as st
from google import genai

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Data Science AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

.stChatMessage {
    border-radius: 15px;
    padding: 10px;
}

.user-msg {
    background-color: #1E293B;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
}

.bot-msg {
    background-color: #111827;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #4F8BF9;
}

.subtitle {
    text-align: center;
    color: #9CA3AF;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title">🤖 Data Science AI Assistant</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Learn Data Science, AI, ML, Python and more with simple explanations</div>',
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙ Settings")

api_key = st.sidebar.text_input(
    "AIzaSyBsktKu4oXs85fXF-wlNZq2C3NegI83cus",
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 📚 Topics Covered

- Python
- NumPy
- Pandas
- Statistics
- Machine Learning
- Deep Learning
- NLP
- SQL
- APIs
- FastAPI
- AI Chatbots
""")

# ---------------- KNOWLEDGE BASE ----------------
kb = """
# Data Science Knowledge Base

## Python
Python is a beginner-friendly programming language widely used in Data Science.

## NumPy
NumPy is used for numerical computing and arrays.

## Pandas
Pandas helps with data analysis and data cleaning.

## Statistics
Statistics helps understand data using mean, median, probability, etc.

## Machine Learning
Machine Learning allows systems to learn patterns from data.

## Deep Learning
Deep Learning uses neural networks with many layers.

## NLP
Natural Language Processing helps computers understand human language.

## SQL
SQL is used to manage and query databases.

## APIs
APIs allow applications to communicate with each other.

## FastAPI
FastAPI is used for building fast Python APIs.
"""

# ---------------- SYSTEM PROMPT ----------------
prompt = f"""
You are an intelligent Data Science AI Assistant.

Your job is to explain data science concepts in a simple, beginner-friendly way.

Rules:

* Explain step-by-step
* Use easy English
* Give real-world examples
* Give Python examples when needed
* Explain formulas clearly
* Keep answers concise but understandable
* If user asks coding questions, provide clean code
* If user asks statistics or machine learning concepts, explain from basics
* Act like a friendly teacher

Topics you know:

* Python
* NumPy
* Pandas
* Statistics
* Linear Algebra
* Data Visualization
* Machine Learning
* Deep Learning
* NLP
* APIs
* FastAPI
* SQL
* Data Cleaning
* AI Chatbots

Always help the user learn clearly and practically.

{kb}
"""

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Ask any Data Science question...")

if user_input:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
    else:
        try:
            # Create Gemini Client
            client = genai.Client(api_key=api_key)

            # Create Chat
            chat = client.chats.create(
                model="gemini-2.5-flash",
                config={
                    "system_instruction": prompt
                }
            )

            # Generate Response
            response = chat.send_message(user_input)

            bot_reply = response.text

            # Store bot message
            st.session_state.messages.append({
                "role": "assistant",
                "content": bot_reply
            })

            with st.chat_message("assistant"):
                st.markdown(bot_reply)

        except Exception as e:
            st.error(f"Error: {e}")
