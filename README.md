# FotoOwl AI Multi-Agent Pipeline

## Overview

This project is an AI-powered multi-agent pipeline that automatically converts a collection of event photos into a summarized highlight video.

The system is built using **LangGraph**, where every agent performs a dedicated task in the pipeline.

---

# Pipeline Architecture

```
Input Images
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
Image Analyzer Agent (Google Gemini)
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

# Features

- Multi-Agent Architecture
- LangGraph Workflow
- AI Image Analysis using Gemini
- Intelligent Photo Selection
- Storyboard Generation
- Automatic Music Selection
- Video Composition
- Quality Validation
- Modular Design

---

# Folder Structure

```
FotoOwl-AI-Pipeline/

├── agents/
├── assets/
├── config/
├── graph/
├── input/
├── logs/
├── models/
├── output/
├── prompts/
├── services/
├── utils/

├── main.py
├── README.md
├── requirements.txt
├── .env.example
```

---

# Technologies Used

- Python
- LangGraph
- Google Gemini
- MoviePy
- Pillow
- Pydantic

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_API_KEY
GOOGLE_DRIVE_FOLDER_ID=YOUR_FOLDER_ID

MAX_IMAGES_TO_ANALYZE=2

VIDEO_WIDTH=1280
VIDEO_HEIGHT=720
VIDEO_DURATION=2
VIDEO_FPS=24
MAX_VIDEO_IMAGES=10
```

---

# Run

```bash
python main.py
```

---

# Output

The generated video is saved inside

```
output/final_video.mp4
```

---

# Current Workflow

- Drive Downloader
- Image Loader
- Photo Selector
- Gemini Image Analyzer
- Storyboard Generator
- Music Selector
- Video Composer
- Quality Checker

---

# Future Improvements

- Official Google Drive API
- AI Music Recommendation
- Face Detection
- Duplicate Image Removal
- Cloud Deployment
- Streamlit Dashboard

---

# Author

**Atharv Thigale**

B.Tech – Artificial Intelligence and Data Science
