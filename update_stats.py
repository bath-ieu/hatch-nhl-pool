def update_html(standings_data, timestamp):
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # Génération du HTML des lignes de classement
    rows_html = []
    for rank, p in enumerate(standings_data, 1):
        row = f"""
            <div class="pool-row">
                <div class="rank-badge">{rank}</div>
                <div class="participant-info">
                    <div class="participant-name" onclick="openModal('{p['name']}')">{p['name']} 🔍</div>
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

    # Injection de la liste des participants dans le HTML et de la variable JSON pour la modale
    json_data_str = json.dumps(standings_data, ensure_ascii=False)
    
    # Remplacement des balises dans index.html
    # On met à jour la liste HTML
    start_tag = '<div class="standings-list" id="pool-standings">'
    end_tag = '<div class="update-time" id="last-updated">'
    
    start_idx = content.find(start_tag) + len(start_tag)
    end_idx = content.find(end_tag)

    new_content = content[:start_idx] + "\n" + new_rows_str + "\n        </div>\n\n        " + content[end_idx:]

    # Insertion des données JSON pour les scripts de la modale
    new_content = new_content.replace('const poolData = /*POOL_DATA_JSON*/;', f'const poolData = {json_data_str};')

    # Mise à jour de l'horodatage
    time_tag_start = 'Dernière synchronisation : '
    t_start_idx = new_content.find(time_tag_start)
    if t_start_idx != -1:
        t_end_idx = new_content.find('</div>', t_start_idx)
        new_content = new_content[:t_start_idx] + f"Dernière synchronisation : {timestamp}" + new_content[t_end_idx:]

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
