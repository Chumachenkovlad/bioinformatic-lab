with open('result.tsv') as f:
    with open('f.tsv', 'w') as fw:
        for line in list(f.readlines()):
            l = line.split()
            s = '{}\t{}\n'.format(l[0], l[1])
            if float(l[2]) > 1:
                print(l[0], l[1])
                fw.write(s)
