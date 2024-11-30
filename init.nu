#!/usr/bin/env nu

# can be empty, must be string
def main [day?: string, year?: string] = {
    # if empty get current day / year
    let day = match $day {
        null => { date now | format date %d }
        _ => { $day | into int }
    }
    let year = match $year {
        null => { date now | format date %Y }
        _ => $year     
    }
    # add leading 0 for better folder structure
    let day_for_folder = if ($day | into int)  < 10 { ['0', $day] | str join } else { $day }
    # user agent for no abuse and session for auth
    $env.AOC_USER_AGENT = "aoc@brauni.dev"
    $env.AOC_SESSION = (open ./AoC_private/session.txt)
    mkdir $"./($year)/($day_for_folder)"
    mkdir $"./AoC_private/($year)/($day_for_folder)"
    # aocd module (pip install advent-of-code-data) to get and cache inputs etc.
    aocd $day $year | str trim -r | save $"./AoC_private/($year)/($day_for_folder)/input.txt" -f
    aocd $day $year --example | str trim -r | save $"./($year)/($day_for_folder)/example.txt" -f

    let headers = {
        cookie: $"session=($env.AOC_SESSION)"
        headers: $"User-Agent=($env.AOC_USER_AGENT)"
    }
    # get aoc html site, get start and end of text and paste it to statement file
    # will include solutions if logged in and already submitted
    let site = http get $"https://adventofcode.com/($year)/day/($day)" --headers $headers
    let start = $site | str index-of "<article"
    let end = ($site | str index-of -e "</article>") + ('</article>' | str length )
    let end_success = ($site | str index-of -e "</code>") + ('</code>' | str length )
    let eend = if $end_success != null { [$end | $end_success] | math max } else { $end }
    $site | str substring $start..$eend | save $"./AoC_private/($year)/($day_for_folder)/statement.html" -f

    # create link url
    $"[InternetShortcut]\nURL=https://adventofcode.com/($year)/day/($day)\n" | save $"./($year)/($day_for_folder)/link.url" -f
    
    # create code template
    ^python make_code.py $day $year
    # open template
    ^code $"./($year)/($day_for_folder)/code.py"

    # open browser with todays site
    ^$env.BROWSER $"https://adventofcode.com/($year)/day/($day)"
}
