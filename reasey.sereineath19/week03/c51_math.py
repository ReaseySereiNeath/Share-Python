class MathsModule:
    @staticmethod
    def get_min(number):
        return min(number)

    @staticmethod
    def get_max(number):
        return max(number)

    @staticmethod
    def get_min_max(number):
        return (min(number), max(number))

    @staticmethod
    def average(number):
        sum = 0
        for i in number:
            sum = sum + i
        average = sum / len(number)
        return average

    @staticmethod
    def diff(number):
        sum = max(number) - min(number)
        return sum
