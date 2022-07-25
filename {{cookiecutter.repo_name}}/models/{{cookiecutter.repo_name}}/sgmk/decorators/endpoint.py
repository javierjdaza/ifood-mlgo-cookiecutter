from sgmk.decorators.entrypoint import Entrypoint


class endpoint_function(Entrypoint):
    """Define a new type of entrypoint: endpoint_function"""
    def __init__(self, function=None, **kwargs):
        super().__init__(function, **kwargs)
