from openai import OpenAI

from core.config import settings


class aiService():
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def openai_response(self, prompt):
        response_obj = self.client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can choose other engines as well
            # messages=[{"role": "system", "content":prompt}],
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": "Generate content based on the given details."}
            ]
        )
        response = response_obj.choices[0].message.content
        return response
