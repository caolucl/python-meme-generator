# pylint: disable=unused-variable
from typing import List
import subprocess
import os
import random
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        Quotes = []
        file_ref = open(path, "r", encoding="utf-8-sig")
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split(' - ')
                new_Quote = QuoteModel(parse[0], parse[1])
                Quotes.append(new_Quote)
        file_ref.close()
        return Quotes
