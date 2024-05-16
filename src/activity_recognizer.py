# this program recognizes activities

import numpy as np
import pandas as pd
from sklearn.preprocessing import scale, MinMaxScaler
from sklearn import svm, preprocessing, metrics
from sklearn.model_selection import train_test_split
from DIPPID import SensorUDP

""" Source I worked with:
    https://www.datacamp.com/tutorial/svm-classification-scikit-learn-python 
"""

DATA_FOLDER = 'resampled_data'
PERSON = 'johannes'

TEST_SIZE = 0.1  # 80/20 split
RANDOM_STATE = 120

# rbf accuracy = 0.9608 but it always predicts jumpingjacks in real life and therefore is not usable
KERNEL = 'linear' # linear, rbf (non-linear), ...

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)


def main():
    # Load Data
    data = load_datasets()

    # Preprocess Data
    normalized_data, numerical_activities = preprocess_data(data)

    # Split Data
    X_train, X_test, y_train, y_test = train_test_split(normalized_data,
                                                        numerical_activities,
                                                        test_size=TEST_SIZE,
                                                        random_state=RANDOM_STATE
                                                        )

    # get classifier SVC
    classifier = get_classifier(X_train, X_test, y_train, y_test)

    return classifier


# load all data in one datafrane
def load_datasets():
    activities = ['jumpingjacks', 'lifting', 'rowing', 'running']

    df = pd.DataFrame()
    for index in range(1, 6):
        for activity in activities:
            data = pd.read_csv(f'{DATA_FOLDER}/{PERSON}-{activity}-{index}.csv')

            # add activity name to dataFrame
            data['activity'] = activity
            concat_params = [df, data]
            df = pd.concat(concat_params)

    # delte rows with NaNs
    df = df.dropna()

    return df


def preprocess_data(data: pd.DataFrame):
    data = pd.DataFrame(data.drop(['id'], axis=1))

    # transform activities into numerical values [0-3] see activities in load_datasets
    encoder = preprocessing.LabelEncoder()
    encoder.fit(data['activity'])
    numerical_activities = encoder.transform(data['activity'])

    sensor_data = pd.DataFrame(data.drop(['timestamp', 'activity'], axis=1))

    # inspired by machine_learning_tour: center values around mean and normalize them
    # center
    scaled_data = scale(sensor_data)
    data_mean = sensor_data.copy()
    data_mean = scaled_data

    # normalize (mapping all values to a certain range)
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data_mean)
    normalized_data = data_mean.copy()
    normalized_data = scaled_data

    return normalized_data, numerical_activities


# get accuracy score and classifier for continous prediction
def get_classifier(X_train, X_test, y_train, y_test):
    classifier = svm.SVC(kernel=KERNEL)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    # print copied from https://www.datacamp.com/tutorial/svm-classification-scikit-learn-python - Evaluating the model (whith slight changes from me)
    print('\n----------------')
    print(f'Model Accuracy: {round(metrics.accuracy_score(y_test, y_pred), 4)}')
    print('----------------\n')

    return classifier


def real_time_prediction(classifier):
    if sensor.has_capability('accelerometer'):
        acc_x = float(sensor.get_value('accelerometer')['x'])
        acc_y = float(sensor.get_value('accelerometer')['y'])
        acc_z = float(sensor.get_value('accelerometer')['z'])

    if sensor.has_capability('gyroscope'):
        gyro_x = float(sensor.get_value('gyroscope')['x'])
        gyro_y = float(sensor.get_value('gyroscope')['y'])
        gyro_z = float(sensor.get_value('gyroscope')['z'])

    try:
        prediction = classifier.predict([[acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z]])
        return prediction
    except:
        print('Something went wrong! Check if your input device is running and activliy sending data!')


if __name__ == '__main__':
    main()
