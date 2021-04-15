class Poker:
    valueOrdering = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                     'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    handRanking = {1: 'Royal Flush', 2: 'Straight Flush', 3: 'Four of a kind', 4: 'Full House',
                   5: 'Flush', 6: 'Straight', 7: 'Three of a kind', 8: 'Two pair',
                   9: 'Pair', 10: 'High Card'}

    def __init__(self, inputString):
        self.valueSet = []
        self.suitSet = []
        hand = inputString.split()
        for iterator in range(5):
            self.valueSet.append(hand[iterator][0])
            self.suitSet.append(hand[iterator][1])
        self.sort_value_set()

    def sort_value_set(self):
        for counter in range(len(self.valueSet)):
            for counterTwo in range(0, len(self.valueSet) - 1):
                if self.valueOrdering[self.valueSet[counterTwo]] > self.valueOrdering[self.valueSet[counterTwo + 1]]:
                    self.valueSet[counterTwo], self.valueSet[counterTwo + 1] = \
                        self.valueSet[counterTwo + 1], self.valueSet[counterTwo]

    def get_value_ordering(self):
        valueList = self.valueOrdering.keys()
        return ''.join(valueList)

    def hand_ranks_for_same_suit(self):
        valueString = self.get_value_ordering()
        if valueString.__contains__(''.join(self.valueSet)):
            if ''.join(self.valueSet) == 'TJQKA':
                return 1  # Royal Flush
            return 2  # Straight Flush
        if ''.join(self.valueSet[:4]) == '2345' and self.valueSet[4] == 'A':  # Straight flush check for A2345
            return 2
        return 5  # Flush

    def hand_ranks_for_different_suit(self):
        uniqueValues = list(set(self.valueSet))
        valueString = self.get_value_ordering()
        if len(uniqueValues) == 2:
            if uniqueValues[0].count(self.valueSet[0]) == 1 or uniqueValues[0].count(self.valueSet[0]) == 4:
                return 3  # Four of a kind
            else:
                return 4  # Full house
        elif len(uniqueValues) == 3:
            if uniqueValues[0].count(self.valueSet[0]) == 3 or uniqueValues[1].count(self.valueSet[0]) \
                    or uniqueValues[2].count(self.valueSet[0]):
                return 7  # Three of a kind
            return 8  # Two pair
        elif len(uniqueValues) == 4:
            return 9  # Pair
        else:
            if valueString.__contains__(''.join(self.valueSet)) or \
                    (''.join(self.valueSet[:4]) == '2345' and self.valueSet[4] == 'A'):
                return 6  # Straight
        return 10  # For high card

    def get_rank(self):
        print(self.valueSet)
        isSameSuitFlag = len(set(self.suitSet))
        if isSameSuitFlag == 1:
            return self.hand_ranks_for_same_suit()
        else:
            return self.hand_ranks_for_different_suit()

    def get_hand_name(self, rank):
        return self.handRanking[rank]

    def get_card_value(self, position):
        return self.valueOrdering[self.valueSet[position]]


def high_card_decision(playerOne, playerTwo):
    for iterator in range(4, -1, -1):
        highCardValueOfPlayerOne = playerOne.get_card_value(iterator)
        highCardValueOfPlayerTwo = playerTwo.get_card_value(iterator)
        if highCardValueOfPlayerOne > highCardValueOfPlayerTwo:
            print('Player 1 got high card. Winner!!')
            return
        elif highCardValueOfPlayerOne < highCardValueOfPlayerTwo:
            print('Player 2 got high card. Winner!!')
            return
    print('Its a tie game!!!')


def find_winner(playerOne, playerTwo):
    rankOfPlayerOne = playerOne.get_rank()
    rankOfPlayerTwo = playerTwo.get_rank()
    if rankOfPlayerOne < rankOfPlayerTwo:
        print(playerOne.get_hand_name(rankOfPlayerOne)+' is more powerful.. Player 1 wins the round')
    elif rankOfPlayerOne > rankOfPlayerTwo:
        print(playerTwo.get_hand_name(rankOfPlayerTwo)+' is more powerful.. Player 2 wins the round')
    else:
        high_card_decision(playerOne, playerTwo)


if __name__ == '__main__':
    player1 = Poker(input())
    player2 = Poker(input())
    find_winner(player1, player2)
