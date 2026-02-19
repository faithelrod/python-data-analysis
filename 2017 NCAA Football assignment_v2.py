import marimo

__generated_with = "0.15.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # MIS 501 Football Data Analysis Assignment

    ## Overview
    This project analyzes NCAA football game data from the 2017 season using Python. You will practice data ingestion, manipulation, analysis, and reporting skills.

    ## Key Concepts Used
    * **Basic Python**: syntax, len() function, variables, conditionals, loops
    * **Data structures**: lists, dictionaries, and sets
    * **Data analysis**: polars library for DataFrames and aggregations
    * **Pattern matching**: regex for extracting text patterns
    * **File I/O**: JSON file reading and writing
    * **File system**: pathlib for file access

    ## Dataset Information
    You have been provided JSON files containing football game data from the 2017 season.

    **Important Notes:**
    - Use only JSON files in the 'full' folders (not 'flattened')
    - If the provided data conflicts with real-world statistics, use the provided data
    - 'Season' includes all games provided (regular season + bowl games)
    - You are free to use any and all AI available to you.
    - Do not collaborate with others or use others' individual work on this assignment.

    ## Assignment Objectives
    Answer the questions below and output your results to a JSON file with:
    - **Keys**: Question identifiers (e.g., 'q1', 'q2', 'q3.1')
    - **Values**: Your answers in appropriate data types

    ## Deliverables
    - Submit a JSON file named: `mis511_python_project_[netid].json`
    - Submit your .py file
    """
    )
    return


@app.cell
def _():
    # Example: How to structure your answer file
    example_answer_file = {}
    example_answer_file['q1'] = 'yes'  # String answer
    example_answer_file['q2'] = 42      # Numeric answer
    example_answer_file['q3'] = ['item1', 'item2']  # List answer
    print(example_answer_file)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ---
    ## Setup: Import Required Libraries
    """
    )
    return


@app.cell
def _():
    # Standard library imports
    import pathlib
    import json
    import os
    import re
    import statistics
    return json, os, re, statistics


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Data Loading
    Load all game data from JSON files organized by week.
    """
    )
    return


@app.cell
def _(json, os):
    # Initialize dictionary to store all game data
    game_dict = {}

    # Define all weeks in the season (including bowl games)
    game_weeks = [
        "Bowl", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5",
        "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11",
        "Week 12", "Week 13", "Week 14", "Week 15"
    ]

    # Iterate through each week and load game files
    for week in game_weeks:
        week_path = f'2017 Alabama football JSON/{week}/full'

        for file in os.listdir(week_path):
            # Initialize nested dictionary for this game
            game_dict[file] = {}

            # Read and parse JSON file
            with open(f'{week_path}/{file}', 'r') as path:
                json_bytes = path.read()
                game_data = json.loads(json_bytes)
                game_dict[file].update(game_data)
    return game_dict, game_weeks


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ---
    ## Question 1
    **How many games are in the data set?**
    """
    )
    return


@app.cell
def _(game_dict):
    q1 = len(game_dict)
    return (q1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Question 2
    **What are the top-level keys for each game file?**

    These keys represent the main data categories available for each game.
    """
    )
    return


@app.cell
def _(game_dict):
    q2 = list(game_dict[list(game_dict.keys())[0]].keys())
    return (q2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Data Quality Check

    Real-world data often contains irregularities or errors. Key questions to consider:
    - Are team names consistent across files? (e.g., "Texas A&M" vs "Texas A and M")
    - Are there duplicate games in the dataset?
    - Are all teams in the season represented?

    We'll examine file names and team references to assess data quality.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Question 3
    **Are all teams referenced consistently? (yes/no)**
    """
    )
    return


@app.cell
def _(game_dict):
    all_teams_q3 = set()

    for file_name, game_info in game_dict.items():
        teams_list = game_info.get('teams', [])
        for team_obj in teams_list:
            if 'team' in team_obj and isinstance(team_obj['team'], dict):
                team_name = team_obj['team'].get('displayName', '')
            else:
                team_name = team_obj.get('displayName', '')
            if team_name:
                all_teams_q3.add(team_name)

    # Check for inconsistencies
    team_list_q3 = sorted(list(all_teams_q3))
    inconsistencies_found = []

    for i, team in enumerate(team_list_q3):
        for j in range(i+1, len(team_list_q3)):
            other = team_list_q3[j]
        
            normalized_team = team.lower().replace(' and ', ' & ').replace('_', "'").replace('-', ' ')
            normalized_other = other.lower().replace(' and ', ' & ').replace('_', "'").replace('-', ' ')
        
            if normalized_team == normalized_other:
                inconsistencies_found.append((team, other))

    if len(inconsistencies_found) > 0:
        q3 = 'no'
    else:
        q3 = 'yes'
    return all_teams_q3, q3


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Question 3.1
    **Provide a Python list of all teams in the dataset, sorted alphabetically.**
    """
    )
    return


@app.cell
def _(all_teams_q3):
    teams = sorted(list(all_teams_q3))
    q3_1 = teams
    return q3_1, teams


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Question 4
    **Does the data seem reliable?**

    - **q4**: 'yes' or 'no'
    - **q4.1**: Provide 1-2 sentences with quantifiable reasons from the dataset.
      If you cleaned any data, explain what and why.
    """
    )
    return


@app.cell
def _(game_dict, teams):
    complete_games_q4 = 0
    for gfile, gdata in game_dict.items():
        has_drives = 'drives' in gdata and len(gdata.get('drives', [])) > 0
        has_scoring = 'scoringPlays' in gdata
        has_teams = 'teams' in gdata and len(gdata.get('teams', [])) == 2
    
        if has_drives and has_scoring and has_teams:
            complete_games_q4 += 1

    completeness_rate_q4 = (complete_games_q4 / len(game_dict)) * 100

    q4 = 'yes'
    q4_1 = f"The data appears reliable with {complete_games_q4} out of {len(game_dict)} games ({completeness_rate_q4:.1f}%) containing complete drive, scoring, and team information. All {len(teams)} teams are consistently named throughout the dataset."

    return q4, q4_1


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Question 5
    **How many unique teams are represented in the data?**
    """
    )
    return


@app.cell
def _(teams):
    q5 = len(teams)
    return (q5,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Question 6
    **Alabama Field Goal Analysis**

    Alabama fans often assume their kicker will miss field goals. Does the 2017 season
    data support this perception? Compare Alabama's field goal success rate to other teams.

    - **q6**: 'yes' or 'no' (Does Alabama miss more often than others?)
    - **q6.1**: Provide quantifiable evidence from the dataset
    """
    )
    return


@app.cell
def _(game_dict):
    def get_drives_list(drives_data):
        if isinstance(drives_data, dict):
            return drives_data.get('previous', [])
        return drives_data if isinstance(drives_data, list) else []

    fg_stats_q6 = {}

    for gfile_q6, ginfo_q6 in game_dict.items():
        scoring_plays_q6 = ginfo_q6.get('scoringPlays', [])
    
        # Count successful field goals
        for play_q6 in scoring_plays_q6:
            if play_q6.get('scoringType', {}).get('name') == 'field-goal':
                tname_q6 = play_q6.get('team', {}).get('displayName', '')
                if tname_q6:
                    if tname_q6 not in fg_stats_q6:
                        fg_stats_q6[tname_q6] = {'made': 0, 'missed': 0}
                    fg_stats_q6[tname_q6]['made'] += 1
    
        # Count missed field goals from drives
        drives_list_q6 = get_drives_list(ginfo_q6.get('drives', []))
        teams_data_q6 = ginfo_q6.get('teams', [])
    
        # Create team ID to name mapping
        team_map_q6 = {}
        for tobj_q6 in teams_data_q6:
            tid_q6 = tobj_q6.get('id', '')
            if 'team' in tobj_q6 and isinstance(tobj_q6['team'], dict):
                tn_q6 = tobj_q6['team'].get('displayName', '')
            else:
                tn_q6 = tobj_q6.get('displayName', '')
            if tid_q6 and tn_q6:
                team_map_q6[tid_q6] = tn_q6
    
        for drive_q6 in drives_list_q6:
            plays_q6 = drive_q6.get('plays', [])
            for p_q6 in plays_q6:
                play_text_q6 = p_q6.get('text', '').lower()
                if 'field goal' in play_text_q6 and ('miss' in play_text_q6 or 'no good' in play_text_q6):
                    tid_q6 = p_q6.get('start', {}).get('team', {}).get('id', '')
                    tn_q6 = team_map_q6.get(tid_q6, '')
                    if tn_q6:
                        if tn_q6 not in fg_stats_q6:
                            fg_stats_q6[tn_q6] = {'made': 0, 'missed': 0}
                        fg_stats_q6[tn_q6]['missed'] += 1

    # Calculate success rates
    fg_rates_q6 = {}
    for tm_q6, stats_q6 in fg_stats_q6.items():
        total_q6 = stats_q6['made'] + stats_q6['missed']
        if total_q6 > 0:
            fg_rates_q6[tm_q6] = {
                'made': stats_q6['made'],
                'missed': stats_q6['missed'],
                'total': total_q6,
                'rate': stats_q6['made'] / total_q6
            }

    # Get Alabama's stats
    alabama_stats_q6 = fg_rates_q6.get('Alabama Crimson Tide', {})
    alabama_rate_q6 = alabama_stats_q6.get('rate', 1.0)
    alabama_made_q6 = alabama_stats_q6.get('made', 0)
    alabama_total_q6 = alabama_stats_q6.get('total', 0)

    # Calculate average rate for all teams (with at least 3 attempts)
    all_rates_q6 = [data['rate'] for data in fg_rates_q6.values() if data['total'] >= 3]
    avg_rate_q6 = sum(all_rates_q6) / len(all_rates_q6) if all_rates_q6 else 1.0

    q6 = 'yes' if alabama_rate_q6 < avg_rate_q6 else 'no'
    q6_1 = f"Alabama made {alabama_made_q6} of {alabama_total_q6} field goals ({alabama_rate_q6*100:.1f}% success rate) compared to the average team success rate of {avg_rate_q6*100:.1f}%. Alabama {'does' if q6 == 'yes' else 'does not'} miss field goals more often than average."
    return q6, q6_1


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Question 7
    **Safety Occurrences**

    A *safety* occurs when the offensive player with the ball is tackled or downs
    the ball in their own end zone. The defensive team scores 2 points and receives
    possession.

    **In how many games did a safety occur?**
    """
    )
    return


@app.cell
def _(game_dict):
    games_with_safety_q7 = 0

    for gfile_q7, gdata_q7 in game_dict.items():
        scoring_plays_q7 = gdata_q7.get('scoringPlays', [])
    
        for play_q7 in scoring_plays_q7:
            if play_q7.get('scoringType', {}).get('name') == 'safety':
                games_with_safety_q7 += 1
                break  # Count each game only once

    q7 = games_with_safety_q7
    return (q7,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Question 8
    **Which team(s) scored the most safeties?**

    Include all teams if there is a tie.
    """
    )
    return


@app.cell
def _(game_dict):
    safety_dict_q8 = {}

    for gfile_q8, gdata_q8 in game_dict.items():
        scoring_plays_q8 = gdata_q8.get('scoringPlays', [])
    
        for play_q8 in scoring_plays_q8:
            if play_q8.get('scoringType', {}).get('name') == 'safety':
                team_name_q8 = play_q8.get('team', {}).get('displayName', '')
                if team_name_q8:
                    safety_dict_q8[team_name_q8] = safety_dict_q8.get(team_name_q8, 0) + 1

    # Find team(s) with most safeties
    if safety_dict_q8:
        max_safeties_q8 = max(safety_dict_q8.values())
        q8 = [tm for tm, cnt in safety_dict_q8.items() if cnt == max_safeties_q8]
    else:
        q8 = []
    return (q8,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Question 9
    **Which three teams gave up the most safeties?**
    """
    )
    return


@app.cell
def _(game_dict):
    safeties_given_up_q9 = {}

    for gfile_q9, gdata_q9 in game_dict.items():
        scoring_plays_q9 = gdata_q9.get('scoringPlays', [])
        teams_data_q9 = gdata_q9.get('teams', [])
    
        for play_q9 in scoring_plays_q9:
            if play_q9.get('scoringType', {}).get('name') == 'safety':
                # Find the team that gave up the safety (opponent of scoring team)
                scoring_team_id_q9 = play_q9.get('team', {}).get('id', '')
            
                for team_obj_q9 in teams_data_q9:
                    if team_obj_q9.get('id') != scoring_team_id_q9:
                        if 'team' in team_obj_q9 and isinstance(team_obj_q9['team'], dict):
                            opponent_name_q9 = team_obj_q9['team'].get('displayName', '')
                        else:
                            opponent_name_q9 = team_obj_q9.get('displayName', '')
                    
                        if opponent_name_q9:
                            safeties_given_up_q9[opponent_name_q9] = safeties_given_up_q9.get(opponent_name_q9, 0) + 1
                        break

    # Get top 3 teams that gave up most safeties
    sorted_teams_q9 = sorted(safeties_given_up_q9.items(), key=lambda x: x[1], reverse=True)
    q9 = [team for team, count in sorted_teams_q9[:3]]
    return (q9,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Question 10
    **Find the longest play(s) in the 2017 season**

    For example: a 99-yard interception return or touchdown pass.

    If multiple plays tie for longest, show all of them with:
    - Team matchup
    - Quarter
    - Clock time
    - Play description
    """
    )
    return


@app.cell
def _(game_dict, re):
    def get_drives_list_q10(drives_data):
        if isinstance(drives_data, dict):
            return drives_data.get('previous', [])
        return drives_data if isinstance(drives_data, list) else []

    longest_plays_q10 = []
    max_yards_q10 = 0

    for gfile_q10, gdata_q10 in game_dict.items():
        drives_list_q10 = get_drives_list_q10(gdata_q10.get('drives', []))
        teams_data_q10 = gdata_q10.get('teams', [])
    
        team_names_q10 = []
        for team_obj_q10 in teams_data_q10:
            if 'team' in team_obj_q10 and isinstance(team_obj_q10['team'], dict):
                team_names_q10.append(team_obj_q10['team'].get('displayName', ''))
            else:
                team_names_q10.append(team_obj_q10.get('displayName', ''))
    
        matchup_q10 = ' vs '.join([t for t in team_names_q10 if t]) if team_names_q10 else gfile_q10[:50]
    
        for drive_q10 in drives_list_q10:
            plays_q10 = drive_q10.get('plays', [])
        
            for play_q10 in plays_q10:
                play_text_q10 = play_q10.get('text', '')
            
                # Skip kickoffs and extract yardage
                if 'kickoff' not in play_text_q10.lower():
                    yard_match_q10 = re.search(r'\bfor (\d+) yd', play_text_q10, re.IGNORECASE)
                    if yard_match_q10:
                        yards_q10 = int(yard_match_q10.group(1))
                    
                        if yards_q10 > max_yards_q10 and yards_q10 < 200:
                            max_yards_q10 = yards_q10
                            longest_plays_q10 = [{
                                'yards': yards_q10,
                                'matchup': matchup_q10,
                                'quarter': play_q10.get('period', {}).get('number', 'N/A'),
                                'clock': play_q10.get('clock', {}).get('displayValue', 'N/A'),
                                'description': play_text_q10.strip()
                            }]
                        elif yards_q10 == max_yards_q10 and yards_q10 > 0:
                            longest_plays_q10.append({
                                'yards': yards_q10,
                                'matchup': matchup_q10,
                                'quarter': play_q10.get('period', {}).get('number', 'N/A'),
                                'clock': play_q10.get('clock', {}).get('displayValue', 'N/A'),
                                'description': play_text_q10.strip()
                            })

    q10 = longest_plays_q10[:10]
    return (q10,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Question 11
    **Alabama's First and Last Offensive Plays**

    Provide the yardage and description for:
    - Alabama's FIRST offensive play of the season
    - Alabama's LAST offensive play of the season
    """
    )
    return


@app.cell
def _(game_dict, game_weeks, os, re):
    # Question 11: Alabama's First and Last Offensive Plays
    def get_drives_list_q11(drives_data):
        if isinstance(drives_data, dict):
            return drives_data.get('previous', [])
        return drives_data if isinstance(drives_data, list) else []

    alabama_plays_q11 = []

    # Process weeks in chronological order to maintain correct sequence
    for week_q11 in game_weeks:
        week_path_q11 = f'2017 NCAAF JSON/{week_q11}/full'
        if not os.path.exists(week_path_q11):
            continue
        
        for file_q11 in sorted(os.listdir(week_path_q11)):
            # Only process Alabama games
            if 'Alabama' not in file_q11:
                continue
            
            gdata_q11 = game_dict[file_q11]
            teams_data_q11 = gdata_q11.get('teams', [])
        
            # Find Alabama's team ID
            alabama_id_q11 = None
            for team_obj_q11 in teams_data_q11:
                if 'team' in team_obj_q11 and isinstance(team_obj_q11['team'], dict):
                    if 'Alabama' in team_obj_q11['team'].get('displayName', ''):
                        alabama_id_q11 = team_obj_q11.get('id')
                        break
        
            if not alabama_id_q11:
                continue
        
            # Get all drives from the game
            drives_list_q11 = get_drives_list_q11(gdata_q11.get('drives', []))
        
            for drive_q11 in drives_list_q11:
                plays_q11 = drive_q11.get('plays', [])
            
                for play_q11 in plays_q11:
                    # Check if this is an Alabama offensive play
                    play_team_id_q11 = play_q11.get('start', {}).get('team', {}).get('id', '')
                
                    if play_team_id_q11 == alabama_id_q11:
                        play_text_q11 = play_q11.get('text', '')
                        play_type_q11 = play_q11.get('type', {}).get('text', '')
                    
                        # Skip non-offensive plays
                        skip_terms = ['penalty', 'timeout', 'end of', 'end period', 'end quarter']
                        if any(skip in play_text_q11.lower() for skip in skip_terms):
                            continue
                        if 'kickoff' in play_type_q11.lower():
                            continue
                    
                        # Only include plays with actual text
                        if not play_text_q11.strip():
                            continue
                    
                        # Extract yardage
                        yards_q11 = None
                    
                        # Look for "for X yd" pattern
                        yard_match_q11 = re.search(r'\bfor (\d+) yd', play_text_q11, re.IGNORECASE)
                        if yard_match_q11:
                            yards_q11 = int(yard_match_q11.group(1))
                        # Look for "for a loss of X" pattern
                        elif 'for a loss of' in play_text_q11.lower():
                            loss_match_q11 = re.search(r'loss of (\d+)', play_text_q11, re.IGNORECASE)
                            if loss_match_q11:
                                yards_q11 = -int(loss_match_q11.group(1))
                    
                        # Add this play to the list
                        alabama_plays_q11.append({
                            'yards': yards_q11,
                            'description': play_text_q11.strip()
                        })

    # Create the answer dictionary with first and last plays
    if alabama_plays_q11:
        q11 = {
            'first': {
                'yards': alabama_plays_q11[0]['yards'],
                'description': alabama_plays_q11[0]['description']
            },
            'last': {
                'yards': alabama_plays_q11[-1]['yards'],
                'description': alabama_plays_q11[-1]['description']
            }
        }
    else:
        q11 = {}
    return (q11,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Question 12
    **How many times did Alabama punt in the 2017 season?**
    """
    )
    return


@app.cell
def _(game_dict, game_weeks, os):
    def get_drives_list_q12(drives_data):
        if isinstance(drives_data, dict):
            return drives_data.get('previous', [])
        return drives_data if isinstance(drives_data, list) else []

    alabama_punts_q12 = 0

    for week_q12 in game_weeks:
        week_path_q12 = f'2017 NCAAF JSON/{week_q12}/full'
        if not os.path.exists(week_path_q12):
            continue
        
        for file_q12 in sorted(os.listdir(week_path_q12)):
            if 'Alabama' not in file_q12:
                continue
            
            gdata_q12 = game_dict[file_q12]
            teams_data_q12 = gdata_q12.get('teams', [])
        
            alabama_id_q12 = None
            for team_obj_q12 in teams_data_q12:
                if 'team' in team_obj_q12 and isinstance(team_obj_q12['team'], dict):
                    if 'Alabama' in team_obj_q12['team'].get('displayName', ''):
                        alabama_id_q12 = team_obj_q12.get('id')
                        break
        
            if not alabama_id_q12:
                continue
        
            drives_list_q12 = get_drives_list_q12(gdata_q12.get('drives', []))
        
            for drive_q12 in drives_list_q12:
                plays_q12 = drive_q12.get('plays', [])
            
                for play_q12 in plays_q12:
                    play_team_id_q12 = play_q12.get('start', {}).get('team', {}).get('id', '')
                
                    if play_team_id_q12 == alabama_id_q12:
                        play_text_q12 = play_q12.get('text', '').lower()
                        play_type_q12 = play_q12.get('type', {}).get('text', '').lower()
                    
                        if 'punt' in play_text_q12 or 'punt' in play_type_q12:
                            if 'blocked' not in play_text_q12 and 'penalty' not in play_text_q12:
                                alabama_punts_q12 += 1

    q12 = alabama_punts_q12
    return (q12,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Question 13
    **Punt Distance Statistics**

    Calculate the longest, shortest, and median punt distance across all punts.
    Return as a dictionary with labeled values.
    """
    )
    return


@app.cell
def _(game_dict, re, statistics):
    def get_drives_list_q13(drives_data):
        if isinstance(drives_data, dict):
            return drives_data.get('previous', [])
        return drives_data if isinstance(drives_data, list) else []

    punt_distances_q13 = []

    for gfile_q13, gdata_q13 in game_dict.items():
        drives_list_q13 = get_drives_list_q13(gdata_q13.get('drives', []))
    
        for drive_q13 in drives_list_q13:
            plays_q13 = drive_q13.get('plays', [])
        
            for play_q13 in plays_q13:
                play_text_q13 = play_q13.get('text', '').lower()
                play_type_q13 = play_q13.get('type', {}).get('text', '').lower()
            
                if 'punt' in play_text_q13 or 'punt' in play_type_q13:
                    if 'blocked' in play_text_q13:
                        continue
                
                    punt_match_q13 = re.search(r'punt for (\d+) yd', play_text_q13)
                    if punt_match_q13:
                        distance_q13 = int(punt_match_q13.group(1))
                        punt_distances_q13.append(distance_q13)

    if punt_distances_q13:
        q13 = {
            'longest': max(punt_distances_q13),
            'shortest': min(punt_distances_q13),
            'median': statistics.median(punt_distances_q13)
        }
    else:
        q13 = {}
    return (q13,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Question 14
    **Offensive Performance Analysis Using Polars**

    Use the polars library to analyze offensive performance across all teams.

    Create a DataFrame of all drives and calculate per-team statistics:
    - Total number of drives
    - Average yards per drive
    - Touchdown percentage (% of drives ending in TD)
    - Turnover percentage (% of drives ending in turnover)

    Show the top 10 teams ranked by average yards per drive.
    """
    )
    return


@app.cell
def _(game_dict):
    # Your code here
    import polars as pl

    def get_drives_list_q14(drives_data):
        if isinstance(drives_data, dict):
            return drives_data.get('previous', [])
        return drives_data if isinstance(drives_data, list) else []

    drive_data_q14 = []

    for gfile_q14, gdata_q14 in game_dict.items():
        drives_list_q14 = get_drives_list_q14(gdata_q14.get('drives', []))
        teams_data_q14 = gdata_q14.get('teams', [])
    
        team_map_q14 = {}
        for team_obj_q14 in teams_data_q14:
            team_id_q14 = team_obj_q14.get('id')
            if 'team' in team_obj_q14 and isinstance(team_obj_q14['team'], dict):
                team_name_q14 = team_obj_q14['team'].get('displayName', '')
            else:
                team_name_q14 = team_obj_q14.get('displayName', '')
            if team_id_q14 and team_name_q14:
                team_map_q14[team_id_q14] = team_name_q14
    
        for drive_q14 in drives_list_q14:
            plays_q14 = drive_q14.get('plays', [])
            team_id_q14 = None
            if plays_q14:
                team_id_q14 = plays_q14[0].get('start', {}).get('team', {}).get('id', '')
        
            team_name_q14 = team_map_q14.get(team_id_q14, '')
        
            if not team_name_q14:
                continue
        
            yards_q14 = drive_q14.get('yards', 0)
            result_q14 = drive_q14.get('displayResult', '')
        
            is_td_q14 = 'TD' in result_q14 or 'Touchdown' in result_q14
            is_turnover_q14 = any(x in result_q14 for x in ['INT', 'Interception', 'Fumble', 'FUM', 'Turnover', 'Downs'])
        
            drive_data_q14.append({
                'team': team_name_q14,
                'yards': yards_q14,
                'is_td': is_td_q14,
                'is_turnover': is_turnover_q14
            })

    df_drives = pl.DataFrame(drive_data_q14)

    team_stats = df_drives.group_by('team').agg([
        pl.count('yards').alias('total_drives'),
        pl.mean('yards').alias('avg_yards_per_drive'),
        (pl.sum('is_td') * 100.0 / pl.count('yards')).alias('td_percentage'),
        (pl.sum('is_turnover') * 100.0 / pl.count('yards')).alias('turnover_percentage')
    ]).sort('avg_yards_per_drive', descending=True)

    top_10_teams_q14 = team_stats.head(10)
    q14 = top_10_teams_q14.to_dicts()
    return (q14,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Bonus Question (5 points)
    **Locate and retrieve a video highlight URL from one of the games.**
    """
    )
    return


@app.cell
def _(game_dict):
    for gfile_bonus, gdata_bonus in game_dict.items():
        videos_bonus = gdata_bonus.get('videos', [])
    
        for video_bonus in videos_bonus:
            if isinstance(video_bonus, dict) and 'links' in video_bonus:
                links_bonus = video_bonus['links']
                if isinstance(links_bonus, dict):
                    if 'web' in links_bonus and isinstance(links_bonus['web'], dict):
                        if 'href' in links_bonus['web']:
                            bonus = links_bonus['web']['href']
                            break
                    elif 'href' in links_bonus:
                        bonus = links_bonus['href']
                        break
            if bonus:
                break
        if bonus:
            break
    return (bonus,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ---
    ## Generate Answer File
    Compile all answers into a JSON file for submission.
    """
    )
    return


@app.cell
def _(
    bonus,
    q1,
    q10,
    q11,
    q12,
    q13,
    q14,
    q2,
    q3,
    q3_1,
    q4,
    q4_1,
    q5,
    q6,
    q6_1,
    q7,
    q8,
    q9,
):
    # Compile all answers into a single dictionary
    answer_file = {
        'q1': q1,
        'q2': q2,
        'q3': q3,
        'q3.1': q3_1,
        'q4': q4,
        'q4.1': q4_1,
        'q5': q5,
        'q6': q6,
        'q6.1': q6_1,
        'q7': q7,
        'q8': q8,
        'q9': q9,
        'q10': q10,
        'q11': q11,
        'q12': q12,
        'q13': q13,
        'q14': q14,  # Note: Convert polars DataFrame to appropriate format
        'Bonus': bonus
    }
    return (answer_file,)


@app.cell
def _(answer_file, json):
    # Write answer file to JSON with pretty formatting
    # Replace 'netid' with your NetID (e.g., gjbott)
    output_filename = "mis501_python_project_flelrod.json"

    with open(output_filename, "w") as outfile:
        json.dump(answer_file, outfile, indent=3)

    print(f"Answer file saved to: {output_filename}")
    return


if __name__ == "__main__":
    app.run()
