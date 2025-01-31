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

## 📦 Installation  

### **1️⃣ Install Dependencies**  
Run the following command to install all required Python packages:  
```bash
pip install streamlit langchain langchain-community langchain-openai faiss-cpu sentence-transformers unstructured openai tiktoken dotenv
**🔹 Step 2: Install Dependencies**

Make sure you have Python **3.8+** installed. Then, install the required packages:

bash

CopyEdit

pip install -r requirements.txt

**🔹 Step 3: Set Up OpenAI API Key**

Create a **.env** file in the project root and add your **OpenAI API key**:

makefile

CopyEdit

OPENAI_API_KEY=your_openai_api_key

Or set it manually in your terminal:

bash

CopyEdit

export OPENAI_API_KEY="your_openai_api_key"

**🔹 Step 4: Run the Streamlit App**

bash

CopyEdit
streamlit run app.py

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
