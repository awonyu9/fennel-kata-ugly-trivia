import pytest
import trivia
from output_expected import output

def test_trivia(capsys):
    trivia.main()

    capture = capsys.readouterr()

    assert capture.out == output

def test_if_playable():
    game = trivia.Game()
    assert game.is_playable() == False
    game.add('Chet')
    assert game.is_playable() == False
    game.add('Pat')
    assert game.is_playable() == True
    game.add('Sue')
    assert game.is_playable() == True