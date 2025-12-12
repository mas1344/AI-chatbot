import streamlit as st
import requests
from pathlib import Path
import requests
from dotenv import load_dotenv
import os 

load_dotenv()
url = f"https://chatbot-mas.azurewebsites.net/rag/query?code={os.getenv('FUNCTION_APP_API')}"


ASSETS_PATH = Path(__file__).absolute().parents[1] / "assets"

def layout():

    st.markdown("# chatbot")
    st.markdown("Ask a question about data engineering courses")
    text_input = st.text_input(label="Ask a questions")

    if st.button("Send") and text_input.strip() != "":
        response = requests.post(
            url, json={"prompt": text_input}
        )

        data = response.json()

        st.markdown("## Question:")
        st.markdown(text_input)

        st.markdown("## Answer:")
        st.markdown(data["answer"])

        st.markdown("## Source:")
        st.markdown(data["filepath"])
 
        st.image(ASSETS_PATH / f"{data['filename']}.png")

if __name__ == "__main__":
    layout()