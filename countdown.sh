#!/bin/bash

echo "⏳ Enter countdown time (seconds):"
read time

while [ $time -gt 0 ]; do
    echo "$time seconds remaining..."
    sleep 1
    time=$((time - 1))
done

echo "⏰ Time's up!"
