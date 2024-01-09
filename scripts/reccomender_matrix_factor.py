import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split

## 1. Reading Dataset 
#Reading ratings file:
ratings = pd.read_csv('/Users/paramanandbhat/Downloads/MatrixfactorizationBasedCollaborativeFilteringusingSurprise-201024-234535 (1)/ratings.csv')

#Reading Movie Info File
movie_info = pd.read_csv('/Users/paramanandbhat/Downloads/MatrixfactorizationBasedCollaborativeFilteringusingSurprise-201024-234535 (1)/movie_info.csv')

## 2.  Merging Movie information to ratings dataframe   

ratings = ratings.merge(movie_info[['movie id','movie title']], how='left', left_on = 'movie_id', right_on = 'movie id')

print(ratings.head())