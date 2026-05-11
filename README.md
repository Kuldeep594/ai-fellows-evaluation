
# CeRAI AI Evaluation – Option A

This repository contains my submission for the AI Fellows India technical assignment. I evaluated the **Llama 3.2 3B** conversational model using a workflow that combines the CeRAI AI Evaluation Tool (for test data management) and direct API calls (to work around an unresolved executor issue).

## Quick Links
- Live report: `docs/index.html` (open in a browser or serve locally)
- Raw responses: `responses.json` (Fluency prompts), `healthcare_responses.json` (Healthcare prompts)

## Setup
1. Install [Anaconda](https://www.anaconda.com/).
2. Create environment: `conda create -n aieval python=3.10 -y && conda activate aieval`
3. Install dependencies from the CeRAI tool: `pip install -r AIEvaluationTool-1.2/requirements.txt` (update path if needed)
4. Install Ollama and pull the model:
ollama pull llama3.2:3b
ollama serve # keep running

text
5. (Optional) To explore the CeRAI pipeline, the tool’s code is in `AIEvaluationTool-1.2/`.

## How to reproduce the evaluation
### Direct API evaluation (used for final scores)
1. Activate the environment: `conda activate aieval`
2. Run the Healthcare script:
python send_healthcare_prompts.py

text
3. Run the Fluency script:
python send_prompts.py (if you kept the original version, or modify the list inside)

text
These scripts send the prompts to `http://localhost:11434/api/generate` and save the responses as JSON files.
4. Open `docs/index.html` to see the scores and interpretation.

### Attempted CeRAI pipeline (partially working)
- The database was initialised with `src/app/importer/main.py`
- Interface Manager was started with `src/app/interface_manager/main.py`
- Executor ran but always reported `No response received from the agent`. This is a known issue with the local API provider that I could not resolve in the given time.

## Repository contents
- `send_healthcare_prompts.py` — Healthcare prompt set + API call script
- `healthcare_responses.json` — Model responses for healthcare
- `send_prompts.py` — Fluency prompt set + API call script
- `responses.json` — Model responses for fluency
- `docs/index.html` — Self‑contained evaluation report
- `AIEvaluationTool-1.2/` — The CeRAI tool, with config changes committed for reference
- `data/` — SQLite database + imported test data
- `.env` and other config files — Show the environment fixes applied

## Honest account
The CeRAI tool’s executor repeatedly failed to get a response from my locally served model, despite correct configuration. I filed issues and attempted debugging but ultimately switched to a simplified direct‑call approach to meet the assignment deadlines. The report fully documents this and still presents a complete, scored evaluation.
