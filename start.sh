#!/bin/bash
# شروع FastAPI
python main.py &

# شروع Bot
python bot.py &

wait
