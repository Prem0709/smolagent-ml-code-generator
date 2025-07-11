```markdown
# 🤖 smolagent-ml-code-generator

An intelligent ML code generation tool powered by **SmolAgent** and **Gemini 1.5 Flash** that transforms natural language instructions into clean, executable Python code for machine learning tasks.

## 🚀 Features

- 🧠 Accepts plain English prompts to describe ML tasks
- 📁 Supports CSV dataset upload
- 🔍 Auto-analyzes data and generates preprocessing, model training, and evaluation code
- 📊 Outputs performance metrics like RMSE or accuracy
- 💾 Saves each session’s output as a uniquely named `.py` file
- 🖥️ Easy-to-use Gradio interface
- 🧰 Built using SmolAgents, LiteLLM, Gradio, and Gemini 1.5 Flash

## 📸 Demo

![App Screenshot](https://raw.githubusercontent.com/Prem0709/smolagent-ml-code-generator/main/assets/demo_screenshot.png)  
*Generate ML code in seconds with just a prompt!*

## 📂 Project Structure

```

smolagent-ml-code-generator/
│
├── app.py                   # Main Gradio application
├── generated\_code/          # Folder to store generated Python files
├── requirements.txt         # Python dependencies
├── README.md                # Project overview
└── .gitignore               # Git ignore rules

````

## ⚙️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/Prem0709/smolagent-ml-code-generator.git
cd smolagent-ml-code-generator

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Set your Gemini API key
export GOOGLE_API_KEY=your-gemini-api-key
# or on Windows:
# set GOOGLE_API_KEY=your-gemini-api-key

# Run the app
python app.py
````

## 📥 Example Prompt

> `Train a regression model to predict diabetes progression. Evaluate RMSE and select top 3 features.`

## 📘 License

This project is open source under the [MIT License](LICENSE).

---


## 🔗 Connect

* [LinkedIn](https://www.linkedin.com/in/premkumar-pawar0709)

```


