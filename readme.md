
# Matrix Factorization-based Collaborative Filtering

This repository contains the implementation of a recommendation system using matrix factorization-based collaborative filtering. The system utilizes the Surprise library to predict user ratings for movies.

## Project Structure

```
RECCOMENDER-SYSTEM-MATRIX-FACTORIZATION-BASED-COLLABORATIVE-FILTERING
│
├── data
│   ├── movie_info.csv
│   └── ratings.csv
│
├── matrixfactor
│   └── ...
│
├── notebook
│   └── matrix_factorization_based_collaborative_filtering.ipynb
│
├── scripts
│   └── recommender_matrix_factor.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Installation

To run this project, you will need to install the required libraries. Make sure you have Python installed on your system, and then install the dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

To run the recommendation system:

1. Navigate to the `scripts` directory.
2. Run the script using Python:

```bash
python recommender_matrix_factor.py
```

## Data Description

The `data` directory contains two CSV files:

- `movie_info.csv`: Contains information about movies.
- `ratings.csv`: Contains user ratings for movies.

The script merges these two datasets to form a comprehensive set of data that includes user IDs, movie titles, and ratings.

## Implementation Details

The system implements the following steps:

1. Reads the datasets.
2. Merges movie information with user ratings.
3. Splits the data into training and test sets.
4. Uses the Surprise library's `SVD` algorithm to train on the dataset.
5. Performs predictions and evaluates the model using RMSE.
6. Utilizes grid search to optimize the SVD algorithm's performance.
7. Predicts ratings for the test set and evaluates the results.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

- [Surprise: A Python scikit for recommender systems.](http://surpriselib.com/)


