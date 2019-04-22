# Mars-Rover-Data-Analysis
This repository contains python scripts to analyze some data collected by the Chemcam instrument on Curiosity Mars Rover.

fullread.py

This script was used to take in all of the MOC files provided by Ralf and create a separate csv file that contains the Chemcam team's results for data analysis. This separate csv file called Ultmoc6.csv is what I used for my final plots when I plotted my peak areas against the Chemcam team's results.
-------------------------------------------------------------------------------------------
NameCleaner.py

This script was used to rename all Chemcam raw data files to only the digits found in their initial names. For ex. File named: CL5_43534543RDR.csv is renamed to 43534543.csv.
-------------------------------------------------------------------------------------------
relocationclean.py

This file was used to drop the first 5 laser shots from all raw data files to ensure I don't include the dust observed in each observation. Furthermore, this script creates a new file in a new directory for ease of use.
-------------------------------------------------------------------------------------------
remover.py

For ease of iteration, I removed all files that ended with .lbl as these files were unnecessary.
-------------------------------------------------------------------------------------------
rockyuniv.py 

Further clean raw data files to only keep the columns, rows, values that I am interested in. 
-------------------------------------------------------------------------------------------
Univanaly_K.py

Take the sum of each potassium peak, subtract background, normalize data, take the sum of both peaks and plot against the Chemcam team's results.
-------------------------------------------------------------------------------------------
Univanaly_Na.py

Same as potassium for Na instead.
-------------------------------------------------------------------------------------------
K-File.py

Realized there's a more efficient way of analyzing. Create an x and y axis, out put those values to a csv so i can plot without having to wait 20 minutes per computation...
-------------------------------------------------------------------------------------------
FitK-Log.py

Take the scatter plot of K peak vs K moc values and fit a log curve.
-------------------------------------------------------------------------------------------
FitK-Log.py

Take the scatter plot of K peak vs K moc values and fit a linear curve.
-------------------------------------------------------------------------------------------
FitK.py

Take the scatter plot of K peak vs K moc values and fit a SQRT curve.
-------------------------------------------------------------------------------------------
FitNa-Lin.py

Take the scatter plot of Na peak vs Na moc values and fit a line.
-------------------------------------------------------------------------------------------


