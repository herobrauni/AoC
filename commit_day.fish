#!/usr/bin/env fish
# Commit & push a solved AoC day: private inputs submodule first, then this repo.
#   ./commit_day.fish                  # message = the changed day, e.g. 2016/05
#   ./commit_day.fish 2016/05          # explicit day as message
#   ./commit_day.fish "fix part 2"     # your own message

function changed_days
    for repo in . AoC_private
        for path in (git -C $repo status --porcelain -uall | string sub -s 4)
            set -l m (string match -r '^[0-9]{4}/[0-9]{2}/' -- $path)
            test -n "$m"; and echo (string trim --right --chars=/ -- $m)
        end
    end
end

function main
    cd (git rev-parse --show-toplevel); or begin
        echo "error: not inside a git repository" >&2
        return 1
    end

    set -l days (changed_days | sort -u)
    set -l default_msg (date +%Y/%d)
    test -n "$days[1]"; and set default_msg $days[1]

    # Note: no `if` block here — `read` would scope `msg` to that block.
    set -l msg $argv[1]
    test -z "$msg"; and isatty stdin; and read -l -P "Commit message [$default_msg]: " msg
    test -n "$msg"; or set msg $default_msg

    if test (count $days) -gt 1
        echo "note: multiple changed days ($days), using $msg" >&2
    end

    # 1. Private submodule: puzzle inputs, statements, …
    set -l priv (git -C AoC_private status --porcelain)
    if test -n "$priv"
        git -C AoC_private add -A; or return 1
        git -C AoC_private commit -m "$msg"; or return 1
        git -C AoC_private push; or return 1
        echo "pushed AoC_private: $msg"
    else
        echo "AoC_private: nothing to commit"
    end

    # 2. This repo: the day folder(s) + the updated submodule pointer
    set -l paths
    for p in $days AoC_private
        test -e $p; and set -a paths $p
    end
    test -n "$paths[1]"; or set paths -A

    set -l dirty (git status --porcelain)
    if test -n "$dirty"
        git add -A -- $paths; or return 1
        git commit -m "$msg"; or return 1
        git push; or return 1
        echo "pushed aoc: $msg"
    else
        echo "aoc: nothing to commit"
    end
end

main $argv
