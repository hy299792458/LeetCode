class Solution(object):
    def predictPartyVictory(self, senate):
        senate = [char for char in senate]
        ban = ["R", 0]
        pair = {"R" : "D", "D" : "R"}
        while True:
            nextRound = []
            cnt = {"D": 0, "R": 0}
            for i in range(len(senate)):
                if ban[1] == 0:
                    ban = [pair[senate[i]], 1]
                    nextRound.append(senate[i])
                    cnt[senate[i]] += 1
                elif ban[0] != senate[i]:
                    ban[1] += 1
                    nextRound.append(senate[i])
                    cnt[senate[i]] += 1
                else:
                    ban[1] -= 1
            if cnt["D"] == 0:
                return "Radiant"
            if cnt["R"] == 0:
                return "Dire"
            senate = nextRound
