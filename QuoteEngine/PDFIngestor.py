"""Create a class to extract data from a PDF file."""
# pylint: disable=unused-variable
from typing import List
import subprocess
import os
import random
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Define PDFIngestor class."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse function to extract data from PDF file.

        The function will return list of quotes from data.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        Quotes = []
        tmp = f'./tmp/{random.randint(0,100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])
        file_ref = open(tmp, "r")
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split(' - ')
                print(parse)
                new_Quote = QuoteModel(parse[0], parse[1])
                Quotes.append(new_Quote)
        file_ref.close()
        os.remove(tmp)
        return Quotes
