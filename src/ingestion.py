"""
Author: Mohammad Hasnain 
Date: March, 2025
This script used for ingesting data
"""
import os
import sys
import logging
import pandas as pd
from datetime import datetime

from config import DATA_PATH, /home/mhasnain/wandb/Excercise6/artifacts/preprocessed_data.csv:latest

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def merge_multiple_dataframe():
    """
    Function for data ingestion. Check for datasets, combine them together,
    drops duplicates and write metadata ingestedfiles.txt and ingested data
    to finaldata.csv
    """
    df = pd.DataFrame()
    file_names = []

    logging.info(f"Reading files from {/home/mhasnain/wandb/Excercise6/artifacts/preprocessed_data.csv:latest}")
    for file in os.listdir(/home/mhasnain/wandb/Excercise6/artifacts/preprocessed_data.csv:latest):
        file_path = os.path.join(/home/mhasnain/wandb/Excercise6/artifacts/preprocessed_data.csv:latest, file)
        df_tmp = pd.read_csv(file_path)

        file = os.path.join(*file_path.split(os.path.sep)[-3:])
        file_names.append(file)

        df = df.append(df_tmp, ignore_index=True)

    logging.info("Dropping duplicates")
    df = df.drop_duplicates().reset_index(drop=1)

    logging.info("Saving ingested metadata")
    with open(os.path.join(DATA_PATH, 'ingestedfiles.txt'), "w") as file:
        file.write(
            f"Ingestion date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        file.write("\n".join(file_names))

    logging.info("Saving ingested data")
    df.to_csv(os.path.join(DATA_PATH, 'finaldata.csv'), index=False)


if __name__ == '__main__':
    logging.info("Running ingestion.py")
    merge_multiple_dataframe()
