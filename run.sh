source env/bin/activate # Activates virtual environment

cd files/ # Move into directory with python files

python fakenewsscraper.py & python gui.py # Runs necessary python files

rm NEWS.csv # Removes NEW.csv data when program is stopped

cd .. # Move out of files directory

deactivate # Deactivates vitual environment
