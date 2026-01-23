<<<<<<< HEAD
=======
<<<<<<< HEAD

>>>>>>> 4ab9a0d (README update)
# cloud-variant-analytics

is a reference implementation of an end-to-end cloud-native data engineering pipeline for genomic variant processing and analytics. The project demonstrates how raw sequencing data can be ingested, processed, annotated, and transformed into analytics-ready datasets using modern AWS data engineering patterns.

The platform ingests BAM files into Amazon S3, executes containerized variant calling workflows, and enriches results using public clinical and oncology annotation sources. Processed data is normalized and transformed using PySpark on AWS Glue, stored in columnar formats, and exposed for interactive querying through Athena or Redshift Serverless. A lightweight Streamlit application provides visibility into pipeline execution, summary metrics, and curated variant outputs.

<<<<<<< HEAD
This project is designed to highlight scalable data pipeline architecture, reproducibility, and cloud best practices rather than clinical interpretation. All workflows are built from scratch using public datasets and synthetic metadata, with no patient data, PHI, or proprietary pipelines included.
=======
This project is designed to highlight scalable data pipeline architecture, reproducibility, and cloud best practices rather than clinical interpretation. All workflows are built from scratch using **public datasets and synthetic metadata**, with no patient data, PHI, or proprietary pipelines included.

## Assumptions (MVP)

* Input: human whole-exome sequencing (WES), Illumina 2×150 bp paired-end FASTQ
* Reference genome: GRCh38/hg38
* Target regions: RefSeq exonic intervals with ±50 bp padding (BED)
* QC and trimming:

  * adapter and low-quality tail trimming at Phred Q20
  * minimum read length ≥50 bp after trimming
  * report percentage of bases ≥Q30
=======
# cloud-variant-analytics

is a reference implementation of an end-to-end cloud-native data engineering pipeline for genomic variant processing and analytics. The project demonstrates how raw sequencing data can be ingested, processed, annotated, and transformed into analytics-ready datasets using modern AWS data engineering patterns.

The platform ingests BAM files into Amazon S3, executes containerized variant calling workflows, and enriches results using public clinical and oncology annotation sources. Processed data is normalized and transformed using PySpark on AWS Glue, stored in columnar formats, and exposed for interactive querying through Athena or Redshift Serverless. A lightweight Streamlit application provides visibility into pipeline execution, summary metrics, and curated variant outputs.

This project is designed to highlight scalable data pipeline architecture, reproducibility, and cloud best practices rather than clinical interpretation. All workflows are built from scratch using public datasets and synthetic metadata, with no patient data, PHI, or proprietary pipelines included.
>>>>>>> bb5c22b (initial project)
>>>>>>> 4ab9a0d (README update)
