source env/bin/activate # Activates virtual environment

python python/fakenewsscraper.py & python python/gui.py # Runs necessary python files

rm csv/NEWS.csv # Removes NEW.csv data when program is stopped

deactivate # Deactivates vitual environment
