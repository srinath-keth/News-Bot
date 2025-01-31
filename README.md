# 📰 News-Bot: AI-Powered News Research Tool 📈  

RockyBot is an AI-powered **news research tool** that allows users to extract content from news articles, store it in a **vector database (FAISS)**, and use **OpenAI's GPT** to answer user queries based on the extracted data.  

## 🚀 Features  
✅ **Extracts content** from URLs using `UnstructuredURLLoader`  
✅ **Splits text into chunks** for better retrieval  
✅ **Embeds the content** using `OpenAIEmbeddings`  
✅ **Stores embeddings** in a FAISS vector database  
✅ **Retrieves answers** using **OpenAI's GPT (`gpt-4` or `gpt-3.5-turbo`)**  
✅ **Displays relevant source links** along with the answer  
✅ **Fully automated UI** using **Streamlit**  

---
## Installation

1.Clone this repository to your local machine using:

```bash
  git clone https://github.com/codebasics/langchain.git
```
2.Navigate to the project directory:

```bash
  cd 2_news_research_tool_project
```
3. Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```

**⚙️ Tech Stack**

- **Python 3.8+** - Core programming language
- **Streamlit** - UI framework for web-based interaction
- **LangChain** - AI chaining framework
- **FAISS** - Vector database for fast search
- **OpenAI GPT-4** - AI model for Q&A
- **Sentence Transformers** - Text embeddings
- **Unstructured** - URL-based document parsing

**🎯 How It Works**

**1️⃣ Enter News URLs**

Users provide up to **3 article URLs**, which the app processes.

**2️⃣ Extract & Process Content**

- **Scrapes** the content from URLs.
- **Splits** it into smaller chunks.

**3️⃣ Generate Embeddings & Store in FAISS**

- Converts text into **embeddings** using **OpenAI Embeddings**.
- Stores them in a **FAISS index** for fast retrieval.

**4️⃣ Ask Questions & Get AI-Powered Answers**

- Uses **semantic search** to find relevant text.
- Passes the retrieved text to **GPT-4** for answering.
- Displays the **answer & relevant sources**.
**🎯 Future Improvements**

✅ **Support for Multiple AI Models (Claude, Llama-2, etc.)**  
✅ **Automated Data Refresh for News Updates**  
✅ **Integrating Financial APIs for Live Market Data**

**💡 Contributing**

We welcome contributions! To contribute:

1. **Fork** the repository.
2. **Create a new branch** (feature-new).
3. **Commit changes** (git commit -m "Added new feature").
4. **Push to GitHub** (git push origin feature-new).
5. **Create a Pull Request**.
