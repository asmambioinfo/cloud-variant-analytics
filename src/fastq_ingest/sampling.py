"""
fastq_ingest.sampling
sampling utilities for fastq records

sampling records instead of reading the entire file into memory which can be huge. 
purpose:
- read a subset of records from fastq files for quick qc
- investigate records (header, sequence, plus, and quality) without loading the entire file
- Two methods for sampling:
    1. Reservoir sampling: radomly sample k records from the entire file. Notice that we don't need to know hte total number of records in advance.
        the stream of records is processed one by one and reservioir sampling algorithm ensures that each record has an equal probability of being included 
        or replaced in the sample set. 
    2. head/tail sampling where sample from first n records (head) and last n records (tail) of the fastq file is extracted to investigate potential issues at the beginning or end of the file.
python compatible with version 3.6+
"""
import random
from collections import deque
from typing import Iterator, List, Dict, Optional, Tuple, Deque

from .reader import FastqReader
from .models import Record 



def reservoir_sample(path: str, k: int, seed:Optional[int]=None) -> Tuple[List[Record], int]:
    """
    get sample of k records from a stream of fastq records without having to know the total number of records in advance. 
    earlier records have better chance of being included, but also higher chance of being replaced as we process more records.
    later records have lower chance of being included but if included, they stay in the sample set (lower chance of being replaced).
    """
    rng = random.Random(seed)
    sample: List[Record] = []
    total = 0
    for record in FastqReader(path).records():
        total +=1
        if len(sample) < k:
            sample.append(record)
        else:
            j = rng.randint(1, total)
            if j <= k: 
                sample[j - 1] = record



    return sample, total

    def head_tail_sample(path: str, n: int) -> Tuple[List[Record], int]:
        """
        get head and tail samples of n records each from fastq file 
        """
        head: List[Record] = []
        tail: Deque[Record] = deque(maxlen=n)
        total = 0
        for record in FastqReader(path).records():
            total +=1
            if len(head) < n:
                head.append(record)
            tail.append(record)
            
        tail_list: List[Record] = list(tail)
        head_idx = set([r.idx for r in head])
        combined = head + [r for r in tail_list if r.idx not in head_idx]

        
        return combined, total



