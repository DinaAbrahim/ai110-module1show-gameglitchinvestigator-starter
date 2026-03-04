from logic_utils import check_guess, update_score


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


# --- update_score tests ---

def test_update_score_win_early_attempt():
    # attempt 1: points = 100 - 10*1 = 90
    assert update_score(0, "Win", 1) == 90

def test_update_score_win_mid_attempt():
    # attempt 5: points = 100 - 10*5 = 50
    assert update_score(100, "Win", 5) == 150

def test_update_score_win_minimum_points():
    # attempt 10: 100 - 100 = 0, but floor is 10
    assert update_score(0, "Win", 10) == 10

def test_update_score_win_floor_enforced():
    # attempt 15: 100 - 150 = -50, still floor of 10
    assert update_score(0, "Win", 15) == 10

def test_update_score_too_high():
    assert update_score(100, "Too High", 3) == 95

def test_update_score_too_low():
    assert update_score(100, "Too Low", 3) == 95

def test_update_score_unknown_outcome():
    # Unrecognized outcome should leave score unchanged
    assert update_score(100, "Unknown", 1) == 100