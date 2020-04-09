class Reader:
    @staticmethod
    def read(filename):
        f = open(filename, "r")
        return f.read().strip('\n')

    @staticmethod
    def readlines(filename):
        for i in filename:
            f = open(filename, "r")
            return f.read().splitlines()
