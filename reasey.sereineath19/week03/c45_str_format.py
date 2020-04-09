class StringFormat:
    @staticmethod
    def first(text):
        if len(text) == 0:
            return '""'
        else:
            return text[0]

    @staticmethod
    def last(text):
        if len(text) == 0:
            return '""'
        else:
            return text[-1]

    @staticmethod
    def lower(text):
        if len(text) == 0:
            return '""'
        else:
            return text.lower()

    @staticmethod
    def upper(text):
        if len(text) == 0:
            return '""'
        else:
            return text.upper()

    @staticmethod
    def reversed(text):
        if len(text) == 0:
            return '""'
        else:
            return text[::-1]
