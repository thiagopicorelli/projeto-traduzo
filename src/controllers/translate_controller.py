from flask import Blueprint, request, render_template
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    text_to_translate = ""
    translate_from = "pt"
    translate_to = "en"
    translated = "Tradução"

    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")
        if len(text_to_translate.strip()) != 0:
            translated = GoogleTranslator(
                source=translate_from,
                target=translate_to
            ).translate(text_to_translate)
    return render_template(
        "index.html",
        language=LanguageModel.list_dicts(),
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    raise NotImplementedError
