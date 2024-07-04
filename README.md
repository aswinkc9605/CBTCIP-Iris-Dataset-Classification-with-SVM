
# Iris Dataset Classification with SVM

This project demonstrates the preprocessing and modeling of the famous Iris dataset using a Support Vector Machine (SVM) classifier in Python. The Iris dataset is a classic dataset in the field of machine learning and contains measurements of iris flowers across three species.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Preprocessing Steps](#preprocessing-steps)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project covers the following steps:
1. Handling missing values.
2. Removing unnecessary columns.
3. Encoding categorical variables.
4. Splitting the dataset into training and testing sets.
5. Training an SVM classifier.
6. Evaluating the model's performance.

## Dataset

The Iris dataset consists of 150 samples of iris flowers, with four features:
- Sepal length in cm
- Sepal width in cm
- Petal length in cm
- Petal width in cm

The target variable is the species of the iris flower, which has three possible values:
- Setosa
- Versicolor
- Virginica

## Installation

To run this project, you need Python and the following libraries installed:

- pandas
- scikit-learn

You can install these dependencies using pip:

```bash
pip install pandas scikit-learn
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/aswinkc9605/Iris-Dataset-Classification-with-SVM.git
   ```
2. Navigate to the project directory:
   ```bash
   cd IRIS FLOWER CLASSIFICATION
   ```
3. Run the Python script:
   ```bash
   python sample.py
   ```

## Preprocessing Steps

1. **Handling Missing Values**: Checked for any missing values in the dataset.
2. **Removing 'Id' Column**: Removed the 'Id' column as it is not necessary for the analysis.
3. **Encoding 'Species' Column**: Encoded the 'Species' column into numerical values using `LabelEncoder`.

## Modeling

1. **Splitting the Dataset**: Split the dataset into training (80%) and testing (20%) sets.
2. **Training the SVM Classifier**: Initialized and trained an SVM classifier with a linear kernel.

## Evaluation

1. **Making Predictions**: Used the trained SVM classifier to predict the labels for the test set.
2. **Calculating Accuracy**: Computed the accuracy of the model.
3. **Classification Report**: Generated a detailed classification report including precision, recall, and F1-score.

## Results

The model achieved an accuracy of approximately 0.97 on the test set. The detailed classification report can be found in the output of the script.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

