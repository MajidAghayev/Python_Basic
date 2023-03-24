


def kidsWithCandies(candies: list[int], extraCandies: int):

    for x in candies:
        if x + extraCandies > max(candies):
           print("ok")
        else:
            print("not ok")



kidsWithCandies(candies = [1, 3, 5, 4, 2],extraCandies = 1)