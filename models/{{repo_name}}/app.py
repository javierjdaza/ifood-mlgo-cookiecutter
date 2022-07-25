from urllib import response
from sgmk.decorators.endpoint import endpoint_function
from sgmk.decorators.model_load import load_function

import os
import joblib
import pandas as pd

import logging

import functools

logging.basicConfig(level=logging.INFO)



@load_function
def load_model(model_save_path):
    '''
    TODO: Write your loading model logic here.
    On your endpoint_function, the result will
    be ready as a parameter. Thus, return the
    necessary object here.
    For example, it can be a single model, or
    a custom dictionary containing a list of
    models and their identification.
    '''
    model_file = os.path.join(model_save_path, 'model.joblib')
    loaded_model = joblib.load(model_file)
    logging.info(f"-- Model Loading: Done!")
    return loaded_model



@endpoint_function
def y(json_dict, model):
  pass



