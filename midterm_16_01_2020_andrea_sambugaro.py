def createCouple(aa):
    couples=[]
    for x in range(len(aa)):
        for i in range (len(aa)):
            c=aa[x]+aa[i]
            if c[::-1] not in couples:
                couples.append(c)
    #print couples
    return couples

def collectColumns(matrix):
    score=[]
    for line in matrix:
        line=line.rstrip()
        line=line.split()
        score.append(line)
    x=20
    columns=[]
    for n in range(20):
        col=[]
        for j in range(x):
            col.append(score[j][n])
        x=x-1
        columns.extend(col)
        del score[0]
    return columns


def createDictionary(couples, score):
    dictionary={}
    i=0
    for c in couples:
        dictionary[c]=score[i]
        i+=1
    #print (dictionary['VV'])
    return dictionary

def scoring(seq1, seq2,dict):
    s = 0
    for i in range(len(seq1)):
        m_key = seq1[i]+seq2[i]
        mr_keyr= seq2[i]+seq1[i]
        if dict.has_key(m_key):
            s = s + int(dict[m_key])
        elif dict.has_key(mr_keyr):
            s = s + int(dict[mr_keyr])
        elif "-" in m_key:
            s-=2
    return s



def readInput(fasta_file):
    seqs = []
    for line in fasta_file:
        if not line.startswith('>'):
            seqs.append(line.strip())
    return seqs

def alignment_score(seqs,CreateCouples,Scores,Scores1):
    Dictionary=createDictionary(CreateCouples,Scores)
    print seqs[0]
    print seqs[1]
    print ('The score from PAM is: '+ str(scoring(seqs[0],seqs[1],Dictionary)))
    Dictionary=createDictionary(CreateCouples,Scores1)
    print ('The score from BLOSUM is: '+ str(scoring(seqs[0],seqs[1],Dictionary)))



file1=open("./alignments.fasta")



pam=open("./PAM250.txt","r")
blosum62=open("./blosum62.txt","r")
aminoacid="ARNDCQEGHILKMFPSTWYV"
Scores=collectColumns(pam)
Scores1=collectColumns(blosum62)
CreateCouples=createCouple(aminoacid)
seqs=readInput(file1)
alignment_score(seqs,CreateCouples,Scores,Scores1)
