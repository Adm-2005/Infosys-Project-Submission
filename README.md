# 💫 Infosys Project Submission

This repository features the final submission for the **AI&ML Internship** program of Infosys Springboard. It includes three subparts: -
- **First-Aid RAG:** A RAG agent that helps to perform immediate first-aid.
- **Pandas Agent:** An AI agent that is used to automated data analysis workflow.
- **SQL Agent:** An AI agent that is used to automate database operations.

## 📁 Project Structure

```bash

Infosys-Project-Submission/
├── agile_docs/
│   ├── Agile_Sprint.xlsx
│   ├── Unit_Test_Plan.xlsx
├── first_aid_rag/
│   ├── data/
│   │   ├── FA-manual.pdf 
│   ├── src/
│   │   ├── __init__.py
│   │   ├── gradio_interface.py
│   │   ├── rag_agent.py
│   ├── app.py
│   ├── requirements.txt
├── pandas_agent/
│   ├── pandas_ai_agent.ipynb
├── sql_agent/
│   ├── sql_ai_agent.ipynb
├── .gitignore
├── LICENSE
├── README.md

```

## 🛠️ Setup Instructions

### **For First-aid RAG,**

1. **Clone the repository**
```bash

git clone https://github.com/Adm-2005/Infosys-Project-Submission

```

2. **Create an environment file**
```bash

GROQ_API_KEY = <your-api-key>

```

3. **Run the application**
```bash

cd first-aid-rag
python app.py

```

Visit http://127.0.0.1:7860/ and use the application.

### **For Pandas Agent,**

Open the ```pandas_ai_agent.ipynb``` notebook on Google Colab or any other interactive notebook platform and run all the cells.

### **For SQL Agent,**

Open the ```sql_ai_agent.ipynb``` notebook on Google Colab or any other interactive notebook platform and run all the cells.