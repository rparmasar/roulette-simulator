from lib import bet, wheel_spoke

def testInsideBetResolveSuccess():
    params = {
        'numbers': [12]
    }
    test_bet = bet.Bet('single_number', 100, params)
    test_spin_result = wheel_spoke.Spoke(12, 'red')

    wager_result = test_bet.resolve(test_spin_result)

    assert(wager_result == 3500)

def testInsideBetResolveFail():
    params = {
        'numbers': [12]
    }
    test_bet = bet.Bet('single_number', 100, params)
    test_spin_result = wheel_spoke.Spoke(24, 'red')

    wager_result = test_bet.resolve(test_spin_result)

    assert(wager_result == -100)

def testOutsideParityBetResolveSuccess():
    params = {
        'parity': 'even'
    }
    test_bet = bet.Bet('number_parity', 100, params)
    test_spin_result = wheel_spoke.Spoke(12, 'red')

    wager_result = test_bet.resolve(test_spin_result)

    assert(wager_result == 100)

def testOutsideParityBetResolveFail():
    params = {
        'parity': 'even'
    }
    test_bet = bet.Bet('number_parity', 100, params)
    test_spin_result = wheel_spoke.Spoke(25, 'red')

    wager_result = test_bet.resolve(test_spin_result)

    assert(wager_result == -100)

def testOutsideColourBetResolveSuccess():
    params = {
        'colour': 'red'
    }
    test_bet = bet.Bet('single_colour', 100, params)
    test_spin_result = wheel_spoke.Spoke(12, 'red')

    wager_result = test_bet.resolve(test_spin_result)

    assert(wager_result == 100)

def testOutsideColourBetResolveFail():
    params = {
        'colour': 'red'
    }
    test_bet = bet.Bet('single_colour', 100, params)
    test_spin_result = wheel_spoke.Spoke(25, 'black')

    wager_result = test_bet.resolve(test_spin_result)

    assert(wager_result == -100)

def testOutsideGroupBetResolveSuccess():
    test_bet = bet.Bet('lower_third', 100)
    test_spin_result = wheel_spoke.Spoke(12, 'red')

    wager_result = test_bet.resolve(test_spin_result)

    assert(wager_result == 200)

def testOutsideGroupBetResolveFail():
    test_bet = bet.Bet('lower_third', 100)
    test_spin_result = wheel_spoke.Spoke(25, 'black')

    wager_result = test_bet.resolve(test_spin_result)

    assert(wager_result == -100)