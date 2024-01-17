# Function LevDist

Implements an extension to Lenvenstein string distance. In addition to insertion, deletion and subsitution of characters, the method also considers substring swaps as one operation. 
This leads to a distance betwenn two strings that is always at most as large as the original Levenstein distance.

    
LevDist("abce","cdab") # ==  2  
LevDist("JohnSmith","SmithJohn") # == 1 
