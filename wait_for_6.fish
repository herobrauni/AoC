#!/usr/bin/env fish

function main
    set -l target_time_str "today 06:00:00"

    while true
        set -l current_timestamp (date +%s)
        set -l target_timestamp (date -d "$target_time_str" +%s)

        if test $current_timestamp -ge $target_timestamp
            break
        end

        set -l remaining_seconds (math $target_timestamp - $current_timestamp)

        set -l hours (math $remaining_seconds / 3600)
        set -l minutes (math ($remaining_seconds % 3600) / 60)
        set -l seconds (math $remaining_seconds % 60)

        echo "Waiting for another $hours hours, $minutes minutes, and $seconds seconds."
        sleep 1s
    end

    ./init.fish
end

main
