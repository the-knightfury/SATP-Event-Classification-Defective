import pandas as pd
import path
import SourceCode.utils as u


if __name__ == "__main__":

    source_data_path = path.MASTER
    event_path = path.TAGTOG_POST_ANNOTATION
    destination_data_path = path.TAGTOG_POST_ANNOTATION

    action_file = path.ACTION
    source_file = path.FROM_2011To2015

    path_name = source_data_path + source_file
    action_path = event_path + action_file
    

    master_data = pd.read_csv(path_name, header=[0])
    master_data = u.remove_special_characters(master_data, 'news')

    actions = pd.read_csv(action_path, header=[0])


    # Step - 1 : Pull Out All the Probable relevant story



    # Step - 2 : Get a proportionate data for each country and each year - 750 * 3 - Total data



    # Step - 3 : Divide the data into 3 parts


    print(master_data.head(10))

    # df = pd.read_csv("news_sample_data_16000.tsv", sep='\t')
    # prefix = 'news_satp_'
    # chunk_size = int(df.shape[0] / 32)
    # i = 4
    # for start in range(0, df.shape[0], chunk_size):
    #     df_subset = df.iloc[start:start + chunk_size]
    #     df_subset.to_csv('splitted_data/' + prefix + str(i) + '.tsv', index=False, header=True, sep='\t')
    #     i += 1
    #     print(df_subset.shape)