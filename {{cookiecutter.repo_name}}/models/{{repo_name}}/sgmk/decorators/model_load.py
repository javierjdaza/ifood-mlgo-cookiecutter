from sgmk.decorators.entrypoint import Entrypoint


class load_function(Entrypoint):
    """Define a new type of entrypoint: load_function"""
    def __init__(self, function=None, **kwargs):
        super().__init__(function, **kwargs)
