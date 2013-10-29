#!/opt/local/bin/python3.3

class basenoise(object):
    def __init__(self):
        raise NotImplementedError("You need to make one of me.")

    def generate_noise(self):
        raise NotImplementedError("implement me to generate noise over a range of values")
