import base64, json
from google import genai
from google.genai import types
from ..config import get_settings

class GeminiService:
    def __init__(self):
        s = get_settings()
        self.model = s.gemini_model
        self.client = genai.Client(api_key=s.gemini_api_key) if s.gemini_api_key else None

    def recommend(self, planner, payload, catalog, image_bytes=None, mime_type=None):
        if not self.client:
            return None
        schema = {
            "planner": planner, "budget": "integer",
            "budget_allocation": {"category": "integer"},
            "summary": "string",
            "recommendations": [{
                "title":"string","category":"string","platform":"string",
                "estimated_price":"integer","reason":"string","url":"string","quantity":"integer"
            }],
            "source_mode":"gemini","notes":["string"]
        }
        prompt = f"""You are PocketSmart AI, a budget-aware recommendation assistant.
Planner: {planner}
User input:
{json.dumps(payload, indent=2)}
Mock catalog:
{json.dumps(catalog, indent=2)}
Rules:
- Never exceed the user's budget when summing estimated_price * quantity.
- Only select entries from the supplied catalog.
- Never invent URLs.
- For a jewelry image, use visible outfit colors/style as an aesthetic signal and do not identify the person.
Return ONLY JSON matching this shape:
{json.dumps(schema, indent=2)}
"""
        contents = [prompt]
        if image_bytes:
            contents.append({"inline_data":{"mime_type": mime_type or "image/jpeg","data": base64.b64encode(image_bytes).decode()}})
        try:
            r = self.client.models.generate_content(
                model=self.model, contents=contents,
                config=types.GenerateContentConfig(
                    temperature=0.35, max_output_tokens=3000, response_mime_type="application/json"
                )
            )
            return json.loads(r.text or "")
        except Exception:
            return None
