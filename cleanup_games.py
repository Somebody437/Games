#!/usr/bin/env python3
import os
import shutil
import sys

os.chdir('/workspaces/Games/nate-games/0/g')

# Games to remove (duplicates and less important versions)
games_to_remove = [
    # FNAF duplicates - keep fnaf only
    'fnaf-2', 'fnaf-3', 'fnaf-4', 'fnaf-5', 'fnaf-fp', 'fnaf-webgl', 
    'fnaf-2hacks', 'fnaf-3scratch', 'fnafweb',
    
    # FNF duplicates - keep fnf only
    'fnfmobile', 'fnfneo', 'fnfvsimposter', 'fnfmidfight',
    
    # Minecraft duplicates - keep minecraft only
    'minecraft-webgl', 'PrecisionClient', 'eaglercraft', 'Paper Minecraft', 
    'minecraft-classic', 'mchacks',
    
    # Geometry Dash duplicates - keep geodash only
    'geodashmeltdown', 'geodashscratch', 'geodashsubzero', 'geodashworld',
    
    # Simple duplicates
    'slope-2', 'tunnel-rush2',
    'whg2', 'whg3',  # Keep only whg
    'ovo2', 'ovo3',  # Keep only ovo
    'paperio3d',  # Keep paperio2
    'hole.io-scratch',  # Keep hole.io
    
    # Bloons TD duplicates - keep BloonsTD only  
    'BloonsTD2', 'BloonsTD3', 'BloonsTD4', 'BloonsTD5', 'btd-battles', 'btd-battles2',
    
    # Other duplicates
    '2048-multitask',  # Keep 2048
    'run2', 'run3',  # Keep run
    'slitherscratch',  # Keep slitherio
    'flappybird',
    'gravitydriver',
    'alienhominid',
    'aquapark-slides',
    'helixjump',
    'elasticman',
    'circle',
    'n-gon',
    'greybox',
    'baldisbasics',
    'backrooms',
    'omnomrun',
    'cut-the-rope',
    'bitlife',
    'monkeymart',
    'adarkroom',
    'snowball.io',
    'smashkarts',
    'draw-the-hill',
    'Undertale',
    'Terraria',
    'happyglass',
    'candycrush',
    'tombmask',
    'granny',
    'happywheels',
    'mr-bullet',
    'burger-frights',
    'msic',
    'Fortnite',
    'HexGL',
    'Hextris',
    'giag',
    'bf3d',
    'particleclicker',
    'fruit-ninja',
    'motox3m',
    'couch2048',
    'madgunz',
    'valorant',
    'doodle-jump',
    'shellshockers',
    'krunker',
    'among-us',
    'drive-mad',
    'eggycar',
    'nsmb',
    'smb',
    'sm64',
    'retrobowl',
    'fallguys',
    'Stumble Guys',
    'zombs-royale',
    'gettingoverit',
    'acidroomreboot',
    'Roblox',
    'Roblox-Offline',
    'stickmanhook',
    'just-fall',
    '1v1lol',
    'HexGL',
    'slitherio',
    'sonic',
]

removed_count = 0
for game in games_to_remove:
    game_path = game
    if os.path.exists(game_path):
        try:
            if os.path.isdir(game_path):
                shutil.rmtree(game_path)
            else:
                os.remove(game_path)
            print(f"✓ Removed: {game}")
            removed_count += 1
        except Exception as e:
            print(f"✗ Failed to remove {game}: {e}")
    else:
        print(f"- Not found: {game}")

print(f"\nTotal removed: {removed_count} games/folders")

# Report final size
import subprocess
result = subprocess.run(['du', '-sh', '/workspaces/Games'], capture_output=True, text=True)
print(f"\nFinal repo size: {result.stdout.strip()}")
