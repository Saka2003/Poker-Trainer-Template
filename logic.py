# File: logic/trainer.py
import random

positions = ['Middle Position', 'Cutoff', 'Button', 'Small Blind', 'Big Blind']
open_positions = ['Early Position', 'Middle Position', 'Cutoff', 'Button', 'Small Blind']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['♠', '♥', '♦', '♣']

# Minimal chart — extend as needed
rfi_chart = {
    'Middle Position': {
        '77': 'raise', '88': 'raise', '99': 'raise', 'TT': 'raise', 'JJ': 'raise', 'QQ': 'raise', 'KK': 'raise', 'AA': 'raise',
        'ATs': 'raise', 'AJs': 'raise', 'AQs': 'raise', 'AKs': 'raise',
        'KTs': 'raise', 'KJs': 'raise', 'KQs': 'raise', 'QTs': 'raise', 'QJs': 'raise', 'J9s': 'raise', 'JTs': 'raise',
        'T9s': 'raise', '98s': 'raise', '87s': 'raise', '76s': 'raise', 'A5s': 'raise', 'AQo': 'raise', 'AKo': 'raise'
    },
    'Cutoff': {
        '22': 'raise', '33': 'raise', '44': 'raise', '55': 'raise', '66': 'raise', '77': 'raise', '88': 'raise',
        '99': 'raise', 'TT': 'raise', 'JJ': 'raise', 'QQ': 'raise', 'KK': 'raise', 'AA': 'raise',
        'A2s': 'raise', 'A3s': 'raise', 'A4s': 'raise', 'A5s': 'raise', 'A6s': 'raise', 'A7s': 'raise', 'A8s': 'raise',
        'A9s': 'raise', 'ATs': 'raise', 'AJs': 'raise', 'AQs': 'raise', 'AKs': 'raise',
        'K5s': 'raise', 'K6s': 'raise', 'K7s': 'raise', 'K8s': 'raise', 'K9s': 'raise', 'KTs': 'raise', 'KJs': 'raise', 'KQs': 'raise',
        'Q8s': 'raise', 'Q9s': 'raise', 'QTs': 'raise', 'QJs': 'raise', 'J8s': 'raise', 'J9s': 'raise', 'JTs': 'raise',
        'T8s': 'raise', '97s': 'raise', '98s': 'raise', '86s': 'raise', '75s': 'raise', '65s': 'raise', '54s': 'raise',
        'ATo': 'raise', 'AJo': 'raise', 'AQo': 'raise', 'AKo': 'raise', 'KTo': 'raise', 'QTo': 'raise', 'JTo': 'raise',
        'T9s': 'raise', '87s': 'raise', '76s': 'raise'
    },
    'Button': {
        '22': 'raise', '33': 'raise', '44': 'raise', '55': 'raise', '66': 'raise', '77': 'raise', '88': 'raise',
        '99': 'raise', 'TT': 'raise', 'JJ': 'raise', 'QQ': 'raise', 'KK': 'raise', 'AA': 'raise',
        'A2s': 'raise', 'A3s': 'raise', 'A4s': 'raise', 'A5s': 'raise', 'A6s': 'raise', 'A7s': 'raise', 'A8s': 'raise',
        'A9s': 'raise', 'ATs': 'raise', 'AJs': 'raise', 'AQs': 'raise', 'AKs': 'raise',
        'K2s': 'raise', 'K3s': 'raise', 'K4s': 'raise', 'K5s': 'raise', 'K6s': 'raise', 'K7s': 'raise', 'K8s': 'raise',
        'K9s': 'raise', 'KTs': 'raise', 'KJs': 'raise', 'KQs': 'raise',
        'Q5s': 'raise', 'Q6s': 'raise', 'Q7s': 'raise', 'Q8s': 'raise', 'Q9s': 'raise', 'QTs': 'raise', 'QJs': 'raise',
        'J7s': 'raise', 'J8s': 'raise', 'J9s': 'raise', 'JTs': 'raise',
        'T6s': 'raise', '96s': 'raise', '85s': 'raise', '75s': 'raise', '64s': 'raise', '53s': 'raise', '43s': 'raise',
        'A4o': 'raise', 'A5o': 'raise', 'A6o': 'raise', 'A7o': 'raise', 'A8o': 'raise', 'A9o': 'raise', 'ATo': 'raise', 'AJo': 'raise', 'AQo': 'raise', 'AKo': 'raise',
        'K9o': 'raise', 'KTo': 'raise', 'KJo': 'raise', 'KQo': 'raise', 'Q9o': 'raise', 'QTo': 'raise', 'QJo': 'raise', 'JTo': 'raise',
        'T9s': 'raise', '87s': 'raise', '76s': 'raise'
    },
    'Small Blind': {
        '22': 'raise', '33': 'raise', '44': 'raise', '55': 'raise', '66': 'raise', '77': 'raise', '88': 'raise', '99': 'raise',
        'TT': 'raise', 'JJ': 'raise', 'QQ': 'raise', 'KK': 'raise', 'AA': 'raise',
        'A2s': 'raise', 'A3s': 'raise', 'A4s': 'raise', 'A5s': 'raise', 'A6s': 'raise', 'A7s': 'raise', 'A8s': 'raise', 'A9s': 'raise',
        'ATs': 'raise', 'AJs': 'raise', 'AQs': 'raise', 'AKs': 'raise',
        'K2s': 'raise', 'K3s': 'raise', 'K4s': 'raise', 'K5s': 'raise', 'K6s': 'raise', 'K7s': 'raise', 'K8s': 'raise', 'K9s': 'raise',
        'KTs': 'raise', 'KJs': 'raise', 'KQs': 'raise',
        'Q4s': 'raise', 'Q5s': 'raise', 'Q6s': 'raise', 'Q7s': 'raise', 'Q8s': 'raise', 'Q9s': 'raise', 'QTs': 'raise', 'QJs': 'raise',
        'J6s': 'raise', 'J7s': 'raise', 'J8s': 'raise', 'J9s': 'raise', 'JTs': 'raise',
        'T6s': 'raise', '95s': 'raise', '84s': 'raise', '74s': 'raise', '63s': 'raise', '53s': 'raise', '43s': 'raise',
        'A2o': 'raise', 'A3o': 'raise', 'A4o': 'raise', 'A5o': 'raise', 'A6o': 'raise', 'A7o': 'raise', 'A8o': 'raise',
        'A9o': 'raise', 'ATo': 'raise', 'AJo': 'raise', 'AQo': 'raise', 'AKo': 'raise',
        'K8o': 'raise', 'K9o': 'raise', 'KTo': 'raise', 'KJo': 'raise', 'KQo': 'raise', 'Q8o': 'raise', 'Q9o': 'raise', 'QTo': 'raise', 'QJo': 'raise', 'JTo': 'raise',
        'T9s': 'raise', '87s': 'raise', '76s': 'raise'
    }
},
    'Cutoff': {'T9s': 'raise', 'AQo': 'raise'},
    'Button': {'JTo': 'raise'},
    'Small Blind': {'22': 'raise'}
}

response_chart = {
    # Facing UTG RFI
    ('UTG', 'Middle Position', '77'): 'call', ('UTG', 'Middle Position', '88'): 'call', ('UTG', 'Middle Position', '99'): 'call',
    ('UTG', 'Middle Position', 'TT'): 'call', ('UTG', 'Middle Position', 'JJ'): 'call',
    ('UTG', 'Middle Position', 'T9s'): 'call', ('UTG', 'Middle Position', 'JTs'): 'call',
    ('UTG', 'Middle Position', 'KQs'): 'call', ('UTG', 'Middle Position', 'QJs'): 'call', ('UTG', 'Middle Position', 'AJs'): 'call',
    ('UTG', 'Middle Position', 'AQs'): 'call', ('UTG', 'Middle Position', 'KJs'): 'call',
    ('UTG', 'Middle Position', 'ATs'): '3b', ('UTG', 'Middle Position', 'A5s'): '3b', ('UTG', 'Middle Position', 'QQ'): '3b', ('UTG', 'Middle Position', 'KK'): '3b',
    ('UTG', 'Middle Position', 'AA'): '3b', ('UTG', 'Middle Position', 'AKo'): '3b',

    # Cutoff vs UTG (MP + extras)
    ('UTG', 'Cutoff', '77'): 'call', ('UTG', 'Cutoff', '88'): 'call', ('UTG', 'Cutoff', '99'): 'call',
    ('UTG', 'Cutoff', 'TT'): 'call', ('UTG', 'Cutoff', 'JJ'): 'call', ('UTG', 'Cutoff', '66'): 'call', ('UTG', 'Cutoff', '55'): 'call', ('UTG', 'Cutoff', '87s'): 'call',
    ('UTG', 'Cutoff', 'T9s'): 'call', ('UTG', 'Cutoff', 'JTs'): 'call', ('UTG', 'Cutoff', 'KQs'): 'call', ('UTG', 'Cutoff', 'QJs'): 'call', ('UTG', 'Cutoff', 'AJs'): 'call',
    ('UTG', 'Cutoff', 'AQs'): 'call', ('UTG', 'Cutoff', 'KJs'): 'call', ('UTG', 'Cutoff', 'A2s'): 'call', ('UTG', 'Cutoff', 'A3s'): 'call', ('UTG', 'Cutoff', 'A4s'): 'call',
    ('UTG', 'Cutoff', 'ATs'): '3b', ('UTG', 'Cutoff', 'A5s'): '3b', ('UTG', 'Cutoff', 'QQ'): '3b', ('UTG', 'Cutoff', 'KK'): '3b', ('UTG', 'Cutoff', 'AA'): '3b', ('UTG', 'Cutoff', 'AKo'): '3b',
    ('UTG', 'Cutoff', '76s'): '3b', ('UTG', 'Cutoff', 'AQo'): '3b', ('UTG', 'Cutoff', 'KTs'): 'call', ('UTG', 'Cutoff', 'QTs'): 'call',

    # Button vs UTG (Cutoff + extras)
    ('UTG', 'Button', '22'): 'call', ('UTG', 'Button', '33'): 'call', ('UTG', 'Button', '44'): 'call',
    ('UTG', 'Button', 'A2s'): 'call', ('UTG', 'Button', 'A3s'): 'call', ('UTG', 'Button', 'A4s'): 'call',
    ('UTG', 'Button', '65s'): 'call', ('UTG', 'Button', '54s'): 'call', ('UTG', 'Button', '43s'): 'call',

    # SB vs UTG (same as cutoff)
    ('UTG', 'Small Blind', '22'): 'call', ('UTG', 'Small Blind', '33'): 'call', ('UTG', 'Small Blind', 'A2s'): 'call',

    # BB vs UTG (Button + extras)
    ('UTG', 'Big Blind', '65s'): 'call', ('UTG', 'Big Blind', '54s'): 'call', ('UTG', 'Big Blind', '43s'): 'call',
    ('UTG', 'Big Blind', 'QTs'): 'call',

    # MP = CO/BTN RFI equivalence
    ('Middle Position', 'Cutoff', 'AQs'): '3b', ('Middle Position', 'Cutoff', 'JJ'): '3b',
    ('Middle Position', 'Cutoff', 'KTs'): 'call',

    # Add T9s and JTs to all BB call ranges
    ('Cutoff', 'Big Blind', 'T9s'): 'call', ('Cutoff', 'Big Blind', 'JTs'): 'call', ('Cutoff', 'Big Blind', 'QTs'): 'call', ('Cutoff', 'Big Blind', 'KTs'): 'call',

    # BB vs MP — Axs hands as calls
    ('Middle Position', 'Big Blind', 'A2s'): 'call', ('Middle Position', 'Big Blind', 'A3s'): 'call', ('Middle Position', 'Big Blind', 'A4s'): 'call', ('Middle Position', 'Big Blind', 'A5s'): 'call',
    ('Middle Position', 'Big Blind', 'A6s'): 'call', ('Middle Position', 'Big Blind', 'A7s'): 'call', ('Middle Position', 'Big Blind', 'A8s'): 'call', ('Middle Position', 'Big Blind', 'A9s'): 'call',

    # BB vs SB — A7s = 3b, AQo+ = 3b
    ('Small Blind', 'Big Blind', 'A7s'): '3b', ('Small Blind', 'Big Blind', 'AQo'): '3b', ('Small Blind', 'Big Blind', 'AKo'): '3b',

    # All Axs added to CO/BTN/SB facing any RFI
    ('Middle Position', 'Cutoff', 'A2s'): 'call', ('Middle Position', 'Cutoff', 'A3s'): 'c

def format_hand(card1, card2):
    # Extract rank and suit
    r1, s1 = card1[0], card1[1]
    r2, s2 = card2[0], card2[1]

    # Make sure ranks are uppercase for safety
    r1 = r1.upper()
    r2 = r2.upper()

    # Determine if suited or offsuit
    suited = s1 == s2

    # Sort ranks by strength (high card first)
    sorted_ranks = sorted([r1, r2], key=lambda x: ranks.index(x), reverse=True)

    # If it's a pair (e.g., TT), return like 'TT'
    if sorted_ranks[0] == sorted_ranks[1]:
        return sorted_ranks[0] + sorted_ranks[1]

    # Return formatted like 'AKs' or 'T9o'
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
