# Fake News Detection (Django + Machine Learning)

A Django web app that classifies a pasted news article as **Fake** or **True** using TF-IDF features and Logistic Regression (scikit-learn). Model experiments are in `main2.ipynb`.

## Requirements
- Python 3.7
- Packages in `requirements.txt`

## Setup
```bash
git clone https://github.com/KanavvNegi/Fake-news-detection.git
cd Fake-news-detection
python -m venv venv
venv\Scripts\activate        # Windows  (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
```

## Dataset (not included - too large for GitHub)
Download the "Fake and Real News" dataset (`Fake.csv`, `True.csv`) from Kaggle:
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

Run `main2.ipynb` to regenerate `manual_testing2.csv`, then place it at
`website/templates/pkl/manual_testing2.csv` (the app reads it from there).

## Run
```bash
cd website
python manage.py runserver
```
Open http://127.0.0.1:8000/ and paste a news article into the input field.

## Project structure
- `main2.ipynb` - data cleaning, training, evaluation
- `website/` - Django project (`mainapp/` holds views and the saved model)
- `website/Capture*.PNG` - screenshots of the app
