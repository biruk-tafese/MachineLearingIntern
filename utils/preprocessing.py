# utils/preprocessing.py
from sklearn.model_selection import train_test_split

def split_data(data, test_size=0.2, random_state=42):
    """
    Split the data into training and testing sets.

    Parameters:
    - data: DataFrame, the input data to be split
    - test_size: float, the proportion of the dataset to include in the test split (default is 0.2)
    - random_state: int or RandomState instance, controls the randomness of the training and testing indices

    Returns:
    - train_data: DataFrame, the training set
    - test_data: DataFrame, the testing set
    """
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)
    return train_data, test_data

