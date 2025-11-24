#!/usr/bin/env fish

function main
    set -l day $argv[1]
    set -l year $argv[2]

    # Set defaults if arguments are missing
    if test -z "$day"
        set day (date +%d)
    end
    
    # Remove leading zeros for calculation/validation
    set -l day_int (string trim --left --chars=0 "$day")
    if test -z "$day_int" # Handle case where day was "00" or "0"
        set day_int 0
    end

    if test -z "$year"
        set year (date +%Y)
    end

    # Validation
    if test $day_int -lt 1 -o $day_int -gt 25
        echo "Day not in range (1-25)"
        return 1
    end

    # Format day for folder (leading zero)
    set -l day_for_folder (printf "%02d" $day_int)

    # Setup Environment
    set -x AOC_USER_AGENT "aoc@brauni.dev"
    if test -f ./AoC_private/session.txt
        set -x AOC_SESSION (cat ./AoC_private/session.txt | string trim)
    else
        echo "Error: ./AoC_private/session.txt not found."
        return 1
    end

    # Create directories
    mkdir -p "./$year/$day_for_folder"
    mkdir -p "./AoC_private/$year/$day_for_folder"

    # Fetch Input and Example using uv run aocd
    # Note: Passing raw day/year to aocd. aocd handles integers fine.
    uv run aocd $day_int $year | string trim --right > "./AoC_private/$year/$day_for_folder/input.txt"
    uv run aocd $day_int $year --example | string trim --right > "./$year/$day_for_folder/example.txt"

    # Fetch Statement HTML
    # Using python for robust HTML string extraction to match init.nu logic
    set -l url "https://adventofcode.com/$year/day/$day_int"
    set -l cookie "session=$AOC_SESSION"
    set -l user_agent "User-Agent=$AOC_USER_AGENT"
    
    echo "Fetching statement from $url..."
    
    # Fetch with curl, process with python
    curl -s -H "Cookie: $cookie" -H "$user_agent" "$url" | uv run python -c "
import sys

html = sys.stdin.read()

start_tag = '<article>'
end_tag = '</article>'
success_tag = '</code>'

start_idx = html.find(start_tag)
if start_idx == -1:
    # Fallback or exit if no article found (e.g. 404 or not logged in properly)
    sys.exit(0)

end_idx = html.rfind(end_tag)
if end_idx != -1:
    end_idx += len(end_tag)

success_idx = html.rfind(success_tag)
if success_idx != -1:
    success_idx += len(success_tag)

# Logic from init.nu: max of end or success
final_end = max(end_idx, success_idx) if success_idx != -1 else end_idx

if final_end != -1:
    print(html[start_idx:final_end].strip())
else:
    print(html[start_idx:].strip())
" > "./AoC_private/$year/$day_for_folder/statement.html"

    # Git operations
    if test -d ./AoC_private
        pushd ./AoC_private
        git add .
        git commit -m "$year/$day_for_folder"
        popd
    end

    # Create link.url
    printf "[InternetShortcut]\nURL=%s\n" "$url" > "./$year/$day_for_folder/link.url"

    # Create code template
    uv run python make_code.py $day_int $year

    # Open VS Code
    if type -q code
        code "./$year/$day_for_folder/code.py" "./AoC_private/$year/$day_for_folder/input.txt"
    end

    # Paste output to console (run aocd again)
    uv run aocd $day_int $year

    # Open Browser
    # Check for BROWSER env var, fallback to xdg-open (linux) or open (mac)
    set -l browser_cmd "$BROWSER"
    if test -z "$browser_cmd"
        if type -q xdg-open
            set browser_cmd xdg-open
        else if type -q open
            set browser_cmd open
        end
    end

    if test -n "$browser_cmd"
        $browser_cmd "$url"
    else
        echo "Could not detect browser to open URL."
    end
end

main $argv
