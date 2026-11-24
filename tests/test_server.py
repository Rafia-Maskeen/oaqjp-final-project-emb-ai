"""Route tests for the Flask application."""

import unittest
from unittest.mock import patch

from server import app


class TestServer(unittest.TestCase):
    """Test the home page and blank-input validation."""

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Emotion Detection", response.data)

    def test_blank_input_message(self):
        response = self.client.get("/emotionDetector?textToAnalyze=%20%20")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_data(as_text=True), "Invalid text! Please try again!")

    @patch("server.emotion_detector")
    def test_detector_service_failure(self, mock_detector):
        mock_detector.return_value = {
            "anger": None, "disgust": None, "fear": None,
            "joy": None, "sadness": None, "dominant_emotion": None
        }
        response = self.client.get("/emotionDetector?textToAnalyze=hello")
        self.assertEqual(response.status_code, 502)


if __name__ == "__main__":
    unittest.main()
