import random

positions = ['Middle Position', 'Cutoff', 'Button', 'Small Blind', 'Big Blind']
open_positions = ['Early Position', 'Middle Position', 'Cutoff', 'Button', 'Small Blind']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['♠', '♥', '♦', '♣']

rfi_chart = {
    'Middle Position': {'AKo': 'raise', 'AQs': 'raise', 'JTs': 'raise'},
    'Cutoff': {'T9s': 'raise', 'AQo': 'raise'},
    'Button': {'JTo': 'raise'},
    'Small Blind': {'22': 'raise'}
}

response_chart = {
   ('Middle Position', 'Middle Position', '77'): 'call', ('Middle Position', 'Middle Position', '88'): 'call',
    ('Middle Position', 'Middle Position', '99'): 'call', ('Middle Position', 'Middle Position', 'TT'): 'call',
    ('Middle Position', 'Middle Position', 'JJ'): 'call', ('Middle Position', 'Middle Position', '66'): 'call',
    ('Middle Position', 'Middle Position', '55'): 'call', ('Middle Position', 'Middle Position', '87s'): 'call',
    ('Middle Position', 'Middle Position', 'T9s'): 'call', ('Middle Position', 'Middle Position', 'JTs'): 'call',
    ('Middle Position', 'Middle Position', 'KQs'): 'call', ('Middle Position', 'Middle Position', 'QJs'): 'call',
    ('Middle Position', 'Middle Position', 'AJs'): 'call', ('Middle Position', 'Middle Position', 'AQs'): 'call',
    ('Middle Position', 'Middle Position', 'KJs'): 'call', ('Middle Position', 'Middle Position', 'A2s'): 'call',
    ('Middle Position', 'Middle Position', 'A3s'): 'call', ('Middle Position', 'Middle Position', 'A4s'): 'call',
    ('Middle Position', 'Middle Position', 'ATs'): '3b', ('Middle Position', 'Middle Position', 'A5s'): '3b',
    ('Middle Position', 'Middle Position', 'QQ'): '3b', ('Middle Position', 'Middle Position', 'KK'): '3b',
    ('Middle Position', 'Middle Position', 'AA'): '3b', ('Middle Position', 'Middle Position', 'AKo'): '3b',
    ('Middle Position', 'Middle Position', '76s'): '3b', ('Middle Position', 'Middle Position', 'AQo'): '3b',
    ('Middle Position', 'Middle Position', 'KTs'): 'call', ('Middle Position', 'Middle Position', 'QTs'): 'call',

    # CO vs MP (same as BTN vs UTG)
    ('Middle Position', 'Button', '66'): 'call', ('Middle Position', 'Button', '55'): 'call',
    ('Middle Position', 'Button', '76s'): '3b', ('Middle Position', 'Button', 'AQs'): '3b',
    ('Middle Position', 'Button', 'KTs'): 'call', ('Middle Position', 'Button', 'QTs'): 'call',
    ('Middle Position', 'Button', 'A4s'): 'call', ('Middle Position', 'Button', 'A3s'): 'call',
    ('Middle Position', 'Button', 'A2s'): 'call',

    # SB vs MP (same as facing UTG)
    ('Middle Position', 'Small Blind', '77'): 'call', ('Middle Position', 'Small Blind', '88'): 'call',
    ('Middle Position', 'Small Blind', '99'): 'call', ('Middle Position', 'Small Blind', 'TT'): 'call',
    ('Middle Position', 'Small Blind', 'JJ'): 'call', ('Middle Position', 'Small Blind', 'T9s'): 'call',
    ('Middle Position', 'Small Blind', 'JTs'): 'call', ('Middle Position', 'Small Blind', 'KQs'): 'call',
    ('Middle Position', 'Small Blind', 'QJs'): 'call', ('Middle Position', 'Small Blind', 'AJs'): 'call',
    ('Middle Position', 'Small Blind', 'AQs'): 'call', ('Middle Position', 'Small Blind', 'KJs'): 'call',
    ('Middle Position', 'Small Blind', 'ATs'): '3b', ('Middle Position', 'Small Blind', 'A5s'): '3b',
    ('Middle Position', 'Small Blind', 'QQ'): '3b', ('Middle Position', 'Small Blind', 'KK'): '3b',
    ('Middle Position', 'Small Blind', 'AA'): '3b', ('Middle Position', 'Small Blind', 'AKo'): '3b',
    ('Middle Position', 'Small Blind', '76s'): '3b', ('Middle Position', 'Small Blind', 'AQo'): '3b',
    ('Middle Position', 'Small Blind', 'KTs'): 'call', ('Middle Position', 'Small Blind', 'QTs'): 'call',

    # BB vs CO/BTN/SB — always call Axs not in 3b
    ('Middle Position', 'Big Blind', 'A2s'): 'call', ('Middle Position', 'Big Blind', 'A3s'): 'call',
    ('Middle Position', 'Big Blind', 'A4s'): 'call', ('Middle Position', 'Big Blind', 'A5s'): 'call',
    ('Middle Position', 'Big Blind', 'A6s'): 'call', ('Middle Position', 'Big Blind', 'A7s'): 'call',
    ('Middle Position', 'Big Blind', 'A8s'): 'call', ('Middle Position', 'Big Blind', 'A9s'): 'call',

    # T9s and JTs from BB facing any RFI
    ('Middle Position', 'Big Blind', 'T9s'): 'call', ('Middle Position', 'Big Blind', 'JTs'): 'call',
    ('Middle Position', 'Big Blind', 'KTs'): 'call', ('Middle Position', 'Big Blind', 'QTs'): 'call'
}

def format_hand(card1, card2):
    r1, s1 = card1[0], card1[1]
    r2, s2 = card2[0], card2[1]
    suited = s1 == s2
    sorted_ranks = sorted([r1, r2], key=lambda x: ranks.index(x), reverse=True)
    if sorted_ranks[0] == sorted_ranks[1]:
        return sorted_ranks[0] + sorted_ranks[1]
    return ''.join(sorted_ranks) + ('s' if suited else 'o')

def get_hand_scenario(mode='response'):
    deck = [r + s for r in ranks for s in suits]
    random.shuffle(deck)
    hand = [deck.pop(), deck.pop()]
    hero_position = random.choice(positions)
    hero_index = positions.index(hero_position)
    if mode == 'response':
        valid_openers = open_positions[:hero_index] if hero_index > 0 else ['Early Position']
        opener_position = random.choice(valid_openers)
        return {
            'position': hero_position,
            'opener': opener_position,
            'hand': hand
        }
    else:
        return {
            'position': hero_position,
            'hand': hand,
            'opener': None
        }

def evaluate_action(hero_pos, opener_pos, hand, action):
    hand_key = format_hand(*hand)
    if opener_pos:
        key = (opener_pos, hero_pos, hand_key)
        optimal = response_chart.get(key, 'fold')
    else:
        optimal = rfi_chart.get(hero_pos, {}).get(hand_key, 'fold')
    return {
        'correct': action == optimal,
        'optimal': optimal
    }
