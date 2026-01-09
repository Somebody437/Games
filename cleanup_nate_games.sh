#!/bin/bash
#
# Script to remove duplicate/large games from nate-games to reduce repo size
# This will remove approximately 1+ GB of redundant game duplicates
#
# Run this from the repository root: bash cleanup_nate_games.sh
#

set -e  # Exit on error

GAMES_DIR="nate-games/0/g"

echo "================================================"
echo "Removing duplicate games from nate-games..."
echo "================================================"
echo ""

# Array of game folders to remove
REMOVE_GAMES=(
    "fnaf-2"           # Keep fnaf only
    "fnaf-3"
    "fnaf-4"
    "fnaf-5"
    "fnaf-fp"
    "fnaf-webgl"
    "fnaf-2hacks"
    "fnaf-3scratch"
    "fnafweb"
    
    "fnfmobile"        # Keep fnf only
    "fnfneo"
    "fnfvsimposter"
    "fnfmidfight"
    
    "minecraft-webgl"  # Keep minecraft only
    "PrecisionClient"
    "eaglercraft"
    "Paper Minecraft"
    "minecraft-classic"
    "mchacks"
    
    "geodashmeltdown"  # Keep geodash only
    "geodashscratch"
    "geodashsubzero"
    "geodashworld"
    
    "slope-2"
    "tunnel-rush2"
    "whg2"
    "whg3"
    "ovo2"
    "ovo3"
    "paperio3d"
    "hole.io-scratch"
    
    "BloonsTD2"        # Keep BloonsTD only
    "BloonsTD3"
    "BloonsTD4"
    "BloonsTD5"
    "btd-battles"
    "btd-battles2"
    
    "2048-multitask"
    "run2"
    "run3"
    "slitherscratch"
    "flappybird"
    "gravitydriver"
    "alienhominid"
    "aquapark-slides"
    "helixjump"
    "elasticman"
    "circle"
    "n-gon"
    "greybox"
    "baldisbasics"
    "backrooms"
    "omnomrun"
    "cut-the-rope"
    "bitlife"
    "monkeymart"
    "adarkroom"
    "snowball.io"
    "smashkarts"
    "draw-the-hill"
    "Undertale"
    "Terraria"
    "happyglass"
    "candycrush"
    "tombmask"
    "granny"
    "happywheels"
    "mr-bullet"
    "burger-frights"
    "msic"
    "Fortnite"
    "HexGL"
    "Hextris"
    "giag"
    "bf3d"
    "particleclicker"
    "fruit-ninja"
    "motox3m"
    "couch2048"
    "madgunz"
    "valorant"
    "doodle-jump"
    "shellshockers"
    "krunker"
    "among-us"
    "drive-mad"
    "eggycar"
    "nsmb"
    "smb"
    "sm64"
    "retrobowl"
    "fallguys"
    "Stumble Guys"
    "zombs-royale"
    "gettingoverit"
    "Roblox"
    "Roblox-Offline"
    "stickmanhook"
    "just-fall"
    "1v1lol"
    "slitherio"
    "sonic"
)

removed=0
skipped=0

# Remove each game folder
for game in "${REMOVE_GAMES[@]}"; do
    game_path="$GAMES_DIR/$game"
    if [ -d "$game_path" ]; then
        echo "Removing: $game"
        git rm -r --force "$game_path" > /dev/null 2>&1 || rm -rf "$game_path"
        ((removed++))
    else
        ((skipped++))
    fi
done

echo ""
echo "================================================"
echo "Removal complete!"
echo "  - Removed: $removed games"
echo "  - Skipped (not found): $skipped"
echo "================================================"
echo ""
echo "Checking repository size..."
du -sh . 
du -sh nate-games
echo ""
echo "Now commit the changes with:"
echo "  git add -A"
echo "  git commit -m 'Remove duplicate games to reduce repo size to <1GB'"
echo "  git push origin main"
