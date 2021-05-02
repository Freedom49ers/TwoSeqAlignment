import argparse

from Bio import SeqIO
from Bio import pairwise2
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

description = """

Aligns two DNA sequences from a fasta file using a local alignment algorithm.

"""

parser = argparse.ArgumentParser(description=description)

parser.add_argument("filename")
parser.add_argument("method", type=str ,help="options: local")

args = parser.parse_args()


seq1, seq2 = list(SeqIO.parse(args.filename, "fasta"))

def show_results(alns):
    for aln in alns:
       print(aln)

if args.method == "local":
    alignments = pairwise2.align.localxx(seq1.seq, seq2.seq)
    show_results(alignments)
