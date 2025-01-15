import pytest
import trivia

def print_hello():
    print("Hello")

def test_game(capsys):
    print_hello()

    captured = capsys.readouterr()
    
    # Tester le contenu de stdout
    assert captured.out == "Hello\n"

def test_trivia(capsys):
    trivia.main()

    capture = capsys.readouterr()

    assert capture.out == """Chet was added
They are player number 1
Pat was added
They are player number 2
Sue was added
They are player number 3
Chet is the current player
They have rolled a 0
Chet's new location is 0
The category is Pop
Pop Question 0
Answer was corrent!!!!
Chet now has 1 Gold Coins.
Pat is the current player
They have rolled a 1
Pat's new location is 1
The category is Science
Science Question 0
Answer was corrent!!!!
Pat now has 1 Gold Coins.
Sue is the current player
They have rolled a 2
Sue's new location is 2
The category is Sports
Sports Question 0
Answer was corrent!!!!
Sue now has 1 Gold Coins.
Chet is the current player
They have rolled a 3
Chet's new location is 3
The category is Rock
Rock Question 0
Answer was corrent!!!!
Chet now has 2 Gold Coins.
Pat is the current player
They have rolled a 4
Pat's new location is 5
The category is Science
Science Question 1
Answer was corrent!!!!
Pat now has 2 Gold Coins.
Sue is the current player
They have rolled a 5
Sue's new location is 7
The category is Rock
Rock Question 1
Answer was corrent!!!!
Sue now has 2 Gold Coins.
Chet is the current player
They have rolled a 6
Chet's new location is 9
The category is Science
Science Question 2
Answer was corrent!!!!
Chet now has 3 Gold Coins.
Pat is the current player
They have rolled a 7
Pat's new location is 0
The category is Pop
Pop Question 1
Question was incorrectly answered
Pat was sent to the penalty box
Sue is the current player
They have rolled a 8
Sue's new location is 3
The category is Rock
Rock Question 2
Answer was corrent!!!!
Sue now has 3 Gold Coins.
Chet is the current player
They have rolled a 9
Chet's new location is 6
The category is Sports
Sports Question 1
Answer was corrent!!!!
Chet now has 4 Gold Coins.
Pat is the current player
They have rolled a 10
Pat is not getting out of the penalty box
Sue is the current player
They have rolled a 11
Sue's new location is 2
The category is Sports
Sports Question 2
Answer was corrent!!!!
Sue now has 4 Gold Coins.
Chet is the current player
They have rolled a 12
Chet's new location is 6
The category is Sports
Sports Question 3
Answer was corrent!!!!
Chet now has 5 Gold Coins.
Pat is the current player
They have rolled a 13
Pat is getting out of the penalty box
Pat's new location is 1
The category is Science
Science Question 3
Answer was correct!!!!
Pat now has 3 Gold Coins.
Sue is the current player
They have rolled a 14
Sue's new location is 4
The category is Pop
Pop Question 2
Answer was corrent!!!!
Sue now has 5 Gold Coins.
Chet is the current player
They have rolled a 15
Chet's new location is 9
The category is Science
Science Question 4
Answer was corrent!!!!
Chet now has 6 Gold Coins.\n"""