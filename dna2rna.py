from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Align import MultipleSeqAlignment

records = list(SeqIO.parse("seqs.fasta", "fasta"))
filterd_records = []
for chosen in list(filter(lambda c: len(c.seq) < 200, records))[0:149]:
    chosen.seq = chosen.seq.transcribe()
    print(chosen.seq)
    filterd_records.append(chosen)
print len(filterd_records)
SeqIO.write(filterd_records, 'seqs_rna.fasta', "fasta")

align = MultipleSeqAlignment(filterd_records)
print(align)
