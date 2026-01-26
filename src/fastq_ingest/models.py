"""
fastq_inges.models 
used across fastq_ingest/qc 

lightweight data classes: 
- used to store data structures
- serilaze cleanly to dictionaries for jason reporting 

python compatible with version 3.6+

"""
from typing import any, List, Dict, Optional

class Record(object):
    def __init__(self, h: str, s: str, p: str, q: str, idx: int):
        self.header = h # sequence header
        self.seqeuence = s # sequence 
        self.plus = p # plus
        self.quality = q # sequence quality
        self.index = idx # record index


class Issue(object):
    def __init__(self, code: str, message: str, record_idx: Optional[int] = None, read_name: Optional[str] = None, extra: Optional[Dict[str, any]] = None):
        self.code = code # issue code 
        self.message = message # issue message
        self.record_idx = record
        self.read_name = read_name 
        self.extra = extra or {}

        def to_dict(self) -> Dict[str, any]:
            return {
                "code": self.code, 
                "message": self.message, 
                "record_idx": self.record_idx, 
                "read_name":self.read_name, 
                "extra": self.extra

            }
class FastqPair(object):
    def __init__(self, r1_path: str,r2_path: Optional[str] = None, SampleID: Optional[str] = None):
        self.r1_path = r1_path # path to read 1 fastq file 
        self.r2_path = r2_path # path to read 2 fastq file 
        self.SampleID = SampleID # sample identifier

class IngestReport(object): 

    """
    Docstring for IngestReport
    suitalbe for dictionary serialization for json reporting 
    status: PASS |WARN | FAIL 
    input/check/sample/results: plain dict for json serialization
    """

    def __init__(self, input: Dict[str, any],
                  check: Dict[str, any], sample: Dict[str, any], results: Dict[str, any], status: str):
             self.input = input
             self.check = check 
             self.sample = sample 
             self.results = results
             self.status = status
        
    def to_dict(self) -> Dict[str, any]:
        return {
                "input": self.input, 
                "sample": self.sample, 
                "check": self.check, 
                "results": self.results, 
                "status": self.status
        }

