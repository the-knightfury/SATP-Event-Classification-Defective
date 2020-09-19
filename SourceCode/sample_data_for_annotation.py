import pandas as pd
import path
import sklearn

if __name__ == "__main__":
    source_root = path.TAGTOG_PRE_ANNOTATION
    source_file = "master_2011to2015_probable_relevant_data.csv"
    source_path = source_root + source_file
    destination = path.TAGTOG_PRE_ANNOTATION + "TagTog_Data/"
    total_data = 9000
    file_index = [i for i in range(10, 22)]
    file_prefix = 'news_satp_'

    master_data = pd.read_csv(source_path, header=[0])

    relevant = master_data[master_data["Relevance"] == True]
    not_relevant = master_data[master_data["Relevance"] == False]

    print(master_data['location'].value_counts())

    n = master_data.shape[0]
    sample_df = master_data.groupby('Relevance').apply(lambda x: x.sample(21500))

    print(sample_df['Relevance'].value_counts())
    print(sample_df['location'].value_counts())

    n = sample_df.shape[0]
    sample_df = sample_df.groupby('year').apply(lambda x: x.sample(4000))

    print(sample_df['Relevance'].value_counts())
    print(sample_df['location'].value_counts())

    n = sample_df.shape[0]
    sample_df = sample_df.groupby('location').apply(lambda x: x.sample(frac = 0.5))

    print(sample_df['Relevance'].value_counts())
    print(sample_df['location'].value_counts())

    print(len(sample_df))

    sample_df = sklearn.utils.shuffle(sample_df)
    sample_df.reset_index(drop=True, inplace=True)
    print(sample_df.head(5))
    print(sample_df['Relevance'].value_counts())






