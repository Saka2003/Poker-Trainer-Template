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
    ('Cutoff', 'Big Blind', 'AKo'): '3b',
    ('Cutoff', 'Big Blind', 'T9s'): 'call',
    ('Cutoff', 'Big Blind', 'JTs'): 'call',
    ('Early Position', 'Middle Position', 'AQs'): 'call',
    ('Early Position', 'Middle Position', 'QQ'): '3b'
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
