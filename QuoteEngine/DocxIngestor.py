"""Create a class to extract data from a Docx file."""
from typing import List
import docx
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Define DocxIngestor class."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse function to extract data from Docx file.

        The function will return list of quotes from data.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        Quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                new_Quote = QuoteModel(parse[0], parse[1])
                Quotes.append(new_Quote)
        return Quotes
