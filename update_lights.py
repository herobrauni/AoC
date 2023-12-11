## Updates the Lights on my Christmas Tree to show my AOC Stars

import requests
from datetime import date as dt

import neopixel
import board
import sys

pixels = neopixel.NeoPixel(board.D18, 50)
pixels.fill((0, 0, 0))


YEAR = dt.today().year
ADVENT_URL = "https://adventofcode.com"
USER_ID = ""
USER_NAME = str(sys.argv[1])
SESSION_COOKIE = str(sys.argv[2])
LEADERBOARD_ID = str(sys.argv[3])
STARS_ENDPOINT = f"{ADVENT_URL}/{YEAR}/leaderboard/private/view/{LEADERBOARD_ID}.json"

res = requests.get(STARS_ENDPOINT, cookies={"session": SESSION_COOKIE})
res.raise_for_status()

leaderboard_info = res.json()

USER_ID = [x for x in leaderboard_info["members"] if leaderboard_info["members"][x]["name"] == USER_NAME][0]

stars = leaderboard_info["members"][USER_ID]["completion_day_level"]

stars_dict = {}

for day, parts in stars.items():
    # print(day, parts)
    # print(parts.keys())
    stars_dict[day] = [x for x in parts.keys()]

for days, parts in stars_dict.items():
    if "1" in parts:
        pixels[(int(days) - 1) * 2] = (255, 0, 0)
        # print(days,(int(days)-1)*2)
    if "2" in parts:
        pixels[(int(days) - 1) * 2 + 1] = (0, 255, 0)
        # print(days,(int(days)-1)*2+1)
