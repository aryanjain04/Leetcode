import heapq
from typing import List

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}
        self.cuisine_heaps = {}
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_info[f] = [c, r]
            if c not in self.cuisine_heaps:
                self.cuisine_heaps[c] = []
            heapq.heappush(self.cuisine_heaps[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_info[food]
        self.food_info[food][1] = newRating
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.food_info[food][1]:
                return food
            heapq.heappop(heap)

        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)