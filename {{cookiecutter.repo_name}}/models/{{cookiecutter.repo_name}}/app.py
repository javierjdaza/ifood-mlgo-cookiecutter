from sgmk.decorators.endpoint import endpoint_function
from sgmk.decorators.model_load import load_function


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
    return None


@endpoint_function
def y(json_dict, model):

    # TODO: write your endpoint logic here

    return {"hello": "world"}

# The function above will return {"hello": "world"}
# whenever you make an HTTP POST request to '/invocations'.
