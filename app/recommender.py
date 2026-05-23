import joblib
import numpy as np

# load saved files
nn = joblib.load('app/models/knn_model.pkl')

df = joblib.load('app/models/movies_df.pkl')

embeddings = np.load('app/models/embeddings.npy')

movie_indices = joblib.load('app/models/movie_indices.pkl')


# recommendation function

def recommend(movie_name, top_n=10):

    movie_name = movie_name.lower()

    if movie_name not in movie_indices:
        return []

    idx = movie_indices[movie_name]

    distances, indices = nn.kneighbors(
        [embeddings[idx]],
        n_neighbors=top_n + 1
    )

    movie_indices_list = indices.flatten()[1:]

    recommendations = []

    for i in movie_indices_list:

        movie = {
            'title': df.iloc[i]['title_x'],
            'overview': df.iloc[i]['overview'],
            'poster': df.iloc[i].get('poster_path', '')
        }

        recommendations.append(movie)

    return recommendations