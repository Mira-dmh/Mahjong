# Mahjong

A Python program that simulates Mahjong tile drawing and calculates the minimum number of tile swaps needed to achieve a winning hand.

## Overview

This program implements a Mahjong game analyzer that:
- Generates a complete set of 136 Mahjong tiles
- Randomly draws 14 tiles for a player
- Calculates the minimum number of tile swaps needed to reach a winning hand
- Provides detailed analysis of tile combinations and winning strategies

## Features

✅ **Complete Tile Generation** - Correctly generates 136 mahjong tiles  
✅ **Random Hand Drawing** - Randomly draws 14 tiles from the deck  
✅ **Minimum Swap Calculation** - Calculates minimum tile swaps needed to win  
✅ **English Documentation** - English comments and variable names  
✅ **Error Handling** - Complete error handling and validation  
✅ **Clear Output** - Detailed output messages and analysis  

## Tile Notation System

The program uses a simplified numerical notation for easier coding:

- **Wan (Characters)**: 1-9
- **Tiao (Bamboo)**: 11-19  
- **Tong (Circles)**: 21-29
- **Wind/Dragon Tiles**: 31-37
  - East/South/West/North: 31-34
  - Red/Green/White Dragons: 35-37

## Game Rules

### Winning Condition
A winning hand must contain exactly 14 tiles arranged as:
- **One pair** (two identical tiles)
- **Four sets** of either:
  - **Triplets** (three identical tiles)
  - **Sequences** (three consecutive tiles of the same suit, e.g., 3-4-5 wan)

### Gameplay
- Each turn, a player can replace one tile with any desired tile
- The program calculates the minimum number of such swaps needed to achieve a winning hand

## How to Use

1. **Run the program**:
   ```bash
   python mahjong.py
   ```

2. **The program will automatically**:
   - Generate a complete mahjong deck (136 tiles)
   - Draw a random hand of 14 tiles
   - Analyze the hand for existing combinations
   - Calculate minimum swaps needed
   - Display detailed results

## Example Output

```
Player hand: [1, 2, 3, 11, 12, 13, 21, 22, 23, 31, 31, 32, 33, 34]
[1, 2, 3, 11, 12, 13, 21, 22, 23, 31, 31, 32, 33, 34]
Extracted existing sequences/triplets/pairs: [[1, 2, 3], [11, 12, 13], [21, 22, 23], [31, 31]]
Supplement 32, complete sequence: [[1, 2, 3], [11, 12, 13], [21, 22, 23], [31, 31], [32, 33, 34]]
Minimum swaps needed: 1
```

## Algorithm Overview

The program uses a systematic approach:

1. **Categorization**: Sorts tiles by suit (Wan, Tiao, Tong, Others)
2. **Pattern Recognition**: Identifies existing triplets, sequences, and pairs
3. **Optimization**: Finds the most efficient way to complete missing combinations
4. **Calculation**: Determines minimum swaps needed for a winning hand

### Special Cases Handled
- Multiple possible pair combinations
- Incomplete sequences (e.g., 1-2 or 2-3 patterns)
- Honor tiles (winds/dragons) that only form pairs or triplets
- Edge cases with scattered single tiles

## File Structure

```
Mahjong/
├── mahjong.py          # Main program file
└── README.md           # This documentation
```

## Technical Details

- **Language**: Python 3
- **Dependencies**: Standard library only (random, collections)
- **Tile Representation**: Integer-based encoding for efficient processing
- **Algorithm Complexity**: Optimized for typical Mahjong hand analysis

## Contributing

Feel free to fork this repository and submit pull requests for improvements or bug fixes.

## License

This project is open source and available under standard terms.