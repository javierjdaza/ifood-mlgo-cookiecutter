from sgmk.decorators.entrypoint import Entrypoint


class train_function(Entrypoint):
    """Define a new type of entrypoint: train_function"""
    def __init__(self, function=None, **kwargs):
        super().__init__(function, **kwargs)
