# src/cva/config.py

"""
Configuration management for pipeline execution

"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Optional 


@dataclass(frozen=True)
class PipelineConfig:
    """
    defined configuration for pipeline execution
    Mainly used to define the pipelines inputs and outputs, but can be extended to 
    include other parameters as needed. 
    Mainly for paired-end sequencing data. 
    """
    #input files
    r1: Path
    r2: Path

    # References: 
    ref_fasta: Path
    ref_bed: Path # in case analysis needs to restercted on certain regions. 

    # output 
    output_dir: Path

    #runtime parameters:
    threads: int = 8

    # tools:
    baw: str = "bwa"
    samtools: str = "samtools"
    gatk: str = "gatk"
    bcftools: str = "bcftools"
    tabix: str = "tabix"

    # Sequenceer quality control parameters:
    min_base_quality: int = 20 # error rate of 1% or less
    min_mapping_quality: int = 30 # error rate of 0.1% or
    min_length: int = 50 # minimum read length to consider for analysis (associated with mapping quality)
    
    #adapter sequences to trim (if needed) # add if sequencer is not trimming adapters.




