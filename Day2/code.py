def possible_games(cube_count, games):
    red_count, green_count, blue_count = cube_count
    for subset in games:
        subset_count = {'red': 0, 'green': 0, 'blue': 0}
        