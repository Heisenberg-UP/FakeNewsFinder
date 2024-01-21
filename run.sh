source env/bin/activate # Activates virtual environment

python files/fakenewsscraper.py & python files/gui.py # Runs necessary python files

rm files/NEWS.csv # Removes NEW.csv data when program is stopped

deactivate # Deactivates vitual environment
