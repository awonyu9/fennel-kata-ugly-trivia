import pytest
import trivia
from output_expected import output

@pytest.fixture
def game():
    game = trivia.Game()
    yield game

def test_trivia(capsys):
    trivia.main()

    capture = capsys.readouterr()

    assert capture.out == output

def test_if_playable(game):
    assert game.is_playable() == False
    game.add('Chet')
    assert game.is_playable() == False
    game.add('Pat')
    assert game.is_playable() == True
    game.add('Sue')
    assert game.is_playable() == True

def test_create_question(game):
    assert game.create_question('Science', 0) == 'Science Question 0'
    assert game.create_question('Pop', 1) == 'Pop Question 1'
    assert game.create_question('Rock', 2) == 'Rock Question 2'
    assert game.create_question('Sports', 3) == 'Sports Question 3'