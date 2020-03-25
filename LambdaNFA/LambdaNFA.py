with open("lambdaNFA.in") as f:

    n = int(f.readline())
    m = int(f.readline())
    ListaCaractere = [x for x in f.readline().split()]
    q0 = int(f.readline())
    NrStariFinale = int(f.readline())
    Final = {int(x) for x in f.readline().split()}
    NrTranzitii = int(f.readline())
    Tranzitie=[{} for i in range(n)]
    Stare = f.readline()
    while Stare!='':
        (a,b,c)=[x for x in Stare.split()]
        if b not in Tranzitie[int(a)]:
            Tranzitie[int(a)][b]=set()
        Tranzitie[int(a)][b].add(int(c))
        Stare=f.readline()
    print(Tranzitie)
    def Verificare(Cuvant,stari):
        StariN = stari
        StariV = set()
        while StariV!=StariN:
            StariV=StariN
            for x in StariV:
                if '$' in Tranzitie[x]:
                    StariN = StariN.union(Tranzitie[x]['$'])
        if Cuvant=='':
            return Final.intersection(StariN)!=set()
        else:
            Aux = set()
            for x in StariN:
                if Cuvant[0] in Tranzitie[x]:
                    Aux=Aux.union(Tranzitie[x][Cuvant[0]])
            return Verificare(Cuvant[1:],Aux)
    Set = set()
    Set.add(q0)
    print(Verificare('bcax',Set))
    print(Verificare('abxyyyxyby', Set))
    print(Verificare('bcbxxy', Set))