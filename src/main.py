# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_partition(s3_key: str, partition: str) -> str:
    parts = s3_key.split('/')
    for part in parts:
        if part.startswith(partition):
            return part.split('=')[1]

    return ''


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    s3key = 'data/cob/merged/dataset_version=20240301/client_system_id=uhg_ia/test.parquet'
    dataset_version = get_partition(s3_key=s3key, partition='client_system_id')
    print(dataset_version)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
