import pandas as pd

data = pd.read_csv('./data/list Hero.csv')

def getHeroData(hero_name):
    heroData = data[data['Hero Name'].str.lower() == hero_name.lower()]
    if not heroData.empty:
        return heroData.iloc[0]
    else:
        return None
    
def calculateTeamStrength(team):
    totalStrength = 0
    hero_data = {}
    for hero in team:
        data = getHeroData(hero)
        if data is not None:
            totalStrength += data['Strength Rating (%)']
            hero_data[hero] = data  
        else:
            print(f"Hero {hero} tidak ditemukan dalam dataset.")
    return totalStrength, hero_data

def calculateWinPercentage(team1, team2):
    team1Strength, team1_data = calculateTeamStrength(team1)
    team2Strength, team2_data = calculateTeamStrength(team2)
    
    if team1Strength == team2Strength:
        return 50, 50, team1_data, team2_data

    totalStrength = team1Strength + team2Strength
    team1WinPercentage = (team1Strength / totalStrength) * 100
    team2WinPercentage = (team2Strength / totalStrength) * 100

    return team1WinPercentage, team2WinPercentage, team1_data, team2_data

def generateMatchData(team1, team2, team1_data, team2_data):
    """
    Fungsi ini menerima dua tim (team1 dan team2) yang berisi nama hero yang dipilih oleh pengguna.
    Fungsi ini akan mengembalikan dictionary yang berisi data hero yang diperlukan untuk analisis dan modeling.
    """
    # Data untuk tim 1 (Tim yang dipilih oleh pengguna)
    team1_data_processed = {}
    for i, hero in enumerate(team1):
        hero_data = team1_data.get(hero)
        if hero_data is not None and not hero_data.empty:  # Periksa jika hero_data tidak kosong
            # Jangan masukkan Hero Name atau Role ke dalam fitur
            team1_data_processed.update({
                f'team1_Hero_{i+1}_Win_Rate': hero_data['Win Rate (%)'],
                f'team1_Hero_{i+1}_Popularity': hero_data['Popularity (%)'],
                f'team1_Hero_{i+1}_Ban_Rate': hero_data['Ban Rate (%)'],
                f'team1_Hero_{i+1}_Scaling_Rating': hero_data['Scaling Rating'],
                f'team1_Hero_{i+1}_Cooldown_Rating': hero_data['Cooldown Rating'],
                f'team1_Hero_{i+1}_Item_Dependency_Rating': hero_data['Item Dependency Rating'],
                f'team1_Hero_{i+1}_Mobility_Rating': hero_data['Mobility Rating'],
                f'team1_Hero_{i+1}_Crowd_Control_Rating': hero_data['Crowd Control Rating'],
                f'team1_Hero_{i+1}_Base_Stats_Growth_Rating': hero_data['Base Stats Growth Rating'],
                f'team1_Hero_{i+1}_Ultimate_Impact_Rating_All_Game_Phases': hero_data['Ultimate Impact Rating_All Game Phases'],
                f'team1_Hero_{i+1}_Ultimate_Impact_Rating_Early_Game': hero_data['Ultimate Impact Rating_Early Game'],
                f'team1_Hero_{i+1}_Ultimate_Impact_Rating_Late_Game': hero_data['Ultimate Impact Rating_Late Game'],
                f'team1_Hero_{i+1}_Ultimate_Impact_Rating_Mid_Game': hero_data['Ultimate Impact Rating_Mid Game'],
                f'team1_Hero_{i+1}_Ultimate_Impact_Rating_Support': hero_data['Ultimate Impact Rating_Support'],
                f'team1_Hero_{i+1}_Strength_Rating': hero_data['Strength Rating (%)']
            })
    
    # Data untuk tim 2 (Tim musuh yang dipilih oleh pengguna)
    team2_data_processed = {}
    for i, hero in enumerate(team2):
        hero_data = team2_data.get(hero)
        if hero_data is not None and not hero_data.empty:  # Periksa jika hero_data tidak kosong
            # Jangan masukkan Hero Name atau Role ke dalam fitur
            team2_data_processed.update({
                f'team2_Hero_{i+1}_Win_Rate': hero_data['Win Rate (%)'],
                f'team2_Hero_{i+1}_Popularity': hero_data['Popularity (%)'],
                f'team2_Hero_{i+1}_Ban_Rate': hero_data['Ban Rate (%)'],
                f'team2_Hero_{i+1}_Scaling_Rating': hero_data['Scaling Rating'],
                f'team2_Hero_{i+1}_Cooldown_Rating': hero_data['Cooldown Rating'],
                f'team2_Hero_{i+1}_Item_Dependency_Rating': hero_data['Item Dependency Rating'],
                f'team2_Hero_{i+1}_Mobility_Rating': hero_data['Mobility Rating'],
                f'team2_Hero_{i+1}_Crowd_Control_Rating': hero_data['Crowd Control Rating'],
                f'team2_Hero_{i+1}_Base_Stats_Growth_Rating': hero_data['Base Stats Growth Rating'],
                f'team2_Hero_{i+1}_Ultimate_Impact_Rating_All_Game_Phases': hero_data['Ultimate Impact Rating_All Game Phases'],
                f'team2_Hero_{i+1}_Ultimate_Impact_Rating_Early_Game': hero_data['Ultimate Impact Rating_Early Game'],
                f'team2_Hero_{i+1}_Ultimate_Impact_Rating_Late_Game': hero_data['Ultimate Impact Rating_Late Game'],
                f'team2_Hero_{i+1}_Ultimate_Impact_Rating_Mid_Game': hero_data['Ultimate Impact Rating_Mid Game'],
                f'team2_Hero_{i+1}_Ultimate_Impact_Rating_Support': hero_data['Ultimate Impact Rating_Support'],
                f'team2_Hero_{i+1}_Strength_Rating': hero_data['Strength Rating (%)']
            })
    
    # Gabungkan data tim 1 dan tim 2 serta persentase kemenangan
    team_data = {**team1_data_processed, **team2_data_processed}
    team1WinPercentage, team2WinPercentage, _, _ = calculateWinPercentage(team1, team2)
    team_data['Persentase_Kemenangan_Tim_1'] = team1WinPercentage
    team_data['Persentase_Kemenangan_Tim_2'] = team2WinPercentage
    
    return team_data