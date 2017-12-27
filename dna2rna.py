from Bio import SeqIO
from Bio.Seq import Seq

records = list(SeqIO.parse("seqs.fasta", "fasta"))
filterd_records = []
for chosen in filter(lambda c: len(c.seq) < 200, records):
    print(len(chosen.seq))
    chosen.seq = chosen.seq.transcribe()
    filterd_records.append(chosen)
print len(filterd_records)
SeqIO.write(filterd_records, 'seqs_rna.fasta', "fasta")
