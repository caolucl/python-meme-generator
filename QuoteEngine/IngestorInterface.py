"""Create a abstract class IngestorInterface."""
from abc import ABC, abstractmethod
from typing import List
from QuoteEngine.QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Define a class."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Specify which type of a file and check if the file is ingested.

        Types of files: Docx, CSV, PDF, Txt.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstrach method to be refactored in inherited classes."""
        pass
