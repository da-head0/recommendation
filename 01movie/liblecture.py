from IPython.display import display, HTML
import pandas as pd
import numpy as np
import math

np.set_printoptions(precision=2)
pd.set_option('display.precision', 2)

def displayMovies(movies, movieIds, ratings=[]):

    html = ""

    for i, movieId in enumerate(movieIds):
        movie = movies[movies['movieId'] == movieId].iloc[0]

        html += f"""
            <div style="display:inline-block;min-width:150px;max-width:150px; vertical-align:top">
                <img src='{movie.imgurl}' width=120> <br/>
                <span>{movie.title}</span> <br/>
                {f"<span>{ratings[i]}</span> <br/>" if len(ratings) > 0 else ""}
                <ul>{"".join([f"<li>{genre}</li>" for genre in movie.genres.split('|')])}</ul>
            </div>
        """

    display(HTML(html))


def getMAE(real, pred):
    errors = real - pred
    return errors.abs().mean()

def getRMSE(real, pred):
    errors = real - pred
    return math.sqrt(errors.pow(2).mean())