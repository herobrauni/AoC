#!/usr/bin/env nu

while (date now) < ('today at 06:00:00' | into datetime) {
    print $"waiting for another ((('today at 06:00:00' | into datetime)) - (date now))"
    sleep 1sec
}

./init.nu