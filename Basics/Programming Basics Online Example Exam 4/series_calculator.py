ADS_TIME_PERCENT = 0.20
SPECIAL_EPISODE_MINUTES = 10 

series_name = input()
seasons = int(input())
season_episodes = int(input())
episode_length = float(input())

#calculate ads length for episode
total_episode_length = episode_length + episode_length * ADS_TIME_PERCENT

#calculate season length 
season_length = season_episodes * total_episode_length + SPECIAL_EPISODE_MINUTES
#calculate total length
seasons_length = int(seasons * season_length)

print(f"Total time needed to watch the {series_name} series is {seasons_length} minutes.")
