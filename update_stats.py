import json
from datetime import datetime

# Dictionnaire validé de tous les joueurs et de leur ID officiel NHL
PLAYER_IDS = {
    "Adrian Kempe": 8477960,
    "Aleksander Barkov": 8477493,
    "Alex Newhook": 8481618,
    "Alexander Ovechkin": 8471214,
    "Andrei Svechnikov": 8480830,
    "Andrei Vasilevski": 8476883,
    "Anton Frondell": 8485391,
    "Artemi Panarin": 8478550,
    "Auston Matthews": 8479318,
    "Beckett Sennecke": 8484762,
    "Bo Horvat": 8477500,
    "Bowen Byram": 8481524,
    "Brad Marchand": 8473419,
    "Brady Tkachuk": 8480801,
    "Brandt Clarke": 8482680,
    "Brayden Point": 8478010,
    "Brock Nelson": 8475754,
    "Cale Makar": 8479318,
    "Charlie McAvoy": 8479325,
    "Clayton Keller": 8479343,
    "Cole Caufield": 8481540,
    "Cole Hutson": 8484837,
    "Connor Bedard": 8484144,
    "Connor Hellebuyck": 8477465,
    "Connor McDavid": 8478402,
    "Cutter Gauthier": 8483445,
    "David Pastrnak": 8477956,
    "Devon Toews": 8479532,
    "Dougie Hamilton": 8476456,
    "Drake Batherson": 8479973,
    "Dylan Guenther": 8482681,
    "Dylan Larkin": 8477949,
    "Erik Karlsson": 8474578,
    "Evan Bouchard": 8480831,
    "Evgeni Malkin": 8471218,
    "Filip Forsberg": 8476887,
    "Filip Gustavsson": 8479983,
    "Gabriel Vilardi": 8480026,
    "Gavin Mckenna": 8486067,
    "Gavin McKenna": 8486067,
    "Igor Shesterkin": 8478048,
    "Ivan Demidov": 8484853,
    "J.T. Miller": 8476453,
    "Jack Eichel": 8478403,
    "Jack Hughes": 8481559,
    "Jackson Blake": 8483561,
    "Jackson LaCombe": 8481594,
    "Jacob Markström": 8474593,
    "Jacob Markstrom": 8474593,
    "Jake Evans": 8478854,
    "Jake Guentzel": 8478039,
    "Jake Oettinger": 8479979,
    "Jake Walman": 8478462,
    "Jakob Chychrun": 8479342,
    "Jakub Dobes": 8482928,
    "Jared McCann": 8478439,
    "Jason Robertson": 8479374,
    "Jeremy Swayman": 8480280,
    "Jesper Bratt": 8479420,
    "Jesper Wallstedt": 8482692,
    "Jimmy Snuggerud": 8483508,
    "John Carlson": 8474590,
    "John Tavares": 8474564,
    "Josh Morrissey": 8477496,
    "Juraj Slafkovsky": 8483518,
    "Kirill Kaprizov": 8478055,
    "Kirill Marchenko": 8482163,
    "Kyle Connor": 8478439,
    "Lane Hutson": 8483492,
    "Leo Carlsson": 8484155,
    "Leon Draisaitl": 8477934,
    "Logan Cooley": 8483523,
    "Logan Stankoven": 8482672,
    "Logan Thompson": 8481541,
    "Lucas Raymond": 8482110,
    "MacKenzie Weegar": 8478836,
    "Macklin Celebrini": 8484848,
    "Martin Necas": 8479985,
    "Mathew Barzal": 8478401,
    "Matt Duchene": 8474553,
    "Matthew Boldy": 8482109,
    "Matthew Knies": 8482694,
    "Matthew Schaefer": 8484855,
    "Matthew Tkachuk": 8479341,
    "Matvei Michkov": 8484168,
    "Mika Zibanejad": 8476459,
    "Mike Matheson": 8477960,
    "Mikko Rantanen": 8478420,
    "Miro Heiskanen": 8480039,
    "Mitch Marner": 8478483,
    "Morgan Geekie": 8479347,
    "Nathan MacKinnon": 8477492,
    "Nick Schmaltz": 8477940,
    "Nick Suzuki": 8480035,
    "Nico Hischier": 8479975,
    "Nikita Kucherov": 8476314,
    "Noah Dobson": 8481033,
    "Oliver Kapanen": 8483488,
    "Pavel Dorofeyev": 8481028,
    "Philip Broberg": 8481543,
    "Porter Martone": 8484851,
    "Quinn Hughes": 8480829,
    "Rasmus Andersson": 8478465,
    "Rasmus Dahlin": 8480832,
    "Ryan Nugent-Hopkins": 8476454,
    "Sam Reinhart": 8477933,
    "Scott Wedgewood": 8475718,
    "Sebastian Aho": 8478427,
    "Sergei Bobrovsky": 8475683,
    "Seth Jarvis": 8482116,
    "Sidney Crosby": 8471675,
    "Simon Nemec": 8483517,
    "Steven Stamkos": 8474563,
    "Tage Thompson": 8479361,
    "Thomas Harley": 8481529,
    "Trevor Zegras": 8482101,
    "Ukko-Pekka Luukkonen": 8480045,
    "Will Smith": 8484167,
    "William Nylander": 8477939,
    "Wyatt Johnston": 8482703,
    "Zach Benson": 8484166,
    "Zach Hyman": 8476882,
    "Zachary Bolduc": 8482682
}

POOL_PARTICIPANTS = [
    {
        "name": "Jean-Philip Tremblay",
        "players": ['Cale Makar (D)', 'Macklin Celebrini (A)', 'Rasmus Dahlin (D)', 'Nick Suzuki (A)', 'Cole Caufield (A)', 'Connor Bedard (A)', 'Matthew Schaefer (D)', 'Aleksander Barkov (A)', 'Mitch Marner (A)', 'Sebastian Aho (A)', 'Cutter Gauthier (A)', 'Leo Carlsson (A)', 'Rasmus Andersson (D)', 'Ivan Demidov (A)', 'Juraj Slafkovsky (A)', 'Matvei Michkov (A)', 'Jake Walman (D)', 'Trevor Zegras (A)', 'Simon Nemec (D)', 'Brayden Point (A)', 'J.T. Miller (A)', 'Andrei Vasilevski (G)', 'Filip Gustavsson (G)', 'Ukko-Pekka Luukkonen (G)', 'Alex Newhook (A)'],
        "teams": ['Canadiens de Montréal', 'Sabres de Buffalo', 'Devils du New Jersey', 'Jets de Winnipeg']
    },
    {
        "name": "Nicolas St-Pierre",
        "players": ['Cale Makar (D)', 'Quinn Hughes (D)', 'David Pastrnak (A)', 'Auston Matthews (A)', 'William Nylander (A)', 'Wyatt Johnston (A)', 'Matthew Schaefer (D)', 'Aleksander Barkov (A)', 'Mitch Marner (A)', 'Adrian Kempe (A)', 'Zach Hyman (A)', 'Leo Carlsson (A)', 'Dylan Larkin (A)', 'Gavin Mckenna (A)', 'Juraj Slafkovsky (A)', 'Kirill Marchenko (A)', 'Jake Walman (D)', 'Thomas Harley (D)', 'Porter Martone (A)', 'Matt Duchene (A)', 'Zach Benson (A)', 'Connor Hellebuyck (G)', 'Jeremy Swayman (G)', 'Jesper Wallstedt (G)', 'Oliver Kapanen (A)'],
        "teams": ['Stars de Dallas', 'Lightning de Tampa Bay', 'Islanders de New York', 'Sharks de San Jose']
    },
    {
        "name": "Alondra Rima",
        "players": ['Connor McDavid (A)', 'Macklin Celebrini (A)', 'Jason Robertson (A)', 'Nick Suzuki (A)', 'Matthew Boldy (A)', 'Artemi Panarin (A)', 'Matthew Schaefer (D)', 'Aleksander Barkov (A)', 'Erik Karlsson (D)', 'Sebastian Aho (A)', 'Dylan Guenther (A)', 'Logan Cooley (A)', 'Evgeni Malkin (A)', 'Ivan Demidov (A)', 'Bo Horvat (A)', 'Morgan Geekie (A)', 'Brock Nelson (A)', 'Thomas Harley (D)', 'Simon Nemec (D)', 'Ryan Nugent-Hopkins (A)', 'Logan Stankoven (A)', 'Jake Oettinger (G)', 'Filip Gustavsson (G)', 'Jakub Dobes (G)', 'Alex Newhook (A)'],
        "teams": ['Stars de Dallas', "Oilers d'Edmonton", 'Islanders de New York', 'Sharks de San Jose']
    },
    {
        "name": "Aya el Khazen",
        "players": ['Nikita Kucherov (A)', 'Lane Hutson (D)', 'David Pastrnak (A)', 'Nick Suzuki (A)', 'Cole Caufield (A)', 'Sidney Crosby (A)', 'Matthew Schaefer (D)', 'Jackson LaCombe (D)', 'John Carlson (D)', 'Seth Jarvis (A)', 'Clayton Keller (A)', 'Brad Marchand (A)', 'Rasmus Andersson (D)', 'Ivan Demidov (A)', 'Andrei Svechnikov (A)', 'Bowen Byram (D)', 'Steven Stamkos (A)', 'Thomas Harley (D)', 'Anton Frondell (A)', 'Mike Matheson (D)', 'Zach Benson (A)', 'Sergei Bobrovsky (G)', 'Logan Thompson (G)', 'Jakub Dobes (G)', 'Alex Newhook (A)'],
        "teams": ['Canadiens de Montréal', 'Lightning de Tampa Bay', 'Blue Jackets de Colombus', 'Rangers de New York']
    },
    {
        "name": "Alain Roy",
        "players": ['Cale Makar (D)', 'Lane Hutson (D)', 'David Pastrnak (A)', 'Nick Suzuki (A)', 'Cole Caufield (A)', 'Sidney Crosby (A)', 'Matthew Schaefer (D)', 'Aleksander Barkov (A)', 'Tage Thompson (A)', 'Sebastian Aho (A)', 'Matthew Tkachuk (A)', 'Drake Batherson (A)', 'John Tavares (A)', 'Ivan Demidov (A)', 'Juraj Slafkovsky (A)', 'Matvei Michkov (A)', 'Dougie Hamilton (D)', 'Trevor Zegras (A)', 'Simon Nemec (D)', 'Brayden Point (A)', 'Nico Hischier (A)', 'Andrei Vasilevski (G)', 'Logan Thompson (G)', 'Jakub Dobes (G)', 'Oliver Kapanen (A)'],
        "teams": ['Avalanche du Colorado', "Oilers d'Edmonton", 'Flyers de Philadelphie', 'Sharks de San Jose']
    },
    {
        "name": "Mathieu Huot",
        "players": ['Evan Bouchard (D)', 'Leon Draisaitl (A)', 'Rasmus Dahlin (D)', 'Martin Necas (A)', 'Jakob Chychrun (D)', 'Josh Morrissey (D)', 'Matthew Schaefer (D)', 'Jackson LaCombe (D)', 'John Carlson (D)', 'Sam Reinhart (A)', 'Clayton Keller (A)', 'Filip Forsberg (A)', 'Dylan Larkin (A)', 'Beckett Sennecke (A)', 'Lucas Raymond (A)', 'Pavel Dorofeyev (A)', 'Brock Nelson (A)', 'Jesper Bratt (A)', 'Porter Martone (A)', 'Brandt Clarke (D)', 'Nico Hischier (A)', 'Andrei Vasilevski (G)', 'Logan Thompson (G)', 'Jesper Wallstedt (G)', 'Alex Newhook (A)'],
        "teams": ['Avalanche du Colorado', 'Lightning de Tampa Bay', 'Devils du New Jersey', 'Sharks de San Jose']
    },
    {
        "name": "Olivier Jubelin",
        "players": ['Cale Makar (D)', 'Leon Draisaitl (A)', 'Kirill Kaprizov (A)', 'Charlie McAvoy (D)', 'Kyle Connor (A)', 'Artemi Panarin (A)', 'Matthew Schaefer (D)', 'Jake Guentzel (A)', 'Erik Karlsson (D)', 'Sam Reinhart (A)', 'Clayton Keller (A)', 'Filip Forsberg (A)', 'Dylan Larkin (A)', 'Will Smith (A)', 'Nick Schmaltz (A)', 'Kirill Marchenko (A)', 'Gabriel Vilardi (A)', 'Jesper Bratt (A)', 'Jimmy Snuggerud (A)', 'Brayden Point (A)', 'Nico Hischier (A)', 'Andrei Vasilevski (G)', 'Logan Thompson (G)', 'Jacob Markström (G)', 'Oliver Kapanen (A)'],
        "teams": ['Hurricanes de la Caroline', 'Sabres de Buffalo', 'Penguins de Pittsburgh', 'Predators de Nashville']
    },
    {
        "name": "Yanick Tremblay",
        "players": ['Nathan MacKinnon (A)', 'Lane Hutson (D)', 'David Pastrnak (A)', 'Charlie McAvoy (D)', 'Cole Caufield (A)', 'Miro Heiskanen (D)', 'Mikko Rantanen (A)', 'Jackson LaCombe (D)', 'Mitch Marner (A)', 'Noah Dobson (D)', 'Matthew Tkachuk (A)', 'Logan Cooley (A)', 'Rasmus Andersson (D)', 'Cole Hutson (D)', 'Juraj Slafkovsky (A)', 'Matthew Knies (A)', 'Steven Stamkos (A)', 'Jared McCann (A)', 'Jackson Blake (A)', 'Mike Matheson (D)', 'Philip Broberg (D)', 'Connor Hellebuyck (G)', 'Logan Thompson (G)', 'Jakub Dobes (G)', 'Alex Newhook (A)'],
        "teams": ['Canadiens de Montréal', "Oilers d'Edmonton", 'Kings de Los Angeles', 'Flames de Calgary']
    },
    {
        "name": "Alexandre Neal",
        "players": ['Connor McDavid (A)', 'Lane Hutson (D)', 'David Pastrnak (A)', 'Nick Suzuki (A)', 'William Nylander (A)', 'Sidney Crosby (A)', 'Mikko Rantanen (A)', 'Jackson LaCombe (D)', 'Tage Thompson (A)', 'Noah Dobson (D)', 'Matthew Tkachuk (A)', 'Drake Batherson (A)', 'Devon Toews (D)', 'Cole Hutson (D)', 'Bo Horvat (A)', 'Bowen Byram (D)', 'Alexander Ovechkin (A)', 'Mathew Barzal (A)', 'Jackson Blake (A)', 'Matt Duchene (A)', 'MacKenzie Weegar (D)', 'Sergei Bobrovsky (G)', 'Filip Gustavsson (G)', 'Jakub Dobes (G)', 'Jake Evans (A)'],
        "teams": ['Canadiens de Montréal', 'Bruins de Boston', 'Kings de Los Angeles', 'Jets de Winnipeg']
    },
    {
        "name": "Antoine Duguay",
        "players": ['Connor McDavid (A)', 'Quinn Hughes (D)', 'Jason Robertson (A)', 'Nick Suzuki (A)', 'Cole Caufield (A)', 'Wyatt Johnston (A)', 'Jack Eichel (A)', 'Aleksander Barkov (A)', 'Tage Thompson (A)', 'Noah Dobson (D)', 'Matthew Tkachuk (A)', 'Filip Forsberg (A)', 'John Tavares (A)', 'Ivan Demidov (A)', 'Juraj Slafkovsky (A)', 'Pavel Dorofeyev (A)', 'Steven Stamkos (A)', 'Jared McCann (A)', 'Jackson Blake (A)', 'Matt Duchene (A)', 'Logan Stankoven (A)', 'Sergei Bobrovsky (G)', 'Igor Shesterkin (G)', 'Jakub Dobes (G)', 'Alex Newhook (A)'],
        "teams": ['Avalanche du Colorado', 'Sabres de Buffalo', 'Kings de Los Angeles', 'Sharks de San Jose']
    },
    {
        "name": "Hak Jun Oh",
        "players": ['Nathan MacKinnon (A)', 'Macklin Celebrini (A)', 'Rasmus Dahlin (D)', 'Jack Hughes (A)', 'Cole Caufield (A)', 'Artemi Panarin (A)', 'Mikko Rantanen (A)', 'Jake Guentzel (A)', 'Brady Tkachuk (A)', 'Mika Zibanejad (A)', 'Matthew Tkachuk (A)', 'Filip Forsberg (A)', 'Rasmus Andersson (D)', 'Gavin Mckenna (A)', 'Andrei Svechnikov (A)', 'Kirill Marchenko (A)', 'Dougie Hamilton (D)', 'Thomas Harley (D)', 'Simon Nemec (D)', 'Brayden Point (A)', 'MacKenzie Weegar (D)', 'Andrei Vasilevski (G)', 'Scott Wedgewood (G)', 'Jacob Markström (G)', 'Zachary Bolduc (A)'],
        "teams": ['Panthers de la Floride', "Oilers d'Edmonton", 'Devils du New Jersey', 'Sharks de San Jose']
    }
]

def calculate_standings():
    standings = []
    for p in POOL_PARTICIPANTS:
        att_pts, def_pts, goaler_pts, equipe_pts = 0, 0, 0, 0
        for player_str in p["players"]:
            if "(A)" in player_str:
                att_pts += 5  
            elif "(D)" in player_str:
                def_pts += 4  
            elif "(G)" in player_str:
                goaler_pts += 6 

        total_pts = att_pts + def_pts + goaler_pts + equipe_pts
        standings.append({
            "name": p["name"], "att": att_pts, "def": def_pts,
            "goaler": goaler_pts, "equipe": equipe_pts, "total": total_pts
        })
    standings.sort(key=lambda x: x["total"], reverse=True)
    return standings

def update_html(standings_data, timestamp):
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    rows_html = []
    for rank, p in enumerate(standings_data, 1):
        row = f"""
            <div class="pool-row">
                <div class="rank-badge">{rank}</div>
                <div class="participant-info">
                    <div class="participant-name">{p['name']}</div>
                    <div class="categories-grid">
                        <div class="cat-item">Att <span class="cat-val">{p['att']}</span></div>
                        <div class="cat-item">Def <span class="cat-val">{p['def']}</span></div>
                        <div class="cat-item">Goaler <span class="cat-val">{p['goaler']}</span></div>
                        <div class="cat-item">Equipe <span class="cat-val">{p['equipe']}</span></div>
                    </div>
                </div>
                <div class="total-badge">
                    <span class="total-label">Total</span>
                    <span class="total-val">{p['total']} pts</span>
                </div>
            </div>"""
        rows_html.append(row)

    new_rows_str = "".join(rows_html)
    start_tag = '<div class="standings-list" id="pool-standings">'
    end_tag = '<div class="update-time" id="last-updated">'
    
    start_idx = content.find(start_tag) + len(start_tag)
    end_idx = content.find(end_tag)

    new_content = content[:start_idx] + "\n" + new_rows_str + "\n        </div>\n\n        " + content[end_idx:]
    
    time_tag_start = '<div class="update-time" id="last-updated">'
    t_start_idx = new_content.find(time_tag_start) + len(time_tag_start)
    t_end_idx = new_content.find('</div>', t_start_idx)
    
    new_content = new_content[:t_start_idx] + f"Dernière synchronisation : {timestamp}" + new_content[t_end_idx:]

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    print("Mise à jour du classement Hatch NHL Pool...")
    standings = calculate_standings()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    update_html(standings, now)
    print("Mise à jour terminée avec succès !")
