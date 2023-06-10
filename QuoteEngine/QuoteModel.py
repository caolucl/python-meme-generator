"""Create a class for quotes."""


class QuoteModel:
    """Define QuoteModel class."""

    def __init__(self, body="", author=""):
        """Define a contrunction class.

        The method contains body which is content of
        quote and author of the quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Reprent data of a quote."""
        return f"{self.body} - {self.author}"
