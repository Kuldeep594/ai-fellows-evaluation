
markdown
# AI Fellows India – Technical Assignment Submission

## 1. Repository URL
https://github.com/Kuldeep594/ai-fellows-evaluation  ← replace with your actual URL

## 2. Live Endpoint URL
https://Kuldeep594.github.io/ai-fellows-evaluation/


*If the endpoint is not yet live, open the report locally:*
```bash
cd docs
python -m http.server 8080
Then visit http://localhost:8080

3. Path Chosen – Option A
I selected Option A (Evaluate & Report) because I wanted to work directly with a live conversational endpoint and build a meaningful test suite around real‑world metrics. After installing the CeRAI evaluation tool, I imported test data and tried to run the automated pipeline. The Interface Manager repeatedly failed to retrieve responses from my locally served Llama model, which blocked the automatic execution and analysis. Because the assignment explicitly states that a documented attempt with clear breakdown is better than nothing, I decided to continue the evaluation manually. I kept the tool’s test plan and database structure for prompt selection, then sent those prompts to the model via direct Ollama API calls. I scored the responses by hand against the chosen metrics and documented both the working parts and the failures. This approach gave me a complete, interpretable set of results and an honest account of what the tool can and cannot do today.

4. AI Use in the Assignment
I used AI assistants (ChatGPT / Claude) throughout the assignment to:

Understand the tool’s documentation – breaking down the multi‑step workflow and mapping it to my Windows environment.

Debug configuration errors – for example, when the importer threw a UnicodeDecodeError, the AI suggested adding encoding='utf-8' to the Python file; I applied the fix myself.

Generate report scaffolding – the HTML structure and the JSON‑LD block were drafted with AI help, then I filled in the actual scores and interpretations.

Course‑correct when the pipeline broke – the AI helped brainstorm why the Interface Manager was timing out, but after trying the suggested fixes without success, I made the decision to switch to a direct API evaluation. I wrote the send_healthcare_prompts.py script myself, adapting a template the AI provided.

Every command was executed by me in my own terminal, every configuration file was manually edited and tested, and all the final scores and justifications are my own. I only used AI to speed up boilerplate tasks and to bounce debugging ideas.
