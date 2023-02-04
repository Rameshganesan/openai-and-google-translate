import os
import openai
from flask import Flask, redirect, render_template, request, url_for
from google.cloud import translate

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
google_project_id = os.getenv("GOOGLE_PROJECT_ID")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        language = request.form["language"]
        question = request.form["question"]
        # Add Google API for transfer from source language to english
        question_trans = translate_me(question, "en")

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question_trans,
            temperature=0.7,
            max_tokens=90
        )
        print(response)
        return redirect(url_for("index", result='<center>' + translate_me(response.choices[0].text,language) + '<br>' + response.choices[0].text + '</center>'))

    result = request.args.get("result")
    print(result)
    return render_template("index.html", result=result)

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






