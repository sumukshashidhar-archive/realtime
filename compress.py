import pandas as pd
import os
import logging


logging.debug("Running Compression")

for filename in os.listdir('./prices/'):
    if filename.endswith('.csv'):
        try:
            fil = os.path.join('./prices/', filename)
            df = pd.read_csv(fil, header=None)
            df = df.drop_duplicates(subset=[1, 2, 3, 4, 5, 6, 7], keep='last')
            df.to_csv(fil, header=False, index=False)
        except Exception as e:
            logging.error(f"Failed to compress file {filename}. {e}")



for filename in os.listdir('./depth/'):
    if filename.endswith('.csv'):
        try:
            fil = os.path.join('./depth/', filename)
            df = pd.read_csv(fil, header=None)
            df = df.drop_duplicates(subset=[1, 2, 3, 4], keep='last')
            df.to_csv(fil, header=False, index=False)
        except Exception as e:
            logging.error(f"Failed to compress file {filename}. {e}")
