#!/usr/bin/env python3
import os
import shutil
import subprocess

os.chdir('/workspaces/Games')

# Games to remove (duplicates and less important versions)
games_to_remove = [
    'fnaf-2', 'fnaf-3', 'fnaf-4', 'fnaf-5', 'fnaf-fp', 'fnaf-webgl', 
    'fnaf-2hacks', 'fnaf-3scratch', 'fnafweb',
    'fnfmobile', 'fnfneo', 'fnfvsimposter', 'fnfmidfight',
    'minecraft-webgl', 'PrecisionClient', 'eaglercraft', 'Paper Minecraft', 
    'minecraft-classic', 'mchacks',
    'geodashmeltdown', 'geodashscratch', 'geodashsubzero', 'geodashworld',
    'slope-2', 'tunnel-rush2', 'whg2', 'whg3', 'ovo2', 'ovo3', 'paperio3d', 
    'hole.io-scratch',
    'BloonsTD2', 'BloonsTD3', 'BloonsTD4', 'BloonsTD5', 'btd-battles', 'btd-battles2',
    '2048-multitask', 'run2', 'run3', 'slitherscratch', 'flappybird', 'gravitydriver',
    'alienhominid', 'aquapark-slides', 'helixjump', 'elasticman', 'circle', 'n-gon',
    'greybox', 'baldisbasics', 'backrooms', 'omnomrun', 'cut-the-rope', 'bitlife',
    'monkeymart', 'adarkroom', 'snowball.io', 'smashkarts', 'draw-the-hill', 
    'Undertale', 'Terraria', 'happyglass', 'candycrush', 'tombmask', 'granny',
    'happywheels', 'mr-bullet', 'burger-frights', 'msic', 'Fortnite', 'HexGL',
    'Hextris', 'giag', 'bf3d', 'particleclicker', 'fruit-ninja', 'motox3m',
    'couch2048', 'madgunz', 'valorant', 'doodle-jump', 'shellshockers', 'krunker',
    'among-us', 'drive-mad', 'eggycar', 'nsmb', 'smb', 'sm64', 'retrobowl',
    'fallguys', 'Stumble Guys', 'zombs-royale', 'gettingoverit', 'Roblox',
    'Roblox-Offline', 'stickmanhook', 'just-fall', '1v1lol', 'slitherio', 'sonic'
]

games_dir = 'nate-games/0/g'
removed = 0

print("Removing duplicate games...")
for game in games_to_remove:
    game_path = os.path.join(games_dir, game)
    if os.path.exists(game_path):
        try:
            if os.path.isdir(game_path):
                shutil.rmtree(game_path)
            removed += 1
            print(f"✓ {game}")
        except Exception as e:
            print(f"✗ {game}: {e}")

print(f"\nRemoved {removed} games")

# Get size info
result = subprocess.run(['du', '-sh', '.'], capture_output=True, text=True)
print(f"\nTotal repo size: {result.stdout.strip()}")

result = subprocess.run(['du', '-sh', 'nate-games'], capture_output=True, text=True)
print(f"nate-games size: {result.stdout.strip()}")
