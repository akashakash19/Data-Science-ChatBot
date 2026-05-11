import streamlit as st
import google.generativeai as genai

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
st.markdown(
    '<div class="title">🤖 Data Science AI Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Learn Python, AI, ML, Pandas, Statistics and more with simple explanations</div>',
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙ Settings")

api_key = st.sidebar.text_input(
    "AIzaSyBsktKu4oXs85fXF-wlNZq2C3NegI83cus",
    type="password"
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
## 📚 Topics Covered

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
- Data Visualization
- Data Cleaning
""")

st.sidebar.markdown("---")

st.sidebar.info(
    "💡 Ask beginner-friendly Data Science questions."
)

# ---------------- KNOWLEDGE BASE ----------------
kb = """
Python is a beginner-friendly programming language used in Data Science.

NumPy is used for numerical computing and arrays.

Pandas helps with data analysis and data cleaning.

Statistics helps understand data using mean, median, probability, and standard deviation.

Machine Learning allows systems to learn patterns from data.

Deep Learning uses neural networks with many hidden layers.

NLP helps computers understand human language.

FastAPI is used to build fast Python APIs.

SQL is used to manage databases.
"""

# ---------------- SYSTEM PROMPT ----------------
prompt = f"""
You are an intelligent Data Science AI Assistant.

Your job is to explain Data Science concepts in very simple English.

RULES:
- Explain step-by-step
- Keep answers beginner friendly
- Give real-world examples
- Give Python examples when needed
- Explain formulas clearly
- Be friendly and helpful
- If user asks coding questions, provide clean code
- Keep answers concise but understandable

Topics:
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
- Data Visualization
- AI Chatbots

Knowledge Base:
{kb}
"""

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- DISPLAY CHAT HISTORY ----------------
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        if msg["role"] == "user":
            st.markdown(
                f"<div class='user-box'>{msg['content']}</div>",
                unsafe_allow_html=True
            )

        else:
            st.markdown(
                f"<div class='bot-box'>{msg['content']}</div>",
                unsafe_allow_html=True
            )

# ---------------- USER INPUT ----------------
user_input = st.chat_input(
    "Ask any Data Science question..."
)

# ---------------- AI RESPONSE ----------------
if user_input:

    # Store User Message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(
            f"<div class='user-box'>{user_input}</div>",
            unsafe_allow_html=True
        )

    # Check API Key
    if not api_key:

        st.error("⚠ Please enter your Gemini API Key in sidebar.")

    else:

        try:

            # Configure Gemini
            genai.configure(api_key=api_key)

            # Load Gemini Model
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

            # Display Bot Response
            with st.chat_message("assistant"):
                st.markdown(
                    f"<div class='bot-box'>{bot_reply}</div>",
                    unsafe_allow_html=True
                )

        except Exception as e:

            st.error(f"❌ Error: {e}")

# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown(
    "<center>🚀 Built with Streamlit + Gemini AI</center>",
    unsafe_allow_html=True
)