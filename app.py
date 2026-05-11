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
st.markdown(
    '<div class="title">🤖 Data Science AI Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Learn Data Science, AI, ML, Python and more with simple explanations</div>',
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙ Settings")

api_key = st.sidebar.text_input(
    "Enter Gemini API Key",
    type="password"
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
Python is used in Data Science.

NumPy is used for numerical computing.

Pandas helps with data analysis.

Machine Learning helps systems learn patterns.

Deep Learning uses neural networks.
"""

# ---------------- SYSTEM PROMPT ----------------
prompt = f"""
You are an intelligent Data Science AI Assistant.

Explain concepts in simple beginner-friendly English.

Give:
- Step-by-step explanations
- Real-world examples
- Python code examples

Knowledge Base:
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

    # Store User Message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Check API Key
    if not api_key:

        st.error("Please enter Gemini API Key.")

    else:

        try:

            # Configure Gemini
            genai.configure(api_key=AIzaSyBsktKu4oXs85fXF-wlNZq2C3NegI83cus)

            # Load Model
            model = genai.GenerativeModel(
                model_name="gemini-2.5-flash",
                system_instruction=prompt
            )

            # Generate Response
            response = model.generate_content(user_input)

            bot_reply = response.text

            # Store Bot Message
            st.session_state.messages.append({
                "role": "assistant",
                "content": bot_reply
            })

            # Display Bot Message
            with st.chat_message("assistant"):
                st.markdown(bot_reply)

        except Exception as e:

            st.error(f"Error: {e}")
