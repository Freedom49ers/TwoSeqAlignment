import argparse

from Bio import SeqIO
from Bio import pairwise2

description = """

Aligns two DNA sequences from a fasta file using a local alignment algorithm.

"""

parser = argparse.ArgumentParser(prog='Local_Seq_Aligner', description=description)

## Introduces the positional arguments filename, method and local
parser.add_argument("filename")
parser.add_argument("method", type=str ,help="options: local")

args = parser.parse_args()


seq1, seq2 = list(SeqIO.parse(args.filename, "fasta"))

def show_results(alns):
    for aln in alns:
       print(aln)

##Introducing a conditional statement, that aligns and shows the sequences in stdout
if args.method == "local":
    alignments = pairwise2.align.localxx(seq1.seq, seq2.seq)
    show_results(alignments)
