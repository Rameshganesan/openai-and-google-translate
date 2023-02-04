import os
import openai
from google.cloud import translate

openai.api_key = "<<your Openai api_key>>"
google_project_id = "<<your google project_id>>"
# set google cloud service account json file with path as environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/medium/service_account.json" 

def translate_me(source_text, lang):
    parent = f"projects/{google_project_id}"
    client = translate.TranslationServiceClient()

    response = client.translate_text(
        contents=[source_text],
        target_language_code=lang,
        parent=parent
    )

    for translation in response.translations:
        trans_text = translation.translated_text
    return trans_text


def anwser_me(source_language, question):
    # Add Google API for transfer from source language to english
    question_trans = translate_me(question, "en")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question_trans,
        temperature=0.9,
        max_tokens=90
    )
    return translate_me(response.choices[0].text, source_language)

print(anwser_me('ta', 'ஜோ பிடனுக்கும் தாஜ்மஹாலுக்கும் என்ன தொடர்பு?'))
