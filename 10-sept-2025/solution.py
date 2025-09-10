from typing import List
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        
        user_lang = [set(l) for l in languages]
     
        problematic_users = set()
        for u, v in friendships:
            if user_lang[u-1].isdisjoint(user_lang[v-1]): 
                problematic_users.add(u-1)
                problematic_users.add(v-1)
      
        if not problematic_users:
            return 0

        min_teach = float('inf')
        for lang in range(1, n+1):
            knows_lang = sum(1 for u in problematic_users if lang in user_lang[u])
            need_teach = len(problematic_users) - knows_lang
            min_teach = min(min_teach, need_teach)

        return min_teach
    


    
  