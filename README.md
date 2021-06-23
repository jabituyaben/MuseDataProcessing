# Muse S RAW EEG Data Processing - should also work the same for the Muse 2 band
Convert data from Mind Monitor to a WAV for viewing in spectrogram tools

Still a WIP right now but working pretty well. The script should be placed in the same folder as the MindView CSV and that CSV should be renamed to 'sleepData.csv'. The script may likely need to be modified so you reference the right columns if your setup for Mind View csv exports are setup differently with different order to the columns - which they quite likely will be.

When recording from the Mind Monitor app you need to ensure you set the sampling rate to constant, this will generate large csv files because it's 256Hz so particularly for overnight sleep analysis it will be large but the zipped file is highly compressed before being uploaded by Mind Monitor.

You'll need all the relavant Python libraries as per the script.

The script processes data from AF7 and AF8 (average) into a WAV file that you can then use in either a dedicated spectrogram tool or something like Audacity https://manual.audacityteam.org/man/spectrogram_view.html

The script also exports relative brainwaves into a CSV that you can open in Excel - it downsamples the full file so it's more manageable. For charting etc I'd suggest adding a moving average so it's easier to see.

Couple of caveats right now are that I need to work more on how bad data is handled, I think it's probably overly brutal. Also should make use of the other channels too and probably do some more on signal processing.

Example spectrogram in Audacity from a sleep session which was around 6 hours. I had a random bar at around 50Hz, apparently not uncommon sometimes:
![image](https://user-images.githubusercontent.com/74158243/123174436-02055500-d478-11eb-89da-23840e798e4c.png)


View from a different tool (http://spek.cc/)


![image](https://user-images.githubusercontent.com/74158243/123173514-9ec6f300-d476-11eb-9e03-15e7b7864f03.png)

Other Links:

Mind Monitor App
https://mind-monitor.com/
