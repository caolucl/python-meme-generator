# Ingestors Module

This module reads quotes from various files and returns a list of processed
quotes.

## Dependencies

[pandas](https://pandas.pydata.org/): for reading CSV files.

[python-docx](https://python-docx.readthedocs.io/en/latest/): for reading DOCX files.

[pdftotext](https://www.xpdfreader.com/pdftotext-man.html): for converting PDF files to plain text

## Usage

Import the main `Ingestor` class and use its class method `parse`.

You can run this module in command line using the following command:
```
python -m ingestors --path <path_of_the_file>
```

## Models

### IngestorInterface
This class is an interface that is used as a base class for all other
ingestors, such as CSV, PDF, Docx, Txt. 
The method `can_ingest` is usued to check if a file is ingested.
The abstract class method `parse` is declared and implemented in inherited classes.

### CSVIngestor
This ingestor implements the `parse` method to read CSV files by lines and return a list of quotes by using `pandas` library to read CSV files

### DocxIngestor
This ingestor implements the `parse` method to read DOCX files by lines and return a list of quotes by using `python-docx` library.

### PDFIngestor
This ingestor implements the `parse` method to read PDF files and extract its lines into a text file by using `pdftotext` command line , then read each lines in the text file and return a list of quotes.

### TextIngestor
This ingestor implements the `parse` method to read TXT files by lines and return a list of quotes.

### Ingestor
The maIngestor will call all the other ingestor classes.
The `parse` methods will specify the type of files which passed on by a path argument based on their extensions and call a approriate ingestor to parse that file.
