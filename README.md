# Muse S RAW EEG Data Processing - should also work the same for the Muse 2 band
Convert data from Mind Monitor to a WAV for viewing in spectrogram tools

Still a WIP right now but working pretty well. The script should be placed in the same folder as the MindView CSV and that CSV should be renamed to 'sleepData.csv'.

When recording from the Mind Monitor app you need to ensure you set the sampling rate to constant, this will generate large csv files because it's 256Hz so particularly for overnight sleep analysis it will be large but the zipped file is highly compressed before being uploaded by Mind Monitor.

You'll need all the relavant Python libraries as per the script.

The script processes data from AF7 into a WAV file that you can then use in either a dedicated spectrogram tool or something like Audacity https://manual.audacityteam.org/man/spectrogram_view.html

The script also exports relative brainwaves into a CSV that you can open in Excel - it downsamples the full file so it's more manageable. For charting etc I'd suggest adding a moving average so it's easier to see.

Once the script is finished it displays a PSD chart so you can sense check the data/processing.

Couple of caveats right now are that I need to work more on how bad data is handled, I think it's probably overly brutal. Also should make use of the other channels rather than just AF7. The axis are wrong the PSD chart too I think.

Example spectrogram in Audacity from a sleep session which was around 6 hours. I had a random bar at around 50Hz, apparently not uncommon sometimes:
![Screenshot](exampleSpectrogram.PNG)
