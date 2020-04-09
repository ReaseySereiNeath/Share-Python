class HTMLGen:
    @staticmethod
    def comment(strings):
        return f'<!--"{strings}"-->'

    @staticmethod
    def title(strings):
        return f'<title>"{strings}"</title>'

    @staticmethod
    def body(strings):
        return f'<body>"{strings}"</body>'

    @staticmethod
    def div(strings):
        return f'<div>"{strings}"</div>'

    @staticmethod
    def p(strings):
        return f'<p>"{strings}"</p>'

    @staticmethod
    def href(strings, name):
        return f'<a href="{strings}">{name}</a>'
