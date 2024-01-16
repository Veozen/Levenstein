def LevDist(a: str,b: str):
    memo={}
    
    def Lev(s: str,t: str):
        #calculate the levenstein distance between two strings
        nonlocal memo
        if (s,t) in memo:
            return memo[(s,t)]
        else:
            if len(s)==0:
                return len(t)
            if len(t)==0:
                return len(s)
                
            Dist=0    
            if s[0]==t[0]:
                Dist = Lev(s[1:],t[1:])
            else:
                
                #find the longes prefix in s that can be found in t
                DistPrefixS=max(len(s),len(t))
                for l in range(len(s),1,-1):
                    prefix=s[:l]
                    #find the prefix in t
                    pos=t.find(prefix)
                    if pos>0:
                        DistPrefixS = 1 + Lev(s[l:],t[:pos] + t[pos+l:])
                        break
             
                #find the longest prefix in t that can be found in s
                DistPrefixT=max(len(s),len(t))
                for l in range(len(t),1,-1):
                    prefix=t[:l]
                    #find the prefix in t
                    pos=s.find(prefix)
                    if pos>0:
                        DistPrefixT = 1 + Lev(t[l:],s[:pos] + s[pos+l:])
                        break
                
                #see if the first two char can be swapped 
                DistSwaps=max(len(s),len(t))
                if len(s)>=2 and len(t)>=2 and s[0]==t[1] and s[1]==t[0]:
                    DistSwaps = 1+ Lev(s[2:],t[2:])
                                             
                DistDeletes = 1 + min(Lev(s[1:],t),Lev(s,t[1:]),Lev(s[1:],t[1:]))
                Dist = min(DistDeletes,DistSwaps,DistPrefixS,DistPrefixT)
            memo[(s,t)]=Dist
            
            return Dist
    
    return Lev(a,b)
    
LevDist("abce","cdab")
LevDist("JohnSmith","SmithJohn")
