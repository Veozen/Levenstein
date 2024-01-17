# Function LevDist

Implements an extension to Lenvenstein string distance. In addition to insertion, deletion, substitution and swaps of characters, the method also considers substring swaps as one operation. This leads to a distance betwenn two strings that is always at most as large as the original Levenstein distance.

    
Lev("abce","cdab") # ==  2  
Lev("JohnSmith","SmithJohn") # == 1 
