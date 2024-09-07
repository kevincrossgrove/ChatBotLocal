# Chat Bot Local

This is a simple [streamlit](https://streamlit.io/) app that allows you to chat with a local LLM using [Ollama](https://ollama.com/).

1. Install [Ollama](https://ollama.com/)
2. Install your model of choice by running:<br/>
`ollama run <model name>` 
<br/>Once installed, that will start a server with your LLM running, on port 11434.
3. Assume you have python already setup, install dependencies by running<br/> `pip install -r requirements.txt`
4. Start up the streamlit app by running `streamlit run main.py` It will be available at [localhost:8501](http://localhost:8501)
