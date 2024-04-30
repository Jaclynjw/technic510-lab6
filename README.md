# technic510-lab5
# English Speaking Practice Tool

This application is designed to help users practice and improve their English speaking skills. It uses OpenAI's GPT-3.5 model to provide two modes of interaction: Spoken Translation and Spoken Dialogue.

## Features

- **Spoken Translation**: Users can enter text in any language, and the app will translate it into natural spoken English.
- **Spoken Dialogue**: Users can have a casual conversation with the AI, which will respond in natural English.

## Enhanced Prompt Engineering

To improve user experience and the quality of AI responses, we've implemented advanced prompt engineering strategies:

- **Contextual Relevance**: The prompts explicitly instruct the AI on the type of English required (American, British, etc.) and the context (informal conversation, technical discussion).
- **Engagement and Continuity**: In conversation mode, the AI is prompted to maintain an engaging and coherent dialogue flow, potentially asking follow-up questions to simulate real-life interactions more closely.
These improvements ensure that the translations are contextually appropriate and the conversations are dynamic and engaging.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Python 3.6 or above.
- You have an OpenAI API key.

## Installing English Speaking Practice Tool

To install English Speaking Practice Tool, follow these steps:

Linux and macOS:

```bash
git clone https://github.com/Jaclynjw/technic510-lab6.git
cd technic510-lab6
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
windows:
```bash
git clone https://github.com/Jaclynjw/technic510-lab6.git
cd technic510-lab6
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
## Using English Speaking Practice Tool

To use English Speaking Practice Tool, follow these steps:

1. Set your OpenAI API key in a .env file:
```bash
OPENAI_API_KEY='your-api-key'
```
2. Run the Streamlit application:
```bash
streamlit run app.py
```
3. Open your web browser and go to http://localhost:8501.
4. Choose the mode you want to use: Spoken Translation or Spoken Dialogue.
5. Enter your text and press the "Submit" button to see the response.

# Learning Reflections

## 1. Integration of OpenAI's GPT-3.5 API

### Key Learnings:
- **API Authentication**: Learned how to securely authenticate API calls using environment variables.
- **API Usage**: Gained experience in using OpenAI's GPT-3.5 API to generate human-like text responses, which was crucial for both the translation and dialogue features.

### Challenges:
- **Rate Limits and Errors**: Encountered and learned to handle API rate limits and error responses effectively.

## 2. Streamlit for Rapid Prototyping

### Key Learnings:
- **UI Development**: Streamlit proved to be an invaluable tool for quick UI development, allowing for real-time previews and easy deployment.
- **State Management**: Learned about `st.session_state` for maintaining state across reruns, which is essential for interactive applications.

### Challenges:
- **Layout Management**: Initially struggled with layout configurations but eventually learned how to use columns and containers to create a user-friendly interface.

## Conclusion

This project not only bolstered my technical skills but also enhanced my problem-solving abilities. It underscored the importance of user-centered design and the effective use of APIs in creating practical tools. The experience has left me better equipped to tackle similar challenges in the future and has sparked a keen interest in exploring more advanced features of AI-driven applications.
