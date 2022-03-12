# 2D-Clash-of-Clans

A game similar to Brick Breaker, but runs on terminal because flash player is dead.

## Installation and running

1. Run the following command to install all the required libraries \
   `pip3 install -r requirements.txt`
2. To run the game, \
   `cd src` \
   `python3 main.py` \
3. Ensure that your terminal is in full screen.

## Controls

- `w` move King up
- `a` move King left
- `s` move King down
- `d` move King right
- `r` use Rage spell
- `h` use Heal spell
- `1` spawn Barbarian at top left corner
- `2` spawn Barbarian at Bottom left corner
- `3` spawn Barbarian at Bottom Right corner
## Features

### Inheritance

`Barbarian` and `King` classes are inherited from the `Character` class. `Hut`, `Cannon` and `TownHall` are inherited from the `Building` class.

### Polymorphism

Functions such as `attack`, `move`, etc are common for multiple objects.

### Encapsulation

Multiple classes and objects are used.

### Abstraction

Many functions such as `printBoard`, `updateGame`, etc are abstracted.
