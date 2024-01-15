
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = set()
        loss_count = {}

        # Iterate through the matches and update winners, losers, and loss count
        for winner, loser in matches:
            winners.add(winner)
            losers.add(loser)
            loss_count[loser] = loss_count.get(loser, 0) + 1

        # Find players with zero and one loss
        players_with_zero_loss = [player for player in winners if player not in losers]
        players_with_one_loss = [player for player, count in loss_count.items() if count == 1]

        # Sort the lists in increasing order
        players_with_zero_loss.sort()
        players_with_one_loss.sort()

        # Return the result as a list of two lists
        return [players_with_zero_loss, players_with_one_loss]
