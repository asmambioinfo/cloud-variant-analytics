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
    def __init__(self, path: str):
        self.path = path 
    
    def records(self) -> Iterator[Record]:
        """
        read fasetq file and yield Record objects
        raise error if any of the records are truncates: missing any of the 4 lines
        """
        with open_text(self.path) as fh:
            idx = 0
            while True:
                h = fh.readline()
                if not h:
                    break
                s = fh.readline()
                p = fh.readline()
                q = fh.readline()

                if (not s) or (not p) or (not q): 
                    raise ValueError(f"Truncated record detected at record index {idx} in file {self.path}")
                
                yield Record(h.rstrip("\n"), s.rstrip("\n"), p.rstrip("\n"), q.rstrip("\n"), idx)
                idx +=1






