def player(prev_play, opponent_history=[]):
    
    counter = {'P': 'S', 'R': 'P', 'S': 'R'}

    if not prev_play:
        prev_play = 'R'

    if not hasattr(player, "steps"):
        player.steps = {}

    opponent_history.append(prev_play)
    prediction = 'P'

    
    if len(opponent_history) > 4:
        last_five = "".join(opponent_history[-5:])
        player.steps[last_five] = player.steps.get(last_five, 0) + 1
        
        possible = ["".join([*opponent_history[-4:], v]) for v in ['R', 'P', 'S']]

        under = {k: player.steps[k] for k in possible if k in player.steps}

        if under:
            prediction = max(under, key=under.get)[-1:]

    

    return counter[prediction]
