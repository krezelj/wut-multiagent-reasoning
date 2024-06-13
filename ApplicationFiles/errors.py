class SpaceException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class EmptyWordException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class DigitWordException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)