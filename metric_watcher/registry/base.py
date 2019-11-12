class Registry:
    
    def __init__(self):
        self.metrics = {}  # keep metric managers per metric 
        self.reporters = {}  # keeps reporters and linked metrics
        