from machinetranslation import translator
from flask import Flask, render_template, request, jsonify
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    # Translate the text
    translated_text = english_to_french(textToTranslate)
    session['translated_text'] = f"Translated text to French: {translated_text}"
    return "Translation successful!"

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    # Translate the text
    translated_text = french_to_english(textToTranslate)
    session['translated_text'] = f"Translated text to English: {translated_text}"
    return "Translation successful!"
@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

