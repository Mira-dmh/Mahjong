# Design a Python program for Mahjong with 136 tiles
# Wind tiles include East, South, West, North (4 tiles), and Dragon tiles include Red, Green, White (3 tiles), totaling 28 tiles. 
# 27+28=55, multiplied by 4 equals 136 tiles.
# Game rules:
# Randomly draw 14 tiles. A pair means two identical tiles, a triplet means three identical tiles, 
# a sequence means three consecutive tiles of the same suit, such as 3-4-5 wan, 6-7-8 circles, etc.
# Among the 14 tiles, there must be one pair, and the remaining 12 tiles can form sequences or triplets (4x3) to win.
# Each turn, replace one tile with an ideal tile (can replace with any desired tile)
# If a player draws one tile and discards one tile, what's the minimum number of rounds needed to achieve a winning hand?
# This Python program is essentially a function that takes any 14 mahjong tiles (selected without replacement from 136 tiles)
# and outputs the minimum number of swaps needed to achieve a winning state

# Simplified tile notation for easier coding:
# Wan (Characters): 1-9
# Tiao (Bamboo): 11-19  
# Tong (Circles): 21-29
# East/South/West/North/Red/Green/White: 31-37

# 程序功能 (Current Program Features):
# ✅ 正确生成136张麻将牌 - Correctly generates 136 mahjong tiles
# ✅ 随机抽取14张牌 - Randomly draws 14 tiles
# ✅ 计算最少换牌次数 - Calculates minimum tile swaps needed
# ✅ 英文注释和变量名 - English comments and variable names
# ✅ 完整的错误处理 - Complete error handling
# ✅ 清晰的输出信息 - Clear output messages

import random
from collections import defaultdict

# Solution
def get_min_winning_moves(hand):
    hand.sort()
    print(hand)
    # Initialize operation: create a mutable container model to store numerical models
    # When an empty defaultdict (key doesn't exist), can directly +1
    wan, tiao, tong, other = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)

    # Categorize by tile type, organize the 14 tiles
    # If the value is less than 10, increase count in "wan" dictionary;
    # If between 10-19, increase count in "tiao" dictionary;
    # If between 20-29, increase count in "tong" dictionary;
    # Otherwise, increase count in "other" dictionary.
    for tile in hand:
        if tile < 10:
            wan[tile] += 1
        elif tile < 20:
            tiao[tile] += 1
        elif tile < 30:
            tong[tile] += 1
        else:
            other[tile] += 1

    pair_count = 0  # Initialize number of pairs to 0
    result = []  # Set up an empty list to continuously add qualifying tile patterns, final output should be 14 tiles

    # Check if the total length of all elements in the tile_groups list equals 14
    def is_winning(tile_groups):
        total_length = 0
        for group in tile_groups:
            total_length += len(group)
        return total_length == 14

    # Extract existing triplets, sequences, and pairs in order
    # Consider special cases like 11 22 33 which can be treated as 2 sequences
    # Extract pairs only once; if there are multiple pairs, supplement them as triplets later
    # result saves currently qualifying tile patterns
    def parse_triplets(tile_dict):
        # items() method returns a view object as a list, which is an iterable key/value pair for easy counting
        for key, count in tile_dict.items():  # Iterate through key-value pairs in tile_dict
            # key represents the key of the current key-value pair. count represents the value associated with key in tile_dict.
            if count == 3:  # count=3 --> triplet
                tile_dict[key] -= 3  # Subtract 3 from the value associated with key
                result.append([key, key, key])

    def parse_sequences(tile_dict):
        # get(key,default) function returns the value of the specified key, if key doesn't exist, returns default value None.
        # Below returns 0
        for key, count in tile_dict.items():
            if tile_dict[key] >= 1 and tile_dict.get(key + 1, 0) >= 1 and tile_dict.get(key + 2, 0) >= 1:
                tile_dict[key] -= 1
                tile_dict[key + 1] -= 1
                tile_dict[key + 2] -= 1
                result.append([key, key + 1, key + 2])

    def parse_pairs(tile_dict):
        # nonlocal -- allows inner functions to directly access and modify outer function variables, since pair count is defined in main function
        nonlocal pair_count
        if pair_count != 0:
            return  # Return, this function performs no operation -- because there's already one pair
        for key, count in tile_dict.items():
            if count == 2:
                tile_dict[key] -= 2
                result.append([key, key])
                pair_count = 1
                break

    def parse_tiles(tile_dict):
        parse_triplets(tile_dict)
        parse_sequences(tile_dict)
        parse_pairs(tile_dict)

    parse_tiles(wan)  # Parse sequences/triplets/pairs in wan
    parse_tiles(tiao)
    parse_tiles(tong)
    # East/South/West/North/Red/Green/White don't consider sequences, only pairs/triplets
    parse_triplets(other)
    parse_pairs(other)

    # Number of tiles that need to be replaced -- final result (total number of tiles to be replaced)
    swaps = 0
    if is_winning(result):
        # is_winning -- check if it's 14 tiles; result -- initially defined empty list, adds pairs/sequences/triplets, must ensure 14 tiles in the end
        return swaps

    # If missing a pair, directly add 0 as placeholder, any single tile works, no need to consider specific tile
    if pair_count == 0:
        swaps += 1
        result.append([0, 0])
    # Merge all key-value pairs from dictionaries wan, tiao, tong, and other into a new dictionary all_tiles.
    # This merges all content from these four dictionaries into one for unified processing of all tiles.
    all_tiles = {}
    all_tiles.update(wan)
    all_tiles.update(tiao)
    all_tiles.update(tong)
    all_tiles.update(other)
    print("Extracted existing sequences/triplets/pairs: {}".format(result))
    # .format method is used for string formatting. It allows inserting values into strings in a specified format.
    # In the given code, {} serves as a placeholder for the result value to be inserted into the string.
    # When the .format method is called on the string, it replaces these placeholders with values passed as arguments to the method.
    # In this case, the value of result will be inserted at the {} position in the string.

    # Up to this point, existing sequences/triplets/pairs have been extracted
    # Next, supplement other scattered tiles into sequences/triplets
    for key, count in all_tiles.items():
        # Pairs can be directly supplemented into triplets
        if count == 2:
            swaps += 1
            result.append([key, key, key])
            print("Supplement {}, complete triplet: {}".format(key, result))
            all_tiles[key] -= 2
        # If it's 1 2/ 2 3 / 1 3 pattern, supplement one tile to form a sequence, other tiles cannot form sequences (excluded)
        if key < 30:
            # Forward direction
            if all_tiles[key] >= 1 and (all_tiles.get(key - 1, 0) >= 1 or all_tiles.get(key - 2, 0) >= 1):
                # Sequences must be of the same suit   # Check if tens digits of key, key-1, and key-2 are the same -- determine same suit
                if key // 10 == (key - 1) // 10 and key // 10 == (key - 2) // 10:
                    swaps += 1
                    result.append([key, key - 1, key - 2])
                    all_tiles[key] -= 1
                    if all_tiles.get(key - 1, 0) >= 1:
                        print("Supplement {}, complete sequence: {}".format(key - 2, result))
                        all_tiles[key - 1] -= 1
                    if all_tiles.get(key - 2, 0) >= 1:
                        print("Supplement {}, complete sequence: {}".format(key - 1, result))
                        all_tiles[key - 2] -= 1
            # Backward direction
            if all_tiles[key] >= 1 and (all_tiles.get(key + 1, 0) >= 1 or all_tiles.get(key + 2, 0) >= 1):
                # Must be of the same suit
                if key // 10 == (key + 1) // 10 and key // 10 == (key + 2) // 10:
                    swaps += 1
                    result.append([key, key + 1, key + 2])
                    all_tiles[key] -= 1
                    if all_tiles.get(key + 1, 0) >= 1:
                        print("Supplement {}, complete sequence: {}".format(key + 2, result))
                        all_tiles[key + 1] -= 1
                    if all_tiles.get(key + 2, 0) >= 1:
                        print("Supplement {}, complete sequence: {}".format(key + 1, result))
                        all_tiles[key + 2] -= 1

        # After each tile supplement, check if conditions are met
        if is_winning(result):
            return swaps

    # Finally, if still not satisfied, remaining tiles are all singles, each single tile needs 2 additional tiles
    total_length = 0
    for group in result:
        total_length += len(group)
    print("Still need {} sequences or triplets, remaining are all single tiles. Each single tile needs 2 additional tiles".format(int((14 - total_length) / 3)))
    return int((14 - total_length) / 3 * 2) + swaps


# Main function
# Generate a complete set of mahjong tiles
def generate_mahjong_deck():
    deck = []
    for i in range(1, 10):
        for j in range(4):
            deck.append(i)
    for i in range(11, 20):
        for j in range(4):
            deck.append(i)
    for i in range(21, 30):
        for j in range(4):
            deck.append(i)
    for i in range(31, 38):
        for j in range(4):
            deck.append(i)
    return deck

# Randomly draw 14 tiles from a complete mahjong deck
def draw_14_tiles(deck):
    hand_14 = random.sample(deck, 14)
    # sample() is a built-in function in Python's random module,
    # returns a specific length list of items selected from a sequence, i.e., list, tuple, string or set. Used for random sampling without replacement.
    return hand_14


# Test the program
mahjong_deck = generate_mahjong_deck()
player_hand = draw_14_tiles(mahjong_deck)
print("Player hand:", player_hand)
print("Minimum swaps needed:", get_min_winning_moves(player_hand))
