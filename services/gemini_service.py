from PIL import Image
import google.generativeai as genai

from config.settings import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)


class GeminiService:

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def analyze_image(self, image_path):

        image = Image.open(image_path)

        prompt = """
Analyze this image.

Return:

Description:
Scene:
Emotion:
Importance:
"""

        response = self.model.generate_content(
            [prompt, image]
        )

        return response.text

    def create_storyboard(self, descriptions):

        prompt = f"""

You are a professional wedding video editor.

Arrange these image descriptions into the best cinematic sequence.

Descriptions:

{descriptions}

Return only numbered storyboard.

"""

        response = self.model.generate_content(prompt)

        return response.text