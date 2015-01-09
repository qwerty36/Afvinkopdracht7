################################################################
################################################################
##Application for sequence processing and transctription########
##Richard Jansen, HAN University of Applied Sciences Nijmegen###
##9-1-2014######################################################
################################################################

#######################
##Variables and shit###
#######################
bestand = open("sequentie.txt")
x = str(bestand.readline())
total = len(x)
C = x.count("c")
G = x.count("g")
A = x.count("a")
T = x.count("t")
RNAseq = []

###################
##Main Functions###
###################
def main():
    DNAcheck()
    print (" ")
    DNAtoRNA()
    print (" ")
    STARTandSTOPpos()
    print (" ")
    BONUSSHIZZLE()
    
def DNAcheck():
    if total == (A+T+C+G):
        print ("THIS IS DNA")
    else:
        print ("THIS AINT NO D,N and A!!!")

def DNAtoRNA():
    prepreRNA = (x.replace("a","T").replace("t","A").replace("c","G").replace("g","C"))
    preRNA = prepreRNA.replace("T","U")
    RNA = preRNA[::-1]
    print (RNA.upper())
    RNAseq.append(RNA)

def STARTandSTOPpos():
    RnaString = str(RNAseq)
    rnaString = (RnaString.replace("[","").replace("]","").replace("'",""))
    z, s = 0, 3
    codonseq = ''
    startindex = rnaString.index('AUG')
    print('Startcodon on location: ' +str(startindex))
    for z in range (startindex, (len(rnaString)-startindex)):
        codon = rnaString[s-3:s]
        codonseq += codon
        if codon in ('UAA', 'UGA', 'UAG'):
            print('Stopcodon on location: ' +str(z//3+startindex))
            break
        else:
            s += 3
    print(codonseq) 

##########
##Bonus###
##########
def BONUSSHIZZLE():
    rnaseq = str(RNAseq)
    seq = (rnaseq[::-1])
    print (seq)
    
main()