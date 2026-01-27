"""
fastq_inges.io is to: 
- provide a consistent way for openning fastq files 
- Handle compressed and uncompressed files
- keep opening file behavior contained in one location 


"""
import gzip
import io 

def open_text(path): 
    """
    Open path as text stream 
    if ends with .gz or other gzip extension, open with gzip in text mode 
    if ends with .fastq, fq extension, open as plain text file
    uses utf-8 encoding with errors "replace" to avoid crashing on bad characters. 
    
    """
    if path.endswith('.gz'): 
        return gzip.open(path, mode = 'rt', encoding = 'utf-8', errors = "replace")
    return open(path, mode = "rt", encoding = 'utf-8', errors= "replace")



