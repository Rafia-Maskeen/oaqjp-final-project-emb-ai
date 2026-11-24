"""Call the Watson NLP service to detect emotions in English text."""

from typing import Any

import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}
TIMEOUT_SECONDS = 30


def _empty_result() -> dict[str, Any]:
    """Return a consistent empty result when input or service response is invalid."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def emotion_detector(text_to_analyze: str) -> dict[str, Any]:
    """Return five emotion scores and the name of the strongest emotion.

    Returns a dictionary with None values for blank input, an unsuccessful HTTP
    response, malformed service data, or a network error.
    """
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return _empty_result()

    payload = {"raw_document": {"text": text_to_analyze.strip()}}

    try:
        response = requests.post(
            URL, headers=HEADERS, json=payload, timeout=TIMEOUT_SECONDS
        )
        response.raise_for_status()
        result = response.json()
        emotions = result["emotionPredictions"][0]["emotion"]
        required = ("anger", "disgust", "fear", "joy", "sadness")
        scores = {name: emotions[name] for name in required}
        dominant = max(scores, key=scores.get)
    except (requests.RequestException, ValueError, KeyError, IndexError, TypeError):
        return _empty_result()

    scores["dominant_emotion"] = dominant
    return scores
