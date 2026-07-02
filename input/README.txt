# FotoOwl AI Multi-Agent Pipeline

## Overview

This project is an AI-powered multi-agent pipeline that converts a collection of event photos into a summarized video reel.

The system follows a modular LangGraph architecture where each agent performs a single responsibility.

---

## Pipeline

```
Google Drive / Input Folder
            │
            ▼
Drive Downloader Agent
            │
            ▼
Image Loader Agent
            │
            ▼
Photo Selector Agent
            │
            ▼
Image Analyzer Agent (Gemini Vision)
            │
            ▼
Storyboard Agent
            │
            ▼
Music Selector Agent
            │
            ▼
Video Composer Agent
            │
            ▼
Quality Checker Agent
            │
            ▼
Output Video
```

---

## Features

- Multi-Agent Architecture
- LangGraph Workflow
- Gemini Vision Image Analysis
- Intelligent Photo Selection
- Storyboard Generation
- Automatic Music Selection
- Video Generation
- Quality Validation
- Modular Design

---

## Folder Structure

```
FotoOwl-AI-Pipeline

agents/
config/
graph/
input/
output/
logs/
models/
services/
utils/
assets/

main.py
README.md
requirements.txt
```

---

## Technologies

- Python
- LangGraph
- Google Gemini
- OpenCV
- MoviePy
- Pillow
- Pydantic

---

## Setup

Create virtual environment

```
python -m venv venv
```

Activate

Windows

```
venv\Scripts\activate
```

Install packages

```
pip install -r requirements.txt
```

---

## Environment Variables

Create `.env`

```
GOOGLE_API_KEY=YOUR_API_KEY

GOOGLE_DRIVE_FOLDER_ID=YOUR_FOLDER_ID

MAX_IMAGES_TO_ANALYZE=2
```

---

## Run

```
python main.py
```

---

## Output

```
output/

final_video.mp4
```

---

## Future Improvements

- Official Google Drive API
- Better Storyboard Generation
- Automatic Music Recommendation
- Face Recognition
- Duplicate Removal
- Video Effects
- Cloud Deployment

---

## Author

Atharv Thigale
B.Tech Artificial Intelligence and Data Science