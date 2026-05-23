# 🎬 Semantic Movie Recommendation System

A Netflix-style AI-powered movie recommendation system built using NLP, transformer-based semantic embeddings, KNN similarity search, and FastAPI.

The system recommends contextually similar movies by understanding semantic meaning from genres, keywords, overviews, cast, and metadata instead of relying only on exact keyword matching.

---

# 🚀 Features

- Semantic movie recommendations
- NLP-based preprocessing pipeline
- Transformer-based embeddings
- K-Nearest Neighbors similarity search
- Netflix-style frontend UI
- FastAPI backend
- Movie poster integration
- Scalable recommendation pipeline
- Content-based recommendation engine

---

# 🧠 How It Works

## 1. Data Preprocessing

Movie metadata is cleaned and processed using NLP preprocessing techniques:
- lowercasing
- removing symbols/brackets
- text normalization
- feature combination

Features used:
- genres
- keywords
- overview
- tagline
- director
- top cast

---

## 2. Semantic Embeddings

Movie descriptions are converted into dense vector embeddings using Sentence Transformers.

Model used:

```python
all-MiniLM-L6-v2
```

This allows the system to understand:
- themes
- movie context
- semantic similarity
- narrative relationships

instead of relying only on exact word overlap.

---

## 3. Recommendation Engine

A KNN similarity model retrieves the most semantically similar movies based on embedding distance.

Algorithms experimented with:
- TF-IDF + Cosine Similarity
- Euclidean Distance
- KNN
- Transformer-based Semantic Embeddings

---

# 🛠️ Tech Stack

## Backend
- Python
- FastAPI
- Scikit-learn
- NumPy
- Pandas
- Joblib

## NLP / Machine Learning
- Sentence Transformers
- KNN Similarity Search
- TF-IDF
- Cosine Similarity
- Semantic Embeddings

## Frontend
- HTML
- CSS
- JavaScript

---

# 📂 Project Structure

```text
movie-recommender/
│
├── app/
│   ├── main.py
│   ├── recommender.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   ├── static/
│   │   ├── style.css
│   │   └── script.js
│   │
│   └── models/
│       ├── knn_model.pkl
│       ├── embeddings.npy
│       ├── movies_df.pkl
│       └── movie_indices.pkl
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/movie-recommender.git
```

```bash
cd movie-recommender
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run The Application

```bash
uvicorn app.main:app --reload
```

Open in browser:

```text
http://127.0.0.1:8000
```

---

# 📸 UI Features

Netflix-inspired UI with:
- movie cards
- recommendation rows
- posters
- hover animations
- responsive design

---

# 📊 Example Recommendations

Input:

```text
Air Force One
```

Recommendations:
- Executive Decision
- White House Down
- Con Air
- Olympus Has Fallen
- Eraser

---

# 🧪 Models & Experiments

The following approaches were tested:

| Model | Result |
|---|---|
| TF-IDF + Cosine Similarity | Basic keyword matching |
| Euclidean Distance | Weak semantic quality |
| KNN + TF-IDF | Better retrieval |
| Sentence Transformers + KNN | Best performance |

---

# 💡 Future Improvements

- FAISS vector search
- Hybrid recommendation system
- TMDB API integration
- Trailer support
- Watchlist functionality
- User authentication
- Collaborative filtering
- React frontend
- Docker deployment

---

# 📚 Medium Article

Read the full project breakdown here:

[Build your own End-to-End Semantic Movie Recommendation System using Sentence Transformers and KNN](https://medium.com/@rahul.arora0603/build-your-own-end-to-end-semantic-movie-recommendation-system-using-sentence-transformers-and-knn-5094e9730b61)

---

# 👨‍💻 Author

Rahul Arora

- [LinkedIn](https://www.linkedin.com/in/rahul-arora-datascience/)
- [Portfolio](https://dsportfolio-lovat.vercel.app/)

---

# ⭐ Support

If you liked this project, consider giving it a star ⭐