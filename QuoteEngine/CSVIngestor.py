"""Create a class to extract data from a CSV file."""
# pylint: disable=unused-variable
from typing import List
import pandas
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Define CSVIngestor class."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse function to extract data from CSV file.

        The function will return list of quotes from data.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        Quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_Quote = QuoteModel(row['body'], row["author"])
            Quotes.append(new_Quote)
        return Quotes
