def get_semifinal_matchups(teams):
    team_score = {}
    
    for t in teams:
        team, score = t.split(":")
        val = [int(x) for x in score.split("-")]
        final_score = val[0] * 3 + val[1] * 2 + val[2] * 1 + val[3] * 0
        team_score[team] = final_score
    
    sorted_leaderboard = dict(sorted(team_score.items(), key=lambda item: item[1], reverse=True))
    
    team_list = list(sorted_leaderboard.keys())
    
    return f"The semi-final games will be {team_list[0]} vs {team_list[3]} and {team_list[1]} vs {team_list[2]}."
