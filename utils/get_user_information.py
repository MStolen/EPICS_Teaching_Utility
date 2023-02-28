import pandas as pd


# Return user data as a Pandas dataframe
def get_user_information(user_file):
    user_data = pd.read_csv(user_file)
    return user_data
