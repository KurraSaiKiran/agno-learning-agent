# 🤖 Agno Learning Agent

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Groq](https://img.shields.io/badge/Powered%20by-Groq-orange.svg)

**A powerful web-based chat interface for AI conversations, built with Streamlit and powered by Groq's LLaMA 3.3 70B model**

[Features](#features) • [Demo](#demo) • [Installation](#installation) • [Usage](#usage) • [Configuration](#configuration)

</div>

---

## 📋 Overview

Agno Learning Agent is an interactive chatbot application that provides a ChatGPT-like experience using Groq's high-performance LLM API. Built with Streamlit, it offers a clean, responsive interface with conversation memory and context awareness.

## ✨ Features

- 🤖 **ChatGPT-like Interface** - Modern message bubbles with user/assistant distinction
- 💬 **Conversation Memory** - Maintains context across multiple messages
- 🔐 **Secure API Management** - Environment-based API key configuration
- 🎨 **Professional Design** - Custom CSS styling with responsive layout
- ⚡ **Fast Responses** - Powered by Groq's optimized LLM infrastructure
- 📱 **Mobile-Friendly** - Fully responsive design for all devices
- 🕒 **Timestamps** - Track message timing in conversations
- 🔄 **Session Management** - Clear chat and reset functionality

## 🎬 Demo

![Agno Agent Demo](https://via.placeholder.com/800x400?text=Add+Your+Screenshot+Here)

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Groq API key ([Get one here](https://console.groq.com/))

### Quick Start

1. **Clone the repository**

```bash
git clone https://github.com/KurraSaiKiran/Agno-Agent.git
cd Agno-Agent
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Configure API Key**

Create a `.env` file in the project root:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

Or set as environment variable:

```bash
# Windows
set GROQ_API_KEY=your_api_key_here

# Linux/Mac
export GROQ_API_KEY=your_api_key_here
```

4. **Run the application**

```bash
streamlit run app.py
```

5. **Open your browser**

Navigate to `http://localhost:8501`

## 💡 Usage

### Basic Conversation

1. **Start the app** - The agent initializes automatically
2. **Type your message** - Use the chat input at the bottom
3. **Get responses** - The agent responds with context awareness
4. **Continue chatting** - Conversation history is maintained

### Controls

- **Clear Chat** - Remove all messages and start fresh
- **Conversation Context** - Last 10 messages are used for context
- **Timestamps** - Each message shows the time it was sent

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key | Yes |

### Model Configuration

The application uses:
- **Model**: `llama-3.3-70b-versatile`
- **Provider**: Groq
- **Temperature**: 0.7
- **Max Tokens**: 1024
- **Context Window**: Last 10 messages

### Customization

You can modify these settings in `app.py`:

```python
# Change model
model="llama-3.3-70b-versatile"

# Adjust temperature (0.0 - 1.0)
temperature=0.7

# Change max response length
max_tokens=1024

# Modify context window
messages[-10:]  # Last 10 messages
```

## 🛠️ Technical Stack

- **Frontend Framework**: [Streamlit](https://streamlit.io/) 1.29+
- **Agent Framework**: [Agno](https://github.com/agno-ai/agno) 0.1.0+
- **LLM Provider**: [Groq](https://groq.com/)
- **Model**: LLaMA 3.3 70B Versatile
- **API Client**: OpenAI-compatible API
- **Styling**: Custom CSS
- **Configuration**: python-dotenv

## 📁 Project Structure

```
Agno-Agent/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .env                           # Environment variables (create this)
├── .gitignore                     # Git ignore rules
├── README.md                      # Project documentation
└── Building_a_Learning_Agent_using_Agno.ipynb  # Jupyter notebook
```

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| "Please set your GROQ_API_KEY" | Add API key to `.env` file or environment variables |
| "Agent initialization warning" | Check API key validity and internet connection |
| Slow responses | Normal - depends on network and API load |
| Module not found | Run `pip install -r requirements.txt` |
| Port already in use | Change port: `streamlit run app.py --server.port 8502` |

### Getting Help

- Check [Groq Documentation](https://console.groq.com/docs)
- Review [Streamlit Docs](https://docs.streamlit.io/)
- Open an [Issue](https://github.com/KurraSaiKiran/Agno-Agent/issues)

## 🎨 Customization

### Styling

Modify the CSS in `app.py` to change:
- Message bubble colors
- Font styles and sizes
- Layout spacing
- Color scheme

### Features

Extend functionality by:
- Adding file upload capabilities
- Implementing conversation export
- Adding voice input/output
- Creating custom prompts
- Integrating additional tools

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Sai Kiran Kurra**

- GitHub: [@KurraSaiKiran](https://github.com/KurraSaiKiran)
- Project: [Agno-Agent](https://github.com/KurraSaiKiran/Agno-Agent)

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for providing fast LLM inference
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Agno](https://github.com/agno-ai/agno) for the agent framework
- [Meta](https://ai.meta.com/) for the LLaMA model

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⭐ Show your support

Give a ⭐️ if this project helped you!

---

<div align="center">
Made with ❤️ by Sai Kiran Kurra
</div>