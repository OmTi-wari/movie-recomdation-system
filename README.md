# 🎬 Movie Recommendation System

A content-based movie recommendation system built with Machine Learning that suggests similar movies based on genres, keywords, cast, crew, and plot overview.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Technologies](#technologies)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)


---

## 🎯 Overview

This system uses **Content-Based Filtering** to recommend 5 similar movies based on:
- Genres (Action, Drama, Comedy, etc.)
- Keywords and tags
- Top 3 cast members
- Director
- Plot overview

**Algorithm**: Bag of Words + Cosine Similarity on vectorized text data

---

## 🛠️ Technologies

- **Python**
- **NumPy** - Array operations
- **Pandas** - Data manipulation
- **NLTK** - Text preprocessing (Porter Stemmer)
- **Scikit-learn** - CountVectorizer, Cosine Similarity
- **Streamlit** - Web interface
- **Pickle** - Model serialization

---

## 📊 Dataset

**TMDB 5000 Movie Dataset** from Kaggle
- `tmdb_5000_movies.csv` - 4,803 movies
- `tmdb_5000_credits.csv` - Cast and crew data

---

## 🏗️ Project Architecture

```
movie-recommendation-system/
│
├── model/
│   ├── archive/
│   │   ├── tmdb_5000_movies.csv       # Original movie data
│   │   └── tmdb_5000_credits.csv      # Original credits data
│   ├── system.ipynb                   # Main notebook with ML pipeline
│   ├── movie_dict.pkl                 # Serialized movie dataframe
│   └── similarity.pkl                 # Precomputed similarity matrix
│
├── frontend/
│   ├── app.py                         # Streamlit web application
│   ├── movie_dict.pkl                 # Copy of movie data for app
│   └── similarity.pkl                 # Copy of similarity matrix
│
└── README.md                          # Project documentation
```


## ⚙️ How It Works

### Pipeline:
1. **Load & Merge** datasets
2. **Extract Features** from JSON columns (genres, cast, crew, keywords)
3. **Combine** all features into "tags" column
4. **Preprocess**: Lowercase, remove spaces, apply Porter Stemming
5. **Vectorize** with CountVectorizer (5000 features, remove stop words)
6. **Calculate** Cosine Similarity matrix
7. **Recommend**: Sort by similarity, return top 5

### Key Code:
```python
# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_def['tags']).toarray()

# Similarity
similarity = cosine_similarity(vectors)

# Recommend
def recommend(movie):
    movies_index = new_def[new_def['title'] == movie].index[0]
    distances = similarity[movies_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [new_def.iloc[i[0]].title for i in movies_list]
```


## 📥 Installation

### Prerequisites
- Python 3.7+
- pip

### Steps
```bash
# Clone repository
git clone https://github.com/OmTi-wari/movie-recomdation-system.git
cd movie-recomdation-system

# Install dependencies
pip install numpy pandas scikit-learn nltk streamlit

# Download NLTK data
python -c "import nltk; nltk.download('punkt')"

# Run notebook to generate models
jupyter notebook model/system.ipynb

# Copy models to frontend
copy model\*.pkl frontend\

# Run app
cd frontend
streamlit run app.py
```


## 💻 Usage

1. Launch app: `streamlit run app.py`
2. Select a movie from dropdown
3. Click "Recommend"
4. View 5 similar movies

---

## 👨‍💻 Author

**Om Tiwari**  
GitHub: [@OmTi-wari](https://github.com/OmTi-wari)

---

## 📚 Documentation

- [Scikit-learn](https://scikit-learn.org/stable/)
- [Streamlit](https://docs.streamlit.io/)
- [NLTK](https://www.nltk.org/)
- [TMDB Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

**⭐ Star this repo if you found it helpful!**













