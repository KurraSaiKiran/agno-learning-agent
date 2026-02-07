import streamlit as st
import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from openai import OpenAI
import time

# Load environment variables from .env file
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Agno Learning Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for ChatGPT-like interface
st.markdown("""
<style>
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .user-message {
        background-color: #f0f4f8;
        border-left: 4px solid #007bff;
        margin-left: 2rem;
    }
    .assistant-message {
        background-color: #ffffff;
        border-left: 4px solid #28a745;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .message-header {
        font-weight: bold;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
    }
    .user-header {
        color: #007bff;
    }
    .assistant-header {
        color: #28a745;
    }
    .message-content {
        line-height: 1.6;
        color: #333333;
    }
    .stTextInput > div > div > input {
        font-size: 16px;
    }
    .sidebar-content {
        padding: 1rem;
    }
    .info-box {
        background-color: #e9ecef;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .error-box {
        background-color: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #f5c6cb;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #c3e6cb;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'agent' not in st.session_state:
    st.session_state.agent = None

def initialize_agent():
    """Initialize the Agno agent (simplified since we use OpenAI client directly for responses)"""
    try:
        # Check for API key
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            st.error("Please set your GROQ_API_KEY environment variable")
            return None
        
        # Create a basic agent for potential future use
        # We'll use the OpenAI client directly for actual responses
        agent = Agent(
            model=OpenAIChat(
                id="llama-3.3-70b-versatile",
                api_key=api_key,
                base_url="https://api.groq.com/openai/v1"
            ),
            markdown=True,
        )
        return agent
    except Exception as e:
        # Even if agent initialization fails, we can still use OpenAI client directly
        st.warning(f"Agent initialization warning: {str(e)}")
        return "fallback"

def display_message(role, content, timestamp=None):
    """Display a chat message with proper styling"""
    message_class = "user-message" if role == "user" else "assistant-message"
    header_class = "user-header" if role == "user" else "assistant-header"
    header_text = "You" if role == "user" else "Agno Agent"
    
    st.markdown(f"""
    <div class="chat-message {message_class}">
        <div class="message-header {header_class}">
            <span>👤</span> {header_text}
            {f'<span style="margin-left: auto; font-size: 0.8rem; color: #6c757d;">{timestamp}</span>' if timestamp else ''}
        </div>
        <div class="message-content">
            {content}
        </div>
    </div>
    """, unsafe_allow_html=True)

def get_agent_response(agent, user_input):
    """Get response from the agent using OpenAI API directly"""
    try:
        # Convert to lowercase for case-insensitive matching
        user_input_lower = user_input.lower()
        
        # Check for "who is saikiran" type queries
        saikiran_keywords = [
            "who is saikiran",
            "who is sai kiran",
            "tell me about saikiran",
            "tell me about sai kiran",
            "what do you know about saikiran",
            "what do you know about sai kiran",
            "information about saikiran",
            "information about sai kiran"
        ]
        
        if any(keyword in user_input_lower for keyword in saikiran_keywords):
            return "Saikiran is a final-year BTech Computer Science student with a strong interest in frontend development and AI-driven applications. He enjoy building real-world projects using modern web technologies and exploring how AI can solve practical problems"
        
        # Check for creator/boss related queries
        creator_keywords = [
            "who implemented you",
            "who created you",
            "who made you",
            "who built you",
            "who developed you",
            "who is your creator",
            "who is your developer",
            "who is your boss",
            "who is your owner",
            "who programmed you",
            "who designed you"
        ]
        
        # Check if any creator keyword is in the user input
        if any(keyword in user_input_lower for keyword in creator_keywords):
            return "I was implemented by Sai Kiran."
        
        # Use OpenAI client directly to get the response
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            return "Please set your GROQ_API_KEY environment variable to use the agent."
        
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1"
        )
        
        # Prepare messages including conversation history
        messages = []
        # Add previous conversation context
        for msg in st.session_state.messages[-10:]:  # Last 10 messages for context
            if msg["role"] == "user":
                messages.append({"role": "user", "content": msg["content"]})
            elif msg["role"] == "assistant":
                messages.append({"role": "assistant", "content": msg["content"]})
        
        # Add current user message
        messages.append({"role": "user", "content": user_input})
        
        # Get response from API
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=1024
        )
        
        # Extract the response text
        if response.choices and response.choices[0].message:
            return response.choices[0].message.content.strip()
        else:
            return "I couldn't generate a response. Please try again."
            
    except Exception as e:
        return f"Error getting response: {str(e)}"

# Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.title("🤖 Agno Agent")
    
    # Initialize agent automatically
    if st.session_state.agent is None:
        with st.spinner("Initializing agent..."):
            st.session_state.agent = initialize_agent()
            if st.session_state.agent:
                st.markdown('<div class="success-box">Agent ready! Start chatting below.</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="error-box">Failed to initialize agent. Please refresh the page.</div>', unsafe_allow_html=True)
    st.subheader("Model Info")
    st.info("""
    **Model**: llama-3.3-70b-versatile
    **Provider**: Groq
    **Capabilities**: 
    - Conversation memory
    - Context understanding
    - Natural language processing
    """)
    
    st.markdown("---")
    
    # Controls
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    
    with col2:
        st.caption("Model: llama-3.3-70b-versatile")
    
    st.markdown("---")
    
    # Instructions
    st.subheader("How to Use")
    st.markdown("""
    1. Type your message in the input box
    2. Press Enter or click Send
    3. The agent will remember your conversation
    4. Use Clear Chat to start fresh
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Main chat interface
st.title("💬 Agno Learning Agent")
st.markdown("Ask me anything! I'll remember our conversation and provide helpful responses.")

# Display chat history
chat_container = st.container()
with chat_container:
    if st.session_state.messages:
        for message in st.session_state.messages:
            display_message(message["role"], message["content"], message.get("timestamp"))
    else:
        st.info("👋 Welcome! Start a conversation by typing a message below.")

# Input area
st.markdown("---")
prompt = st.chat_input("Type your message here...")

if prompt:
    # Check if agent is initialized (or fallback is available)
    if not st.session_state.agent:
        st.error("Agent is not initialized. Please refresh the page!")
        st.stop()
    
    # Add user message to history
    user_message = {
        "role": "user",
        "content": prompt,
        "timestamp": time.strftime("%H:%M")
    }
    st.session_state.messages.append(user_message)
    
    # Display user message immediately
    display_message("user", prompt, user_message["timestamp"])
    
    # Show processing indicator
    with st.spinner("Thinking..."):
        try:
            # Get agent response
            response = get_agent_response(st.session_state.agent, prompt)
            
            # Add assistant response to history
            assistant_message = {
                "role": "assistant",
                "content": response,
                "timestamp": time.strftime("%H:%M")
            }
            st.session_state.messages.append(assistant_message)
            
            # Display assistant response
            display_message("assistant", response, assistant_message["timestamp"])
            
        except Exception as e:
            error_message = f"Sorry, I encountered an error: {str(e)}"
            st.markdown(f'<div class="error-box">{error_message}</div>', unsafe_allow_html=True)
            
            # Add error to history
            error_entry = {
                "role": "assistant",
                "content": error_message,
                "timestamp": time.strftime("%H:%M")
            }
            st.session_state.messages.append(error_entry)

# Auto-scroll to bottom
st.markdown("""
<script>
    var chatContainer = document.querySelector('.main > .block-container');
    chatContainer.scrollTop = chatContainer.scrollHeight;
</script>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Powered by Agno and Groq | Built with Streamlit")