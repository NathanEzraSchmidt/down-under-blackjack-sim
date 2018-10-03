import random

def get_deck(deck_num, shuffle=True):
    d = list(range(1, 10)) + [10, 10, 10, 10]
    single_deck = []
    for i in range(4):
        single_deck += d
    deck = []
    for i in range(deck_num):
        deck += single_deck
    if shuffle:
        random.shuffle(deck)
    return deck

def go_dealer(hand, deck, hit_17=True):
    """
    returns total of dealer hand, pops cards from arg deck
    """
    s = sum(hand)
    ace = 1 in hand
    if (s > 7 and s < 12 and ace) or (s == 7 and ace and hit_17 == False):
        s += 10
    if s > 16:
        return s
    hand += [deck.pop(0)]
    return go_dealer(hand, deck, hit_17)

def compare_player_dealer(player, dealer_sum, push_22=True):
    """
    return values:
        0: player wins
        1: dealer wins
        2: tie
    """
    
    if type(player) == list:
        ace = 1 in player
        s = sum(player)
        if s < 12 and ace:
            s += 10
        if s == 21:
            push_22 = False
        if len(player) == 2:
            if (s == 20 and player[0] == 10):
                push_22 = False
        player_sum = s
    else:
        player_sum = player
        
    if player_sum > 21:
        return 1
    if dealer_sum == 22:
        if push_22:
            return 2
        else:
            return 0
    if dealer_sum > 21:
        return 0
    if player_sum == dealer_sum:
        return 2
    return int(dealer_sum > player_sum)

def get_hard_soft(hand):
    """
    return values:
        0: hard
        1: soft
    """
    return sum(hand) < 12 and 1 in hand

def get_small_strat(player, upcard, hand_count):
    """
    player is list of card ranks
    return values:
        stand: 0
        hit: 1
        double: 2
        split: 3
    """

    u = upcard

    s = sum(player)

    soft = get_hard_soft(player)
    """
    A8 is double or stand
    """
    if len(player) > 2 and soft:
        if s > 2 and s < 8:
            return 1
        if s == 8:
            if u in (1,6,7):
                return 1
            else:
                return 0
        else:
            return 0

    if len(player) == 2 and player[0] == player[1] and hand_count <= 4:
        x = player[0]

        if x == 1:
            return 3
        if x == 2:
            if u in (2,3,10):
                return 3
        if x == 3 or x == 4:
            if u == 10:
                return 3
        if x == 6:
            if u == 9 or u == 10:
                return 3
        if x == 7 or x == 9:
            if u in (2,3,4,9,10):
                return 3
        if x == 8:
            if u != 7:
                return 3

    if soft == 0:
        s = sum(player)
        if s < 9:
            return 1
        if s == 9:
            if u == 10:
                return 2
            else:
                return 1
        if s == 10:
            if u in (1,2,3,4,9,10):
                return 2
            else:
                return 1
        if s == 11:
            if u == 6:
                return 1
            else:
                return 2
        if s == 12 or s == 13:
            if u in (9, 10):
                return 0
            else:
                return 1
        if s == 14:
            if u in (1,2,8,9,10):
                return 0
            else:
                return 1
        if s == 15:
            if u in (1,2,3,8,9,10):
                return 0
            else:
                return 1
        if s == 16:
            if u in (1,2,3,7,8,9,10):
                return 0
            else:
                return 1
        if s > 16:
            return 0
    else:
        if s >=3 and s <= 7:
            if u == 10:
                return 2
            else:
                return 1
        if s == 8:
            if u in (1,6,7):
                return 1
            if u == 10:
                return 2
            else:
                return 0
        if s == 9:
            if u == 10:
                return 2
            else:
                return 0
        return 0

def get_medium_strat(player, upcard, hand_count):
    """
    player is list of card ranks
    return values:
        stand: 0
        hit: 1
        double: 2
        split: 3
    """

    u = upcard

    s = sum(player)

    soft = get_hard_soft(player)
    """
    A8 is double or stand
    """
    if len(player) > 2 and soft:
        if s > 2 and s < 8:
            return 1
        if s == 8:
            if u in (1,2,3):
                return 1
            else:
                return 0
        else:
            return 0

    if len(player) == 2 and player[0] == player[1] and hand_count <= 4:
        x = player[0]
        if x == 1:
            if u == 1:
                return 1
            else:
                return 3
            
        if x == 2 or x == 3:
            if u in (6,7,8,9):
                return 3
        if x == 4 and (u == 6 or u == 7):
            return 3
        if x == 6 or x == 7:
            if u >= 5 and u <= 9:
                return 3
        if x == 8:
            if u != 3 and u != 1:
                return 3
        if x == 9:
            if u == 1 or u >= 5:
                return 3
        if x == 10:
            if u == 7:
                return 3
    if soft == 0:
        s = sum(player)
        if s < 7:
            return 1
        if s == 7:
            if u == 7:
                return 2
            else:
                return 1
        if s == 8:
            if u == 7 or u == 8:
                return 2
            else:
                return 1
        if s == 9:
            if u >= 6 and u <= 9:
                return 2
            else:
                return 1
        if s == 10:
            if u >=5 and u <= 9:
                return 2
            else:
                return 1
        if s == 11:
            if u >=3 and u <= 9:
                return 2
            else:
                return 1
        if s == 12:
            if u in (5,6,7):
                return 0
            else:
                return 1
        if s == 13:
            if u >= 5 and u <= 8:
                return 0
            else:
                return 1
        if s == 14 or s == 15:
            if u >= 4 and u <= 8:
                return 0
            else:
                return 1
        if s == 16:
            if u >= 3 and u <= 8:
                return 0
            else:
                return 1
        if s == 17:
            if u == 1:
                return 1
            else:
                return 0
        if s >= 18:
            return 0
    else:
        if s >= 3 and s <= 7:
            if u in (6,7,8):
                return 2
            else:
                return 1
        if s == 8:
            if u in (6,7,8):
                return 2
            if u in (4,5,9,10): 
                return 0
            else:        
                return 1
        if s == 9:       
            if u == 6 or u == 7:
                return 2
            else:
                return 0
        if s == 10:
            if u == 7:
                return 2
            return 0
        if s >= 11:
            return 0

def get_high_strat(player, upcard, hand_count=1):
    """
    player is list of card ranks
    return values:
        stand: 0
        hit: 1
        double: 2
        split: 3
    """

    u = upcard

    s = sum(player)

    soft = get_hard_soft(player)

    if len(player) > 2 and soft:
        if s > 2 and s < 8:
            return 1
        if s == 10 or s == 11:
            return 0
        if s == 8:
            if u in (1,8,9,10):
                return 1
            else:
                return 0
        if s == 9:
            if u == 10:
                return 1
            else:
                return 0

    if len(player) == 2 and player[0] == player[1] and hand_count <= 4:
        x = player[0]
        if x == 1:
            if u in (7,8,9,10):
                return 1
            else:
                return 3
        if x == 2 or x == 3:
            if u >= 3 and u <= 7:
                return 3
        if x == 4:
            if u >= 3 and u <= 6:
                return 3
        if x == 6 or x == 7:
            if u >= 3 and u <= 7:
                return 3
        if x == 8:
            if not (u in (9,10,1)):
                return 3
        if x == 9:
            if u in (3,4,5,6,8,9):
                return 3
        if x == 10:
            if u == 6:
                return 3
        
    if soft == 0:
        if s <= 7:
            return 1
        if s == 8:
            if u in (4,5,6):
                return 2
            else:
                return 1
        if s == 9:
            if u >= 3 and u <= 6:
                return 2
            else:
                return 1
        if s == 10 or s == 11:
            if u >= 2 and u <= 6:
                return 2
            else:
                return 1
        if s == 12:
            if u >=3 and u <= 6:
                return 0
            else:
                return 1
        if s >= 13 and s <= 16:
            if u >= 2 and u <= 6:
                return 0
            else:
                return 1
        if s == 17:
            if u in (8,9,10):
                return 1
            else:
                return 0
        if s == 18:
            if u == 9 or u == 10:
                return 1
            else:
                return 0
        if s == 19:
            if u == 10:
                return 1
            else:
                return 0
        if s >= 20:
            return 0
    else:
        if s >= 2 and s <= 7:
            if u >= 3 and u <= 6:
                return 2
            else:
                return 1
        if s == 8:
            if u >= 3 and u <= 6:
                return 2
            if u == 2 or u == 7:
                return 0
            return 1
        if s == 9:
            if u >=3 and u <= 6:
                return 2
            if u == 10:
                return 1
            else:
                return 0
        if s == 10:
            if u == 5 or u == 6:
                return 2
            else:
                return 0
        if s >= 11:
            return 0

def has_bj(hand):
    return hand == [1,10] or hand == [10,1]
 
def go_player(player, dealer, deck, result=[], hand_count=[1]):
    """
    appends completed player hands to arg `result`
    arg `hand_count` is used ot limit number of splits
    splits allowed up to 4 times
    """
    
    upcard = dealer[0]
    downcard = dealer[1]

    if downcard >= 2 and downcard <= 5:
        f = get_small_strat
    elif downcard >= 6 and downcard <= 9:
        f = get_medium_strat
    else:
        f = get_high_strat
        
    action = f(player, upcard, hand_count[0])
    
    if action == 0:
        result.append(player)
    if action == 1 or (action == 2 and len(player) > 2): # hit / double
        go_player(player+[deck.pop(0)], dealer, deck, result, hand_count)
        
    if action == 2:
        x = deck.pop(0)
        result.append(player+[x])
        result.append(player+[x])
    if action == 3:
        if player[0] == 1:
            result.append([1, deck.pop(0)])
            result.append([1, deck.pop(0)])
        else:
            hand_count[0] += 1
            go_player([player[0], deck.pop(0)], dealer, deck, result, hand_count)
            go_player([player[0], deck.pop(0)], dealer, deck, result, hand_count)
        
def sim_play(sims=10000, deck_num=6, pen=26):
    """
    sims: number of hands simulated
    pen: number of cards after cut card
    """
    start = 0
    deck = get_deck(deck_num)
    for i in range(sims):
        if len(deck) < pen:
            deck = get_deck(deck_num)
        player = [deck.pop(0), deck.pop(0)]
        dealer = [deck.pop(0), deck.pop(0)]

        if has_bj(player):
            if has_bj(dealer):
                continue
            else:
                start += 1.5
                continue
        if has_bj(dealer):
            start -= 1
            continue
        x = []
        go_player(player, dealer, deck, x, [2])
        dealer_sum = go_dealer(dealer, deck)

        for hand in x:
            r = compare_player_dealer(hand, dealer_sum, True)
            if r == 0:
                start += 1
            elif r == 1:
                start -= 1
    return start/sims

def get_count(deck):
    """
    gets what the true count would be given remaining cards
    """
    
    c = 0
    for i in deck:
        if i == 10 or i == 1:
            c += 1
        elif i >= 2 and i <= 6:
            c -= 1
    return int(c*52/len(deck))

def sim_play_with_count(sims=10000, deck_num=6, pen=26):
    """
    sims: number of hands simulated
    pen: number of cards after cut card
    returns: a list whose positions correspond to positive true counts starting with 0 and whose values are evs
    for example if return value is [-.02, .03, .06], then the EV with a count of 0 is -.02, a count of +1 is .03, etc
    to get count uses a standard hi-lo, where 2-6 are +1, and T and A are -1
    """
    deck = []

    count_wins = [0 for i in range(100)]
    count_totals = count_wins[:]
    
    for i in range(sims):
        if len(deck) < pen:
            deck = get_deck(deck_num)

        c = get_count(deck)
        
        if c >= 0:
            count_totals[c] += 1
        
        player = [deck.pop(0), deck.pop(0)]
        dealer = [deck.pop(0), deck.pop(0)]
        
        if c >= 3:
            if dealer[0] == 1:
                if dealer[1] == 10:
                    count_wins[c] += 1
                else:
                    count_wins[c] -= .5

        if has_bj(player):
            if has_bj(dealer):
                continue
            else:
                if c >= 0:
                    count_wins[c] += 1.5
                continue
        if has_bj(dealer):
            if c >= 0:
                count_wins[c] -= 1
            continue
        x = []
        go_player(player, dealer, deck, x, [2])
        dealer_sum = go_dealer(dealer, deck)

        for hand in x:
            r = compare_player_dealer(hand, dealer_sum, True)
            if r == 0:
                if c >= 0:
                    count_wins[c] += 1
            elif r == 1:
                if c >= 0:
                    count_wins[c] -= 1

    z = []
    
    for i,j in zip(count_wins, count_totals):
        if j:
            z.append(i/j)
        else:
            z.append('na')
            
    return z[:30]
