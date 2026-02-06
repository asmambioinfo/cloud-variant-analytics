From __future__ import annotations

import argparse
import logging
import os 
from pathlib import Path 
from cva.config import PipelineConfig
from cva.core import pipeline


def main(args: argparse.Namespace) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", required= True, help= "Sample identifier")
    ap.add_argument("--fastq_dir", required= True, help="s3:// path to fasetq filea") 
    