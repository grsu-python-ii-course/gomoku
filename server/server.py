import requests
import yaml


# Read config
def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


config = read_yaml('settings.yaml')
print(config)

# Generate games
# YOU CODE HERE

# LOOP FOR GAMES
# YOU CODE HERE

# One game

# GAMEPLAY
# Send request to user 1

user1_ip = config['USERS'][0]
res = requests.post(f'http://{user1_ip}/game', json={"mytext": "lalala"})

if res.ok:
    print(res.json())

# RECALCULATE BOARD if shoot correct
# YOU CODE HERE

# SAVE history
# YOU CODE HERE

# END OF GAMES
# SAVE HISTORY TO FILE 'game_log.json'
# YOU CODE HERE

