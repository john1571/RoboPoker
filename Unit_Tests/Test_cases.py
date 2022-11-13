def test_round_cases():
    # TEST 1 ***********************************************************
    player_dict_1 = {
        'Abe': {'cards': ['2h', '2c'], 'chips': 1000},
        'Ben': {'cards': ['2h', '2c'], 'chips': 1000},
        'Cob': {'cards': ['2h', '2c'], 'chips': 1000},
        'Dan': {'cards': ['2h', '2c'], 'chips': 1000}
    }
    betting_1 = {
        0: [('Abe', 5), ('Ben', 10), ('Cob', 20), ('Dan', 40)],
        1: [('Abe', None), ('Ben', 30), ('Cob', 20), ('Dan', 0)],
        2: [('Abe', None), ('Ben', 60), ('Cob', None), ('Dan', 60)],
    }
    ending_values_1 = [
        ('Abe', 995), ('Ben', 1022), ('Cob', 960), ('Dan', 1023)
    ]
    # TEST 2 ***********************************************************
    player_dict_2 = {
        'Abe': {'cards': ['2h', '2c'], 'chips': 100},
        'Ben': {'cards': ['Ah', 'Ac'], 'chips': 10},
        'Cob': {'cards': ['3h', '3c'], 'chips': 10},
        'Dan': {'cards': ['4h', '4c'], 'chips': 20}
    }
    betting_2 = {
        0: [('Abe', 5), ('Ben', 10), ('Cob', 10), ('Dan', 10)],
        1: [('Abe', 25), ('Ben', None), ('Cob', None), ('Dan', 10)],
    }
    ending_values_2 = [
        ('Abe', 80), ('Ben', 40), ('Cob', 0), ('Dan', 20)
    ]
    # TEST 3 ***********************************************************
    player_dict_3 = {
        'Abe': {'cards': ['Ad', 'As'], 'chips': 20},
        'Ben': {'cards': ['Ah', 'Ac'], 'chips': 10},
        'Cob': {'cards': ['3h', '3c'], 'chips': 10},
        'Dan': {'cards': ['4h', '4c'], 'chips': 20}
    }
    betting_3 = {
        0: [('Abe', 5), ('Ben', 10), ('Cob', 10), ('Dan', 10)],
        1: [('Abe', 25), ('Ben', None), ('Cob', None), ('Dan', 10)],
    }
    ending_values_3 = [
        ('Abe', 40), ('Ben', 20), ('Cob', 0), ('Dan', 0)
    ]
    return [
        (player_dict_1, betting_1, ending_values_1),
        (player_dict_2, betting_2, ending_values_2),
        #(player_dict_3, betting_3, ending_values_3),

    ]