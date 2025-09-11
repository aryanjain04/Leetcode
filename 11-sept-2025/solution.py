#2785. Sort Vowels in a String 

class Solution:
    def sortVowels(self, s: str) -> str:
        
        str_list = list(s)
        vowels_ascii = {65, 69, 73, 79, 85, 97, 101, 105, 111, 117}
        
        vowels = [ch for ch in str_list if ord(ch) in vowels_ascii]

        vowels.sort()
        
        res =  []
        counter = 0
        for ch in str_list:

            if ord(ch) in vowels_ascii:
                res.append(vowels[counter])
                counter+=1

            else:
                res.append(ch)

        return "".join(res)
                