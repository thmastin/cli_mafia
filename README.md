# CLI Mafia Game

A text-based implementation of the classic Mafia party game where players work to eliminate the opposing team through discussion, voting, and deduction.

## Overview

This command-line Mafia game pits Townsfolk against Mafia members in a battle of wits and deception. One human player joins AI-controlled players in a game of social deduction where the town must identify and eliminate the Mafia before they're outnumbered.

### Key Features

- **Mixed gameplay**: Human player vs AI opponents
- **Dynamic player counts**: Support for variable number of players (minimum 4 recommended)
- **Day/Night cycles**: Strategic voting during the day, secretive kills at night
- **Customizable content**: Flavor text, player names, and messages via CSV files
- **Role-based mechanics**: Different abilities for Mafia and Townsfolk
- **Comprehensive testing**: Full test suite included

## Installation

### Requirements
- Python 3.6 or higher
- No external dependencies required

### Setup
1. Clone or download the repository
2. Ensure all CSV data files are present in the `data/` directory
3. Run the game with: `python main.py`

## How to Play

### Game Rules
- **Townsfolk goal**: Eliminate all Mafia members through voting
- **Mafia goal**: Reduce Townsfolk to equal or fewer numbers than Mafia
- **Day phase**: All players discuss and vote to eliminate someone
- **Night phase**: Mafia secretly chooses a Townsfolk to eliminate

### Game Flow
1. Players are assigned roles (you'll be told your role privately)
2. If you're Mafia, you'll see all player roles
3. Day and night phases alternate until one team wins
4. During day discussions, accuse other players of being Mafia
5. Vote to eliminate suspects using "vote [PlayerName]"
6. If you're Mafia, use "kill [PlayerName]" during night phases

### Commands
- **Day voting**: `vote PlayerName`
- **Night killing** (Mafia only): `kill PlayerName`
- **Discussion**: Type any player's name to accuse them
- **Continue**: Press Enter when prompted

## Game Features

### Role Distribution
- Mafia players: 1/4 of total players (minimum 1)
- Remaining players: Townsfolk
- Human player gets randomly assigned role

### AI Behavior
- **Town AI**: Votes randomly among all players (except themselves)
- **Mafia AI**: Avoids voting for fellow Mafia members
- **Discussion**: AI players make accusations to create suspicion

### Win Conditions
- **Townsfolk win**: All Mafia eliminated
- **Mafia wins**: Mafia equals or outnumbers Townsfolk

## File Structure

```
cli_mafia/
├── main.py              # Entry point
├── game.py              # Main game loop and logic
├── setup.py             # Game initialization and role assignment
├── voting.py            # Voting mechanics for day and night phases
├── player.py            # Player class and role definitions
├── player_input.py      # Input validation and processing
├── ui.py                # User interface and message display
├── csv_handler.py       # CSV file loading functions
├── tests.py             # Comprehensive test suite
└── data/                # Customizable game content
    ├── player_names.csv
    ├── greeting_messages.csv
    ├── vote_messages.csv
    ├── discussion_messages.csv
    ├── mafia_kill_messages.csv
    ├── town_kill_messages.csv
    ├── town_names.csv
    └── flavor_text.csv
```

## Customization

### Adding Player Names
Edit `data/player_names.csv` to customize AI player names:
```csv
Name
Alice
Bob
Charlie
```

### Customizing Messages
All game messages can be modified by editing the corresponding CSV files:

- **greeting_messages.csv**: Welcome messages
- **vote_messages.csv**: Voting announcement templates
- **discussion_messages.csv**: Accusation messages
- **mafia_kill_messages.csv**: Night kill descriptions
- **town_kill_messages.csv**: Day elimination messages
- **town_names.csv**: Setting names for flavor text
- **flavor_text.csv**: Opening game descriptions

### Message Format
Messages support string formatting. Use `{variable_name}` for dynamic content:
```csv
ID,Message
1,"The townspeople of {town_name} gather as darkness falls..."
2,"{voter_name} points accusingly at {vote_name}!"
```

## Development

### Running Tests
Execute the full test suite:
```bash
python tests.py
```

The test suite covers:
- Game setup and role assignment
- Voting mechanics
- Win condition checking
- Input validation
- CSV file handling
- Integration testing

### Code Organization
- **Modular design**: Separate concerns across multiple files
- **Role-based logic**: Clear separation between Mafia and Town behavior
- **UI abstraction**: Game logic separated from display code
- **Data-driven content**: Easy customization through CSV files

### Extending the Game
- Add new roles by extending the `Role` enum
- Implement special abilities in the voting modules
- Create new message types by adding CSV handlers
- Modify AI behavior in the voting functions

## Troubleshooting

### Common Issues

**"FileNotFoundError" when starting**
- Ensure all CSV files exist in the `data/` directory
- Check that CSV files have proper headers

**"Invalid input" messages**
- Use exact format: `vote PlayerName` or `kill PlayerName`
- Player names are case-insensitive
- Ensure the player is still alive

**Game doesn't end**
- Win conditions are checked after each phase
- Verify role distribution is correct (check test output)

**AI players have generic names**
- Add more names to `player_names.csv`
- Ensure CSV file is properly formatted

### Error Messages
- **"You must enter a player's name that is a townsfolk and is still alive"**: Mafia cannot target other Mafia
- **"You must type in a player name that is still alive"**: Target player has been eliminated
- **"Invalid input, you must start with the command 'vote'"**: Use proper command format

## Contributing

Feel free to contribute by:
- Adding new game modes or roles
- Improving AI strategy
- Enhancing the user interface
- Adding more customizable content
- Expanding test coverage

## License

This project is open source. Feel free to modify and distribute as needed.