#!/usr/bin/env nu

while (date now) < ('today at 06:00' | into datetime) {
    print "waiting"
    sleep 1sec
}

./init.nu