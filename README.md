# 📚 Luigi Translation Pipeline

This is a simple Luigi pipeline that automates a multi-step translation process. It fetches data, processes it, translates words using an external API, and interacts with the user at the end (e.g., through a quiz or output file).

## 📌 Task Overview

The pipeline includes the following Luigi tasks:

- **GetData** – loads the original word data
- **ProcessData** – processes and formats the data
- **GetTranslation** – translates words using a translation API
- **QuizUser** – handles the final output or user interaction

## 🛠️ Requirements

- Python 3.x
- Luigi
- Requests library

Install dependencies with:

pip install luigi requests

## 🚀 Running the App

To run the pipeline, use:

### py -3 main.py