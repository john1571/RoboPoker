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
        1: [('Abe', None), ('Ben', 30), ('Cob', 20), ('Dan', 0), (None, None)],
        2: [('Abe', None), ('Ben', 60), ('Cob', None), ('Dan', 60)],
    }
    ending_values_1 = [
        ('Abe', 995), ('Ben', 1022), ('Cob', 960), ('Dan', 1022)
    ]
    # TEST 2 ***********************************************************

    player_dict_2 = {
        'Abe': {'cards': ['2h', '2c'], 'chips': 100},
        'Ben': {'cards': ['Ah', 'Ac'], 'chips': 10},  # Ben wins hands down, but can only win 10 from each opponent
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
        1: [('Abe', 15), ('Ben', None), ('Cob', None), ('Dan', 10)],
    }
    ending_values_3 = [
        ('Abe', 40), ('Ben', 20), ('Cob', 0), ('Dan', 0)
    ]
    # TEST 4 **********************************************************
    player_dict_4 = {
        'Abe': {'cards': ['Ad', 'As'], 'chips': 200},
        'Ben': {'cards': ['Kh', 'Ac'], 'chips': 100},
        'Cob': {'cards': ['3h', '3c'], 'chips': 100},
        'Dan': {'cards': ['4h', '4c'], 'chips': 200}
    }
    betting_4 = {
        0: [('Abe', 5), ('Ben', 10), ('Cob', 10), ('Dan', 10)],
        1: [('Abe', 25), ('Ben', 20), ('Cob', None), ('Dan', 20), (None, None)],
        2: [('Abe', 25), ('Ben', 25), ('Cob', None), ('Dan', 25), (None, None)],
        3: [('Abe', 20), ('Ben', 20), ('Cob', None), ('Dan', None)],
    }
    # Pot size = 75 + 75 + 10 + 55 = 215
    # Abe wins 200 - 75 + 215 = 125 + 215 = 340
    ending_values_4 = [
        ('Abe', 340), ('Ben', 25), ('Cob', 90), ('Dan', 145)
    ]
    # TEST BUG 1 **********************************************************
    table = ['3d', '7c', '8h', 'Kd', 'Js']
    player_dict_bug_1 = {
        'Abe': {'cards': ['5c', 'Ks'] + table, 'chips': 3235},
        'Ben': {'cards': ['5s', '9d'] + table, 'chips': 975},
        'Cob': {'cards': ['4d', '7s'] + table, 'chips': 60},
        'Dan': {'cards': ['Ah', '7d'] + table, 'chips': 940},
        'Eli': {'cards': ['8c', '6h'] + table, 'chips': 105},
        'Gad': {'cards': ['Kh', 'Td'] + table, 'chips': 1675},
    }
    betting_bug_1 = {
        0: [('Abe', 5), ('Ben', 10), ('Cob', 20), ('Dan', 40), ('Eli', 40), ('Gad', 40)],
        1: [('Abe', None), ('Ben', None), ('Cob', 40), ('Dan', 80), ('Eli', 65), ('Gad', None), (None, None)], #Cob is all in, ELI is all in
        2: [('Abe', None), ('Ben', None), ('Cob', 0), ('Dan', None), ('Eli', 0), ('Gad', None)], #Dan should not be able to fold
    }
    # Pot size = 340
    # Eli wins 5 + 10 + 60 + 105 + 105 + 40
    #          = 15 + 165 + 145
    #          = 180 + 145 = 325
    # Dan wins remaining 15
    ending_values_bug_1 = [
        ('Abe', 3230), ('Ben', 965), ('Cob', 0), ('Dan', 835), ('Eli', 325), ('Gad', 1635)
    ]
    # TEST BUG 2 **********************************************************
    table = ['3d', '7c', '8h', 'Kd', 'Js']
    player_dict_bug_2 = {
        'Ben': {'cards': ['2s', 'Jc'] + table, 'chips': 2093},
        'Eli': {'cards': ['Qd', '9c'] + table, 'chips': 2755},
        'Gad': {'cards': ['Kd', '9h'] + table, 'chips': 2150},
    }
    betting_bug_2 = {
        0: [('Ben', 10), ('Eli', 20), ('Gad', 20)],
        1: [('Ben', None), ('Eli', None), (None, None)],
        2: [('Ben', None), ('Eli', None), ('Gad', None)],
    }
    # Pot size = 340
    # Eli wins 5 + 10 + 60 + 105 + 105 + 40
    #          = 15 + 165 + 145
    #          = 180 + 145 = 325
    # Dan wins remaining 15
    ending_values_bug_2 = [
        ('Ben', 2083),  ('Eli', 2735), ('Gad', 2180)
    ]
    # TEST BUG 2 **********************************************************
    table = ['3d', '7c', '8h', 'Kd', 'Js']
    player_dict_bug_3 = {
        'Ben': {'cards': ['2s', 'Jc'] + table, 'chips': 2},
        'Eli': {'cards': ['Qd', '9c'] + table, 'chips': 2},
        'Gad': {'cards': ['Kd', '9h'] + table, 'chips': 2},
    }
    betting_bug_3 = {
        0: [('Ben', 1), ('Eli', 2), ('Gad', None)],
        1: [('Ben', None), ('Eli', None)],
    }

    ending_values_bug_3 = [
        ('Ben', 1),  ('Eli', 3), ('Gad', 2)
    ]


    return [
        (player_dict_1, betting_1, ending_values_1),
        (player_dict_2, betting_2, ending_values_2),
        (player_dict_3, betting_3, ending_values_3),
        (player_dict_4, betting_4, ending_values_4),
        (player_dict_bug_1, betting_bug_1, ending_values_bug_1),
        (player_dict_bug_2, betting_bug_2, ending_values_bug_2),
        (player_dict_bug_3, betting_bug_3, ending_values_bug_3),
    ]