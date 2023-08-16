import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    listing = json.loads(HistoryModel.list_as_json())

    assert listing[0]["text_to_translate"] == "Hello, I like videogame"
    assert listing[0]["translate_from"] == "en"
    assert listing[0]["translate_to"] == "pt"

    assert listing[1]["text_to_translate"] == "Do you love music?"
    assert listing[1]["translate_from"] == "en"
    assert listing[1]["translate_to"] == "pt"
