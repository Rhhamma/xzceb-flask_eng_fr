from flask import Flask, render_template, request, session
from machinetranslation import translator

app = Flask("Web Translator")
app.secret_key = "your_secret_key"  # Add a secret key for session usage

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    # Translate the text
    translated_text = translator.english_to_french(textToTranslate)
    session['translated_text'] = f"Translated text to French: {translated_text}"
    return translated_text

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    # Translate the text
    translated_text = translator.french_to_english(textToTranslate)
    session['translated_text'] = f"Translated text to English: {translated_text}"
    return translated_text

@app.route("/")
def renderIndexPage():
    translated_text = session.pop('translated_text', None)
    return render_template('index.html', translated_text=translated_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
