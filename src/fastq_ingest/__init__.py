"""
fastq ingest/qc utilities for validation fastq files before proceesing downstream analysis. 

python compatible with version 3.6+
"""

from .pipeline import run_ingest
__all__ = ['run_ingest']
