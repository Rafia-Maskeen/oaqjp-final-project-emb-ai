# IBM Emotion Detection Final Project

A Flask application that sends English text to the Watson NLP EmotionPredict service and displays five emotion scores (anger, disgust, fear, joy, sadness) plus the dominant emotion.

## Project structure

```text
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── tests/
│   ├── test_emotion_detection.py
│   └── test_server.py
├── task_submissions/
├── server.py
├── requirements.txt
└── README.md
```

## Setup (Windows)

Open a terminal in this folder and run:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If you use Conda, activate your environment instead of creating the virtual environment.

## Run the application

```bash
python server.py
```

Open http://127.0.0.1:5000 in your browser. Enter an English sentence and select **Analyze**. Leaving the text blank displays `Invalid text! Please try again!`.

## Use the detector from Python

```python
from EmotionDetection import emotion_detector

print(emotion_detector("I am happy to be learning Python."))
```

## Run unit tests

```bash
python -m unittest discover -s tests -v
```

The tests mock the external Watson service for deterministic local testing. This checks your application logic but does not prove that the live Watson endpoint is reachable.

## Static code analysis

```bash
pylint server.py
pylint EmotionDetection/emotion_detection.py
```

Copy your actual complete terminal output, including the final score, into `task_submissions/8b_static_code_analysis.txt` (or the exact filename requested by your course). Do not copy an example score.

## Watson service connectivity

The emotion detector calls the Skills Network Watson endpoint configured in `EmotionDetection/emotion_detection.py`. The endpoint must be reachable from your network and available for real predictions. If you receive a timeout, try another network (for example, a mobile hotspot), check whether a VPN/proxy is interfering, and retry later. The application returns an unavailable result rather than inventing emotion scores when the service cannot be reached.

## Mapping to the course activities

- **Task 1:** Fork the original course repository, keep the required repository name `oaqjp-final-project-emb-ai`, and update this README in your fork.
- **Task 2:** `EmotionDetection/emotion_detection.py` and `task_submissions/2a_emotion_detection.py`.
- **Task 3:** formatted score dictionary in `EmotionDetection/emotion_detection.py`; use the Python example above to test it.
- **Task 4:** package files `EmotionDetection/__init__.py` and `EmotionDetection/emotion_detection.py`.
- **Task 5:** `tests/test_emotion_detection.py`; run the test command above and save your actual terminal output as `5b_unit_testing_result.txt`.
- **Task 6:** `server.py` and `templates/index.html`; run locally and capture your own deployment screenshot as `6b_deployment_test.png`.
- **Task 7:** blank-input and service-error handling in the detector and Flask route; capture your own blank-input screenshot as `7c_error_handling_interface.png`.
- **Task 8:** `task_submissions/8a_server_modified.py`; run Pylint and save the actual terminal output as `8b_static_code_analysis.txt`.

## Evidence files

Create and add the screenshots and terminal-output files required by your course only after you have actually run the app/tests/analysis. Empty placeholders are not supplied because evidence must be genuine.
