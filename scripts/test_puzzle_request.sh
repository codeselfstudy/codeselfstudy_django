#!/bin/bash

# This is intended to test the Slack requests, but it might not work yet.
# (I got it working without needing it.)

curl -X POST http://localhost:8000/slack/puzzles/ -H 'Content-Type: application/x-www-form-urlencoded' -d 'token=xxxxxxxxxxxxxxxxxxxx&team_id=xxxxxxxxx&team_domain=xxxxxxxxxxxxx&channel_id=xxxxxxxxx&channel_name=directmessage&user_id=xxxxxxxxx&user_name=xxxx&command=%2Fpuzzle&text=codewars+medium&api_app_id=xxxxxxxxx&is_enterprise_install=false&response_url=https%3A%2F%2Fhooks.slack.com%2Fxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&trigger_id=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
