# Clinical Deterioration AI – Synthea

AI-powered early warning system designed to predict short-term patient clinical deterioration using synthetic electronic health record (EHR) data generated from Synthea.

## Overview

This project combines machine learning and API engineering to support early clinical risk detection. It processes synthetic healthcare data, applies rule-based and model-ready risk prediction logic, and exposes prediction endpoints through a FastAPI backend.

## Key Features

- Modular Python package structure
- FastAPI REST API for prediction endpoints
- Synthetic EHR data workflow using Synthea
- Risk scoring logic for clinical deterioration prediction
- Clean project structure for future ML model integration

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pandas
- Scikit-learn
- Synthetic EHR data
- Docker

## Installation

```bash
git clone https://github.com/AbdulBari33/clinical-deterioration-ai-synthea.git
cd clinical-deterioration-ai-synthea
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .