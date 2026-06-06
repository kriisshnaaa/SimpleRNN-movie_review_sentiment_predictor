# 🎬 IMDB Movie Review Sentiment Analysis using RNN

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![NLP](https://img.shields.io/badge/NLP-Sentiment%20Analysis-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📌 Project Overview

This project is a Deep Learning based Sentiment Analysis application that classifies IMDB movie reviews as **Positive** or **Negative**.

The model is built using:

* TensorFlow & Keras
* Embedding Layer
* Simple RNN
* IMDB Movie Reviews Dataset
* Streamlit Web Application

The application allows users to enter a movie review and instantly predict its sentiment.

---

## 🚀 Features

✅ IMDB Movie Review Classification

✅ Text Preprocessing Pipeline

✅ Word Embeddings

✅ Recurrent Neural Network (RNN)

✅ Real-time Sentiment Prediction

✅ Interactive Streamlit Interface

✅ Confidence Score Display

---

## 🧠 Model Architecture

Input Review

⬇

Text Preprocessing

⬇

Embedding Layer

⬇

Simple RNN

⬇

Dense Layer

⬇

Sigmoid Activation

⬇

Positive / Negative Prediction

---

## 📂 Dataset

Dataset Used:

**IMDB Movie Reviews Dataset**

* 50,000 Movie Reviews
* Binary Sentiment Classification
* Positive Reviews
* Negative Reviews

Dataset is loaded directly using TensorFlow/Keras.

```python
from tensorflow.keras.datasets import imdb
```

## ⚙️ Technologies Used

| Technology | Purpose                 |
| ---------- | ----------------------- |
| Python     | Programming Language    |
| TensorFlow | Deep Learning Framework |
| Keras      | Neural Network API      |
| NumPy      | Numerical Computation   |
| Streamlit  | Web Application         |
| NLP        | Text Processing         |

## 🏗️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/imdb-sentiment-analysis-rnn.git
cd imdb-sentiment-analysis-rnn
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run Application

```bash
streamlit run main.py
```

The application will open in your browser automatically.

## 💡 Example Reviews

### Positive Review

```text
This movie was absolutely fantastic. The acting was brilliant and the story was engaging.
```

### Negative Review

```text
This movie was terrible. The acting was poor and the story was boring.
```

## 📊 Model Performance

Metrics used:

* Accuracy
* Validation Accuracy
* Binary Crossentropy Loss

Example Results:

```text
Training Accuracy : ~95%
Validation Accuracy : ~82%
```

*(Results may vary depending on training configuration.)*

## 📁 Project Structure

```text
├── main.py
├── sentiment_model.h5
├── requirements.txt
├── README.md
└── notebooks/
```

## 🎯 Learning Outcomes

Through this project I learned:

* Natural Language Processing Fundamentals
* Text Encoding
* Tokenization
* Padding Sequences
* Word Embeddings
* Recurrent Neural Networks
* Model Deployment using Streamlit
* Deep Learning Workflow

## 🔮 Future Improvements

* LSTM Architecture
* GRU Architecture
* Transformer Models
* Better Text Cleaning
* Improved UI/UX
* Sentiment Confidence Visualization
* Docker Deployment

## 👨‍💻 Author

Krishna

Deep Learning | NLP | Machine Learning | Full Stack AI Projects

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
