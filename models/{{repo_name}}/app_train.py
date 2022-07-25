import json
from json.tool import main
import os
from sgmk.decorators.train import train_function

import logging
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
logging.basicConfig(level=logging.INFO)



@train_function
def x(input_data_path, model_save_path, input_config_file, hyperparams_path=None):
    '''
    The function to execute the training.
    :param input_config_file: path to the inputconfig file
    :param input_data_path: [str], input directory path where all the training file(s) reside in
    :param model_save_path: [str], directory path to save your model(s)
    :param hyperparams_path: [optional[str], default=None], input path to hyperparams json file.
    '''
    # ============================
    # Loading the data
    # ============================
    train_df = pd.read_csv(os.path.join(input_data_path, 'training','input.csv'))
    logging.info(f"-- Data Loading: Done!")
    
 


