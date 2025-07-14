import os
import pandas as pd
import gradio as gr
import litellm
import datetime
from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel

# ✅ Turn on LiteLLM debug
litellm._turn_on_debug()

# ✅ Set Gemini API key
os.environ["GOOGLE_API_KEY"] = "xfgui-VLc3dE2kEV9wp2EyirnitLvk1w"
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("Please provide a valid Google Gemini API key.")

# ✅ Initialize Gemini model
model = LiteLLMModel(
    model_id="gemini/gemini-1.5-flash",
    api_key=api_key
)

# ✅ Initialize CodeAgent
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
    additional_authorized_imports=[
        'pandas',
        'numpy',
        'sklearn',
        'sklearn.linear_model',
        'sklearn.metrics',
        'sklearn.model_selection',
        'itertools'
    ]
)

# ✅ Ensure folder exists
SAVE_DIR = "generated_code"
os.makedirs(SAVE_DIR, exist_ok=True)

# ✅ Main function
def generate_code(file, user_task):
    try:
        dataset_context = ""

        # Optional: Dataset preview
        if file is not None:
            df = pd.read_csv(file.name)
            dataset_context = f"\nHere are the first few rows of the dataset:\n{df.head(3).to_string()}"

        # Final agent prompt
        full_prompt = f"""
You are an expert AI code assistant generating machine learning code.

Task:
{user_task.strip()}

Use only these libraries: pandas, numpy, sklearn, itertools.
Generate clean Python code for:
- Preprocessing
- Model training (e.g., regression)
- Evaluation (e.g., RMSE or accuracy)
{dataset_context}

Return:
- Python code
- Summary of results (metrics, selected features, etc.)
"""

        # Agent execution
        result = agent.run(full_prompt)

        # Format result
        if isinstance(result, dict):
            code = result.get("code", "")
            summary = "\n".join(f"{k}: {v}" for k, v in result.items() if k != "code")
            final_output = f"{code}\n\n📊 Summary:\n{summary}"
        else:
            code = str(result)
            final_output = code

        # ✅ Create unique filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ml_code_{timestamp}.py"
        filepath = os.path.join(SAVE_DIR, filename)

        # ✅ Save to file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(final_output)

        return final_output, filepath

    except Exception as e:
        return f"❌ Error: {str(e)}", None


# ✅ Gradio UI
iface = gr.Interface(
    fn=generate_code,
    inputs=[
        gr.File(label="📁 Upload Dataset (CSV)", file_types=[".csv"], type="filepath"),
        gr.Textbox(lines=6, label="💡 Describe Your ML Task", placeholder="e.g. Train a regression model and evaluate RMSE.")
    ],
    outputs=[
        gr.Textbox(label="🧠 Generated Python Code + Summary", lines=25, show_copy_button=True),
        gr.File(label="⬇️ Download Generated Code (.py)")
    ],
    title="🧠 ML Code Generator (SmolAgent + Gemini)",
    description="Upload a dataset and describe your ML task. This SmolAgent will generate clean, optimized Python code and save it to a new file each time."
)

# ✅ Launch
if __name__ == "__main__":
    iface.launch(share=True)
