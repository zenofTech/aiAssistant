# engine.py

from .secret_key import API_KEY
import openai

openai.api_key = API_KEY

def chatengine(request):
    prompt = request.POST.get("prompt")
    response = openai.Completion.create(
        engine="text-davinci-003",
        temperature=0.6,
        prompt=prompt,
        max_tokens=2000,
    )
    res = response.choices[0].text
    chats = {"prompt": prompt, "response": res}
    return chats
