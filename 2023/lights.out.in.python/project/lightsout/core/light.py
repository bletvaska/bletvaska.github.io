class Light:
    def __init__(self):
        self._on = False

    def is_on(self):
        return self._on

    def toggle(self):
        self._on = not self._on

    def __str__(self):
        return '1' if self.is_on() else '0'

    def __repr__(self):
        return '1' if self.is_on() else '0'
