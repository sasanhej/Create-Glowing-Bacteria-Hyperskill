def compl(strand):
    return ''.join(['A' if i=='T' else ('T' if i == 'A' else ( 'G' if i == 'C' else 'C')) for i in strand])


def cutGFP(strand, rss):
    rs = rss.split()

    orispl = strand.split(rs[0])
    ori1st = rs[0][1:] + rs[0].join(orispl[1:])
    orisp2 = ori1st.split(rs[1])
    ori2nd = orisp2[0] + rs[1][:1]

    comspl = compl(strand).split(compl(rs[0]))
    com1st = compl(rs[0][5]) + compl(rs[0]).join(comspl[1:])
    comsp2 = com1st.split(compl(rs[1]))
    com2nd = comsp2[0] + compl(rs[1][:5])

    return ori2nd, com2nd


def cutplasimid(strand, rs='CTGCAG'):

    orispl = strand.split(rs)
    ori1st = orispl[0] + rs[:1]
    ori2nd = rs[1:] + ''.join(orispl[1:])

    comspl = compl(strand).split(compl(rs))
    com1st = comspl[0] + compl(rs[:5])
    com2nd = compl(rs[5:]) + ''.join(comspl[1:])

    return ori1st, ori2nd, com1st, com2nd


def attach(file):
    data = open(file).read().split('\n')
    plasimid, plasimidrs, GFP, GFPrs = data[:4]
    plasmid_original_1st, plasmid_original_2nd, plasmid_complementary_1st, plasmid_complementary_2nd = cutplasimid(plasimid, plasimidrs)
    GFP_original, GFP_complementary = cutGFP(GFP, GFPrs)
    first = plasmid_original_1st + GFP_original + plasmid_original_2nd
    second = plasmid_complementary_1st + GFP_complementary + plasmid_complementary_2nd
    return first, second


file = input()
#file = 'plasmid_gfp_example.txt'
attached = attach(file)
print(attached[0], attached[1], sep='\n')
