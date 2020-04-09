class MatrixModule:
    @staticmethod
    def gen_empty_matrix(height, width):
        if height <= 0 or width <= 0:
            return None
        rows, cols = (height, width)
        arr = [["" for i in range(cols)] for j in range(rows)]
        return arr

    @staticmethod
    def gen_value_matrix(value, height, width):
        if height <= 0 or width <= 0:
            return None
        rows, cols = (height, width)
        arr = [[value for i in range(cols)] for j in range(rows)]
        return arr
