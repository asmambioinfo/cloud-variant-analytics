"""
Fastq_ingest.reader module
streaming data reader for fastq files: 
purpose: 
read fastq as 4-line records
produced records objects with 0-based index
detect truncated recrords 
"""
from typing import Iterator
from .io import open_text
from .models import Record

class FastqReader(object):
    def __intit__(self, path: str):
        self.path = path 
        


