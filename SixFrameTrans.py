from Bio.Seq import Seq
from Bio.SeqUtils import six_frame_translations

seq1 = Seq("ATGCCTTGAAATGTATAG")
print(six_frame_translations(seq1))