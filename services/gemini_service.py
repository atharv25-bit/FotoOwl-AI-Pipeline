from google import genai
from PIL import Image

from config.settings import settings


class GeminiService:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GOOGLE_API_KEY
        )

    def analyze_image(self, image_path):

        image = Image.open(image_path)

        prompt = """
You are an expert event photographer and AI image analyst.

Analyze the given image carefully.

Return ONLY valid JSON.

Example:

{
    "description":"Bride smiling while walking towards the stage.",
    "scene":"Wedding Ceremony",
    "emotion":"Happy",
    "importance":9
}

Rules:

1. Return only JSON.
2. No markdown.
3. No explanation.
4. Importance must be an integer between 1 and 10.
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                prompt,
                image
            ]
        )

        return response.text

    def create_storyboard(self, descriptions):

        prompt = f"""
You are a professional cinematic video editor.

Create the best storyboard for a highlight reel.

Image Analysis:

{descriptions}

Instructions:

1. Arrange the scenes in logical order.
2. Start with an introduction.
3. Build the story naturally.
4. Finish with a memorable ending.
5. Return only the storyboard.
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text