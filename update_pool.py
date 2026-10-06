import json
import urllib.request
from datetime import datetime

TEAM_DATA = {
    "Montreal Canadiens": {"id": 8, "abbrev": "MTL"},
    "Dallas Stars": {"id": 25, "abbrev": "DAL"},
    "Carolina Hurricanes": {"id": 12, "abbrev": "CAR"},
    "Colorado Avalanche": {"id": 21, "abbrev": "COL"},
    "Florida Panthers": {"id": 13, "abbrev": "FLA"},
    "Buffalo Sabres": {"id": 7, "abbrev": "BUF"},
    "Tampa Bay Lightning": {"id": 14, "abbrev": "TBL"},
    "Edmonton Oilers": {"id": 22, "abbrev": "EDM"},
    "Boston Bruins": {"id": 6, "abbrev": "BOS"},
    "New Jersey Devils": {"id": 1, "abbrev": "NJD"},
    "New York Islanders": {"id": 2, "abbrev": "NYI"},
    "Columbus Blue Jackets": {"id": 29, "abbrev": "CBJ"},
    "Philadelphia Flyers": {"id": 4, "abbrev": "PHI"},
    "Pittsburgh Penguins": {"id": 5, "abbrev": "PIT"},
    "Los Angeles Kings": {"id": 26, "abbrev": "LAK"},
    "Winnipeg Jets": {"id": 52, "abbrev": "WPG"},
    "San Jose Sharks": {"id": 28, "abbrev": "SJS"},
    "New York Rangers": {"id": 3, "abbrev": "NYR"},
    "Nashville Predators": {"id": 18, "abbrev": "NSH"},
    "Calgary Flames": {"id": 20, "abbrev": "CGY"}
}

PLAYER_DATA = {
    "Adrian Kempe": {"id": 8477960, "position": "A"},
    "Aleksander Barkov": {"id": 8477493, "position": "A"},
    "Alex Newhook": {"id": 8481618, "position": "A"},
    "Alexander Ovechkin": {"id": 8471214, "position": "A"},
    "Andrei Svechnikov": {"id": 8480830, "position": "A"},
    "Anton Frondell": {"id": 8485391, "position": "A"},
    "Artemi Panarin": {"id": 8478550, "position": "A"},
    "Auston Matthews": {"id": 8479318, "position": "A"},
    "Beckett Sennecke": {"id": 8484762, "position": "A"},
    "Bo Horvat": {"id": 8477500, "position": "A"},
    "Brad Marchand": {"id": 8473419, "position": "A"},
    "Brady Tkachuk": {"id": 8480828, "position": "A"},
    "Brayden Point": {"id": 8478440, "position": "A"},
    "Brock Nelson": {"id": 8476359, "position": "A"},
    "Clayton Keller": {"id": 8479325, "position": "A"},
    "Cole Caufield": {"id": 8481540, "position": "A"},
    "Connor Bedard": {"id": 8484144, "position": "A"},
    "Connor McDavid": {"id": 8478402, "position": "A"},
    "Cutter Gauthier": {"id": 8483445, "position": "A"},
    "David Pastrnak": {"id": 8477956, "position": "A"},
    "Drake Batherson": {"id": 8479983, "position": "A"},
    "Dylan Guenther": {"id": 8482681, "position": "A"},
    "Dylan Larkin": {"id": 8477939, "position": "A"},
    "Evgeni Malkin": {"id": 8471161, "position": "A"},
    "Filip Forsberg": {"id": 8476887, "position": "A"},
    "Gabriel Vilardi": {"id": 8480028, "position": "A"},
    "Gavin McKenna": {"id": 8485412, "position": "A"},
    "Ivan Demidov": {"id": 8484835, "position": "A"},
    "J.T. Miller": {"id": 8476459, "position": "A"},
    "Jack Eichel": {"id": 8478403, "position": "A"},
    "Jack Hughes": {"id": 8481559, "position": "A"},
    "Jackson Blake": {"id": 8483669, "position": "A"},
    "Jake Evans": {"id": 8478894, "position": "A"},
    "Jake Guentzel": {"id": 8477496, "position": "A"},
    "Jared McCann": {"id": 8478404, "position": "A"},
    "Jason Robertson": {"id": 8479350, "position": "A"},
    "Jesper Bratt": {"id": 8479420, "position": "A"},
    "Jimmy Snuggerud": {"id": 8483492, "position": "A"},
    "John Tavares": {"id": 8475166, "position": "A"},
    "Juraj Slafkovsky": {"id": 8483507, "position": "A"},
    "Kirill Kaprizov": {"id": 8478864, "position": "A"},
    "Kirill Marchenko": {"id": 8482154, "position": "A"},
    "Kyle Connor": {"id": 8478398, "position": "A"},
    "Leo Carlsson": {"id": 8484153, "position": "A"},
    "Leon Draisaitl": {"id": 8477934, "position": "A"},
    "Logan Cooley": {"id": 8483431, "position": "A"},
    "Logan Stankoven": {"id": 8482747, "position": "A"},
    "Lucas Raymond": {"id": 8482109, "position": "A"},
    "Macklin Celebrini": {"id": 8484829, "position": "A"},
    "Martin Necas": {"id": 8479364, "position": "A"},
    "Mathew Barzal": {"id": 8478439, "position": "A"},
    "Matt Duchene": {"id": 8475168, "position": "A"},
    "Matthew Boldy": {"id": 8482103, "position": "A"},
    "Matthew Knies": {"id": 8482688, "position": "A"},
    "Matthew Tkachuk": {"id": 8479314, "position": "A"},
    "Matvei Michkov": {"id": 8484198, "position": "A"},
    "Mika Zibanejad": {"id": 8476345, "position": "A"},
    "Mikko Rantanen": {"id": 8478420, "position": "A"},
    "Mitch Marner": {"id": 8478483, "position": "A"},
    "Morgan Geekie": {"id": 8479435, "position": "A"},
    "Nathan MacKinnon": {"id": 8477492, "position": "A"},
    "Nick Schmaltz": {"id": 8477960, "position": "A"},
    "Nick Suzuki": {"id": 8480018, "position": "A"},
    "Nico Hischier": {"id": 8479979, "position": "A"},
    "Nikita Kucherov": {"id": 8476453, "position": "A"},
    "Oliver Kapanen": {"id": 8482956, "position": "A"},
    "Pavel Dorofeyev": {"id": 8481021, "position": "A"},
    "Porter Martone": {"id": 8485413, "position": "A"},
    "Ryan Nugent-Hopkins": {"id": 8476456, "position": "A"},
    "Sam Reinhart": {"id": 8477933, "position": "A"},
    "Sebastian Aho": {"id": 8478427, "position": "A"},
    "Seth Jarvis": {"id": 8482116, "position": "A"},
    "Sidney Crosby": {"id": 8471675, "position": "A"},
    "Steven Stamkos": {"id": 8474564, "position": "A"},
    "Tage Thompson": {"id": 8479338, "position": "A"},
    "Trevor Zegras": {"id": 8482146, "position": "A"},
    "Will Smith": {"id": 8484158, "position": "A"},
    "William Nylander": {"id": 8477937, "position": "A"},
    "Wyatt Johnston": {"id": 8482813, "position": "A"},
    "Zach Benson": {"id": 8484168, "position": "A"},
    "Zach Hyman": {"id": 8476104, "position": "A"},
    "Zachary Bolduc": {"id": 8482695, "position": "A"},
    # Défenseurs
    "Bowen Byram": {"id": 8481535, "position": "D"},
    "Brandt Clarke": {"id": 8482680, "position": "D"},
    "Cale Makar": {"id": 8479344, "position": "D"},
    "Charlie McAvoy": {"id": 8479324, "position": "D"},
    "Cole Hutson": {"id": 8484787, "position": "D"},
    "Devon Toews": {"id": 8479407, "position": "D"},
    "Dougie Hamilton": {"id": 8476454, "position": "D"},
    "Erik Karlsson": {"id": 8474578, "position": "D"},
    "Evan Bouchard": {"id": 8480878, "position": "D"},
    "Jackson LaCombe": {"id": 8481585, "position": "D"},
    "Jakob Chychrun": {"id": 8479342, "position": "D"},
    "Jake Walman": {"id": 8478013, "position": "D"},
    "John Carlson": {"id": 8474590, "position": "D"},
    "Josh Morrissey": {"id": 8477497, "position": "D"},
    "Lane Hutson": {"id": 8483515, "position": "D"},
    "MacKenzie Weegar": {"id": 8478853, "position": "D"},
    "Matthew Schaefer": {"id": 8485410, "position": "D"},
    "Mike Matheson": {"id": 8477504, "position": "D"},
    "Miro Heiskanen": {"id": 8480036, "position": "D"},
    "Noah Dobson": {"id": 8481031, "position": "D"},
    "Philip Broberg": {"id": 8481552, "position": "D"},
    "Quinn Hughes": {"id": 8480800, "position": "D"},
    "Rasmus Andersson": {"id": 8478498, "position": "D"},
    "Rasmus Dahlin": {"id": 8480829, "position": "D"},
    "Simon Nemec": {"id": 8483501, "position": "D"},
    "Thomas Harley": {"id": 8481542, "position": "D"},
    # Gardiens
    "Andrei Vasilevskiy": {"id": 8476883, "position": "G"},
    "Connor Hellebuyck": {"id": 8477356, "position": "G"},
    "Filip Gustavsson": {"id": 8479977, "position": "G"},
    "Igor Shesterkin": {"id": 8478048, "position": "G"},
    "Jacob Markstrom": {"id": 8475225, "position": "G"},
    "Jake Oettinger": {"id": 8480280, "position": "G"},
    "Jakub Dobes": {"id": 8482928, "position": "G"},
    "Jeremy Swayman": {"id": 8480284, "position": "G"},
    "Jesper Wallstedt": {"id": 8482662, "position": "G"},
    "Logan Thompson": {"id": 8481541, "position": "G"},
    "Scott Wedgewood": {"id": 8475883, "position": "G"},
    "Sergei Bobrovsky": {"id": 8475683, "position": "G"},
    "Ukko-Pekka Luukkonen": {"id": 8480173, "position": "G"}
}

PARTICIPANTS_ROSTERS = [
    {
        "name": "Mathieu Huot",
        "players": ["Evan Bouchard", "Leon Draisaitl", "Rasmus Dahlin", "Martin Necas", "Jakob Chychrun", "Josh Morrissey", "John Carlson", "Sam Reinhart", "Clayton Keller", "Filip Forsberg", "Dylan Larkin", "Lucas Raymond", "Pavel Dorofeyev", "Brock Nelson", "Jesper Bratt", "Nico Hischier", "Alex Newhook"],
        "goalies": ["Andrei Vasilevskiy", "Logan Thompson", "Jesper Wallstedt"],
        "teams": ["Colorado Avalanche", "Tampa Bay Lightning", "New Jersey Devils", "San Jose Sharks"]
    },
    {
        "name": "Jean-Philip Tremblay",
        "players": ["Cale Makar", "Macklin Celebrini", "Rasmus Dahlin", "Nick Suzuki", "Cole Caufield", "Connor Bedard", "Aleksander Barkov", "Mitch Marner", "Sebastian Aho", "Cutter Gauthier", "Leo Carlsson", "Rasmus Andersson", "Juraj Slafkovsky", "Matvei Michkov", "Jake Walman", "Trevor Zegras", "Brayden Point", "J.T. Miller", "Nico Hischier", "Alex Newhook"],
        "goalies": ["Andrei Vasilevskiy", "Filip Gustavsson", "Ukko-Pekka Luukkonen"],
        "teams": ["Montreal Canadiens", "Buffalo Sabres", "New Jersey Devils", "Winnipeg Jets"]
    },
    {
        "name": "Nicolas St-Pierre",
        "players": ["Cale Makar", "Quinn Hughes", "David Pastrnak", "Auston Matthews", "William Nylander", "Wyatt Johnston", "Aleksander Barkov", "Mitch Marner", "Adrian Kempe", "Zach Hyman", "Leo Carlsson", "Dylan Larkin", "Juraj Slafkovsky", "Kirill Marchenko", "Jake Walman", "Thomas Harley", "Matt Duchene", "Zach Benson", "Oliver Kapanen"],
        "goalies": ["Connor Hellebuyck", "Jeremy Swayman", "Jesper Wallstedt"],
        "teams": ["Dallas Stars", "Tampa Bay Lightning", "New York Islanders", "San Jose Sharks"]
    },
    {
        "name": "Alondra Rima",
        "players": ["Connor McDavid", "Macklin Celebrini", "Jason Robertson", "Nick Suzuki", "Matthew Boldy", "Artemi Panarin", "Aleksander Barkov", "Erik Karlsson", "Sebastian Aho", "Dylan Guenther", "Logan Cooley", "Evgeni Malkin", "Bo Horvat", "Brock Nelson", "Thomas Harley", "Logan Stankoven", "Alex Newhook"],
        "goalies": ["Jake Oettinger", "Filip Gustavsson", "Jakub Dobes"],
        "teams": ["Dallas Stars", "Edmonton Oilers", "New York Islanders", "San Jose Sharks"]
    },
    {
        "name": "Aya el Khazen",
        "players": ["Nikita Kucherov", "Lane Hutson", "David Pastrnak", "Nick Suzuki", "Cole Caufield", "Sidney Crosby", "John Carlson", "Seth Jarvis", "Clayton Keller", "Brad Marchand", "Rasmus Andersson", "Andrei Svechnikov", "Steven Stamkos", "Thomas Harley", "Mike Matheson", "Zach Benson", "Alex Newhook"],
        "goalies": ["Sergei Bobrovsky", "Logan Thompson", "Jakub Dobes"],
        "teams": ["Montreal Canadiens", "Tampa Bay Lightning", "Columbus Blue Jackets", "New York Rangers"]
    },
    {
        "name": "Alain Roy",
        "players": ["Cale Makar", "Lane Hutson", "David Pastrnak", "Nick Suzuki", "Cole Caufield", "Sidney Crosby", "Aleksander Barkov", "Tage Thompson", "Sebastian Aho", "Matthew Tkachuk", "Drake Batherson", "John Tavares", "Juraj Slafkovsky", "Matvei Michkov", "Dougie Hamilton", "Trevor Zegras", "Brayden Point", "Nico Hischier", "Oliver Kapanen"],
        "goalies": ["Andrei Vasilevskiy", "Logan Thompson", "Jakub Dobes"],
        "teams": ["Colorado Avalanche", "Edmonton Oilers", "Philadelphia Flyers", "San Jose Sharks"]
    },
    {
        "name": "Olivier Jubelin",
        "players": ["Cale Makar", "Leon Draisaitl", "Kirill Kaprizov", "Charlie McAvoy", "Kyle Connor", "Artemi Panarin", "Jake Guentzel", "Erik Karlsson", "Sam Reinhart", "Clayton Keller", "Filip Forsberg", "Dylan Larkin", "Will Smith", "Nick Schmaltz", "Kirill Marchenko", "Gabriel Vilardi", "Jesper Bratt", "Brayden Point", "Nico Hischier", "Oliver Kapanen"],
        "goalies": ["Andrei Vasilevskiy", "Logan Thompson", "Jacob Markstrom"],
        "teams": ["Carolina Hurricanes", "Buffalo Sabres", "Pittsburgh Penguins", "Nashville Predators"]
    },
    {
        "name": "Yanick Tremblay",
        "players": ["Nathan MacKinnon", "Lane Hutson", "David Pastrnak", "Charlie McAvoy", "Cole Caufield", "Miro Heiskanen", "Mikko Rantanen", "Mitch Marner", "Noah Dobson", "Matthew Tkachuk", "Logan Cooley", "Rasmus Andersson", "Juraj Slafkovsky", "Matthew Knies", "Steven Stamkos", "Jared McCann", "Mike Matheson", "Philip Broberg", "Alex Newhook"],
        "goalies": ["Connor Hellebuyck", "Logan Thompson", "Jakub Dobes"],
        "teams": ["Montreal Canadiens", "Edmonton Oilers", "Los Angeles Kings", "Calgary Flames"]
    },
    {
        "name": "Alexandre Neal",
        "players": ["Connor McDavid", "Lane Hutson", "David Pastrnak", "Nick Suzuki", "William Nylander", "Sidney Crosby", "Mikko Rantanen", "Tage Thompson", "Noah Dobson", "Matthew Tkachuk", "Drake Batherson", "Devon Toews", "Bo Horvat", "Alexander Ovechkin", "Mathew Barzal", "Matt Duchene", "Jake Evans"],
        "goalies": ["Sergei Bobrovsky", "Filip Gustavsson", "Jakub Dobes"],
        "teams": ["Montreal Canadiens", "Boston Bruins", "Los Angeles Kings", "Winnipeg Jets"]
    },
    {
        "name": "Antoine Duguay",
        "players": ["Connor McDavid", "Quinn Hughes", "Jason Robertson", "Nick Suzuki", "Cole Caufield", "Wyatt Johnston", "Jack Eichel", "Aleksander Barkov", "Tage Thompson", "Noah Dobson", "Matthew Tkachuk", "Filip Forsberg", "John Tavares", "Juraj Slafkovsky", "Pavel Dorofeyev", "Steven Stamkos", "Jared McCann", "Matt Duchene", "Logan Stankoven", "Alex Newhook"],
        "goalies": ["Sergei Bobrovsky", "Igor Shesterkin", "Jakub Dobes"],
        "teams": ["Colorado Avalanche", "Buffalo Sabres", "Los Angeles Kings", "San Jose Sharks"]
    },
    {
        "name": "Hak Jun Oh",
        "players": ["Nathan MacKinnon", "Macklin Celebrini", "Rasmus Dahlin", "Jack Hughes", "Cole Caufield", "Artemi Panarin", "Mikko Rantanen", "Jake Guentzel", "Brady Tkachuk", "Mika Zibanejad", "Matthew Tkachuk", "Filip Forsberg", "Rasmus Andersson", "Andrei Svechnikov", "Kirill Marchenko", "Dougie Hamilton", "Thomas Harley", "Brayden Point", "Zachary Bolduc"],
        "goalies": ["Andrei Vasilevskiy", "Scott Wedgewood", "Jacob Markstrom"],
        "teams": ["Florida Panthers", "Edmonton Oilers", "New Jersey Devils", "San Jose Sharks"]
    }
]

def fetch_nhl_standings():
    url = "https://api-web.nhle.com/v1/standings/now"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            team_records = {}
            for standing in data.get('standings', []):
                t_abbrev = standing.get('teamAbbrev', {}).get('default', '')
                rw = standing.get('regulationWins', 0)
                row = standing.get('otWins', 0)
                otl = standing.get('otLosses', 0)
                # Règles de pointage des équipes
                total_pts = (rw * 2) + (row * 2) + (otl * 1)
                team_records[t_abbrev] = {
                    "rw": rw,
                    "row": row,
                    "otl": otl,
                    "points": total_pts
                }
            return team_records
    except Exception as e:
        print(f"Erreur classements: {e}")
        return {}

def fetch_player_stats(player_id):
    url = f"https://api-web.nhle.com/v1/player/{player_id}/landing"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            featured = data.get('featuredStats', {}).get('regularSeason', {}).get('subSeason', {})
            if featured:
                goals = featured.get('goals', 0)
                assists = featured.get('assists', 0)
                points = featured.get('points', goals + assists)
                return {"goals": goals, "assists": assists, "points": points}
            return {"goals": 0, "assists": 0, "points": 0}
    except Exception as e:
        return {"goals": 0, "assists": 0, "points": 0}

def main():
    team_records_map = fetch_nhl_standings()
    
    output_data = {
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "participants": []
    }

    for p in PARTICIPANTS_ROSTERS:
        att_pts = 0
        def_pts = 0
        goaler_pts = 0
        eq_pts = 0
        
        players_detailed = []
        for player_name in p["players"]:
            info = PLAYER_DATA.get(player_name)
            if info:
                stats = fetch_player_stats(info["id"])
                players_detailed.append({
                    "name": player_name,
                    "position": info["position"],
                    "goals": stats["goals"],
                    "assists": stats["assists"],
                    "points": stats["points"]
                })
                if info["position"] == 'A':
                    att_pts += stats["points"]
                elif info["position"] == 'D':
                    def_pts += stats["points"]

        goalies_detailed = []
        for goalie_name in p["goalies"]:
            info = PLAYER_DATA.get(goalie_name)
            if info:
                stats = fetch_player_stats(info["id"])
                goalies_detailed.append({
                    "name": goalie_name,
                    "goals": stats["goals"],
                    "assists": stats["assists"],
                    "points": stats["points"]
                })
                goaler_pts += stats["points"]

        teams_detailed = []
        for team_name in p["teams"]:
            t_info = TEAM_DATA.get(team_name)
            if t_info:
                rec = team_records_map.get(t_info["abbrev"], {"rw": 0, "row": 0, "otl": 0, "points": 0})
                teams_detailed.append({
                    "name": team_name,
                    "abbrev": t_info["abbrev"],
                    "rw": rec["rw"],
                    "row": rec["row"],
                    "otl": rec["otl"],
                    "points": rec["points"]
                })
                eq_pts += rec["points"]

        total_pts = att_pts + def_pts + goaler_pts + eq_pts

        output_data["participants"].append({
            "name": p["name"],
            "att": att_pts,
            "def": def_pts,
            "goaler": goaler_pts,
            "equipe": eq_pts,
            "total": total_pts,
            "roster_details": {
                "players": players_detailed,
                "goalies": goalies_detailed,
                "teams": teams_detailed
            }
        })

    with open('pool_data.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
