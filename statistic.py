from Bio import AlignIO
from math import log2


def get_key(i, j):
    return '{}_{}'.format(i, j)


def m_i_j(i, j):
    m = 0
    for pair in NUCLEOTIDES_PAIRS:
        fij = double_column_frequincies[get_key(i, j)][pair]
        fi = column_frequincies[i][pair[0]]
        fj = column_frequincies[i][pair[1]]
        if (fi * fj != 0):
            f = fij / (fi * fj)
            if (f != 0):
                m += fij * log2(f)
    return m


NUCLEOTIDES = ['A', 'C', 'G', 'U']
NUCLEOTIDES_PAIRS = [
    'AA', 'CA', 'GA', 'UA', 'CC', 'GC', 'UC', 'UG', 'UU', 'GG'
    'AC', 'AG', 'AU', 'CG', 'CU', 'GU']
alignment = AlignIO.read("aln.fasta", "fasta")
column_length = len(alignment[0].seq)
seqs_lengs = len(alignment)
columns = []
double_columns = {}
column_frequincies = []
double_column_frequincies = {}

final_result = []


for column_index in range(column_length):
    columns.append([])
    for aln_index in range(seqs_lengs):
        columns[column_index].append(alignment[aln_index].seq[column_index])

for i in range(column_length):
    column_frequincies.append({})
    for nucleotide in NUCLEOTIDES:
        column_frequincies[i][nucleotide] = columns[i].count(
            nucleotide) / seqs_lengs

for i in range(column_length):
    for j in range(column_length):
        key = get_key(i, j)
        double_columns[key] = ['{}{}'.format(
            columns[i][row_index], columns[j][row_index]) for row_index in range(seqs_lengs)]


for key in double_columns.keys():
    double_column_frequincies[key] = {}
    for pair in NUCLEOTIDES_PAIRS:
        double_column_frequincies[key][pair] = double_columns[key].count(
            pair) / seqs_lengs

with open('result.tsv', 'w') as f:
    for i in range(column_length):
        for j in range(column_length):
            m = m_i_j(i, j)
            res_i_j = '{} {} {}\n'.format(i, j, m)
            f.write(res_i_j)
            print(res_i_j)
