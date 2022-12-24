from Bio.Seq import Seq

tatabox_seq = Seq("tataaaggcAATATGCAGTAG")
start_idx = tatabox_seq.find("ATG")
end_idx = tatabox_seq.find("TAG", start_idx)

orf = tatabox_seq[start_idx:end_idx+3]
print(orf)
