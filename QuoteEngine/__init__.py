"""Create Ingestor class to involve all ingestors."""
# pylint: disable=redefined-outer-name
from typing import List
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.TxtIngestor import TxtIngestor


class Ingestor(IngestorInterface):
    """Define Ingestor class.
    
    Ingestor contains four types of ingestos for each file tpye.
    """

    Ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Retuen a list of quote from a file.
        
        A function will inclue all ingestors.
        Based on the file type, a ingestor will be choosen to process the file.
        """
        for Ingestor in cls.Ingestors:
            if Ingestor.can_ingest(path):
                return Ingestor.parse(path)
