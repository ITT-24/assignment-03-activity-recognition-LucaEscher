import pandas as pd

DATA_FODLER = 'data'
SAVE_FOLDER = 'downsampled_data'

name = 'luca'
activity = 'running'
number = 1


def downsample_file(name: str, activity: list, number: int) -> None:
    file_name = f'{name}-{activity}-{number}'

    df = pd.read_csv(f'{DATA_FODLER}/{file_name}.csv')

    # delete row if they are the same directly in a row -> ignore timestamps
    df_resampled = df.loc[(df.drop(columns=['timestamp']).shift() != df.drop(columns=['timestamp'])).any(axis=1)]
    df_resampled.to_csv(f'./{SAVE_FOLDER}/{file_name}.csv', index_label='id', index=True)


def downsample_all(activities: list, name: str) -> None:
    for activity in activities:
        for index in range(1, 6):
            downsample_file(name, activity, index)


if __name__ == '__main__':
    activities = ['jumpingjacks', 'lifting', 'rowing', 'running']
    downsample_all(activities, name)
