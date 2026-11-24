"""Unit tests for the emotion detector."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verify successful, blank-input, and service-error behavior."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_returns_emotion_scores(self, mock_post):
        response = Mock()
        response.json.return_value = {
            "emotionPredictions": [{"emotion": {
                "anger": 0.01, "disgust": 0.02, "fear": 0.03,
                "joy": 0.90, "sadness": 0.04
            }}]
        }
        mock_post.return_value = response
        result = emotion_detector("I am happy")
        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.90)

    def test_blank_input_returns_empty_result(self):
        result = emotion_detector("   ")
        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["anger"])

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_network_error_returns_empty_result(self, mock_post):
        import requests

        mock_post.side_effect = requests.Timeout("service timed out")
        result = emotion_detector("I am worried")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
