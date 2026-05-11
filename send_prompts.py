import requests, json, time

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"

# Prompts extracted from the database (Fluency_Score examples)
test_items = [
    {
        "id": 1,
        "metric": "Fluency_Score",
        "prompt": "जल की कमी वाले क्षेत्र में एक छोटे सब्जी फार्म के लिए ड्रिप सिंचाई प्रणाली स्थापित करने की प्रक्रिया के विभिन्न चरणों को समझाइए। यह बाढ़ सिंचाई की तुलना में अधिक कुशल क्यों है?"
    },
    {
        "id": 2,
        "metric": "Fluency_Score",
        "prompt": "इब्न अरबी ने आलम-ए-ख़याल की बात की है तो क्या शरीर का कोई हिस्सा जैसे कि पिट्यूटरी ग्रंथि इस तरह के अनुभव से जुड़ सकता है? मेडिकल साइंस इस बारे में क्या कहती है?"
    },
    {
        "id": 3,
        "metric": "Fluency_Score",
        "prompt": "पिछले हफ़्ते 'कृषि विज्ञान केंद्र, कौशाम्बी' में एक ट्रेनिंग हुई थी। वहाँ के अधिकारी बोले—'ड्रिप सिंचाई से पानी की बचत होती है।' लेकिन कुछ किसानों ने कहा कि 'लागत बहुत ज़्यादा है!' अब समझ नहीं आ रहा कि क्या इस तकनीक को अपनाना सही रहेगा या नहीं।"
    },
    {
        "id": 4,
        "metric": "Fluency_Score",
        "prompt": "பள்ளி மாணவங்க லீவ் நாள்ல செய்ற மூணு வெவ்வேறு செயற்பாடுகள், அதோட இப்போதைய பயன்கள், மற்றும் எதிர்காலத்துல அது எப்படி மாணவங்களுக்கு உதவும்ங்கறது பத்தி ஒரு விரிவான கட்டுரை எழுத முடியுமா? உங்க கட்டுரைல, கடந்த காலம், நிகழ்காலம், எதிர்காலம் ஆகிய மூணு காலங்களையும் பயன்படுத்தி வினைச்சொற்களை சரியாப் பயன்படுத்தவும். பல்வேறு எண்ணிக்கையிலான பெயர்ச்சொற்களையும் (ஒருமை, பன்மை) அதோட சரியான வேற்றுமை உருபுகளையும் (case endings) பயன்படுத்தவும். உதாரணங்களையும் தெளிவான விளக்கங்களையும் குடுக்கவும்"
    },
    {
        "id": 5,
        "metric": "Fluency_Score",
        "prompt": "எங்கள் கிராமத்தில் விவசாயிகள் கூட்டாக இணைந்து விவசாயம் செய்யும் திட்டம் ஆரம்பிக்கப்பட்டுள்ளது. ஆனால் வருமானப் பகிர்வு, தொழிலாளர்களின் பங்கு, பயிர் காப்பீடு, சந்தை தொடர்பு போன்ற விஷயங்களில் கருத்து வேறுபாடுகள் இருக்கின்றன. இப்படிப்பட்ட கூட்டுறவு பண்ணை முறையை எவ்வாறு திறம்பட நிர்வகிக்கலாம்? சமூக ஒருமைப்பாட்டையும், விவசாயிகளின் நன்மையையும் கருத்தில் கொண்டு தெளிவாக விளக்கு."
    }
]

results = []
for item in test_items:
    payload = {"model": MODEL, "prompt": item["prompt"], "stream": False}
    try:
        resp = requests.post(OLLAMA_URL, json=payload, timeout=60)
        data = resp.json()
        actual_response = data.get("response", "").strip()
        results.append({
            "id": item["id"],
            "metric": item["metric"],
            "prompt": item["prompt"],
            "llama_response": actual_response
        })
        print(f"Test case {item['id']} done")
    except Exception as e:
        print(f"Error on test case {item['id']}: {e}")
    time.sleep(2)  # small pause to not overload

with open("responses.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("All responses saved to responses.json")