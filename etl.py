import os
import streamlit as st
import time
import faiss
import pickle
from dotenv import load_dotenv

from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chat_models import ChatOpenAI

# 🔹 Load API Keys from Environment
load_dotenv()  # Make sure you have a .env file with OPENAI_API_KEY

# 🔹 Initialize OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("⚠️ Missing OpenAI API Key. Set it using `export OPENAI_API_KEY='your_key'` or `.env` file.")
    st.stop()

# 🔹 Title
st.title("📰 NewsBot: AI-Powered News Research Tool 📈")

# 🔹 Sidebar: URL Input
st.sidebar.title("🔗 News Article URLs")
urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}", key=f"url_{i}")
    if url:
        urls.append(url)

process_url_clicked = st.sidebar.button("🚀 Process URLs")
file_path = "faiss_store_openai"

main_placeholder = st.empty()

# 🔹 Initialize LLM (OpenAI ChatGPT)
llm = ChatOpenAI(model_name="gpt-4", temperature=0.7, openai_api_key=OPENAI_API_KEY)

if process_url_clicked:
    if not urls:
        st.sidebar.error("⚠️ Please enter at least one URL before processing.")
    else:
        # Load data
        loader = UnstructuredURLLoader(urls=urls)
        main_placeholder.text("⏳ Loading data from URLs...")
        data = loader.load()

        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        main_placeholder.text("🔄 Splitting text into smaller chunks...")
        docs = text_splitter.split_documents(data)

        # Generate embeddings & store in FAISS
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        vectorstore_openai = FAISS.from_documents(docs, embeddings)
        main_placeholder.text("✅ FAISS Embeddings Created & Stored!")

        # Save FAISS index
        vectorstore_openai.save_local(file_path)
        time.sleep(2)

# 🔹 Question Input Box
query = st.text_input("🔍 Ask a Question:")

if query:
    if not os.path.exists(file_path):
        st.error("⚠️ FAISS index not found! Please process URLs first.")
    else:
        # Load FAISS Index
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        vectorstore = FAISS.load_local(file_path, embeddings, allow_dangerous_deserialization=True)

        # Create Retrieval Chain
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())

        # Perform Query
        result = chain({"question": query}, return_only_outputs=True)

        # Display Answer
        st.header("🤖 AI Answer:")
        st.write(result["answer"])

        # Display Sources
        sources = result.get("sources", "")
        if sources:
            st.subheader("🔗 Sources:")
            for source in sources.split("\n"):
                if source.strip():
                    st.markdown(f"📌 [Relevant Source]({source.strip()})")
