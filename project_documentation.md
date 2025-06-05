Scope:
1. Number of players: 8
2. Roles: 
    a. Mafia -- 2 players
    b. Townsflok -- 6 players
3. Game Type: Single Player

Game Flow:
1. Setup - Roles Assigned
2. Night:
    a. Current game state announced
    b. Mafia votes to eliminate 1 townsfolk.
3. Day:
    a. Mafia's decision announced.
    b. Townsfolk & Mafira vote to eliminate 1 player.

Cycle continues until all mafia or townsfolk are eliminated.

4. Winning team announced

Player commands:
1. vote [player_name]
2. kill [player_name]

Implementation Plan:
1. Setup:
    a. Define Player class
        1. Name
        2. Role
        3. Alive
    b. Assign roles randomly
        1. 2 Mafia
        2. 6 Townsfolk
    c. Initilize Game State Variables
        1. Phase
        2. Alive Players
        3. Win Condition
    