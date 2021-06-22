# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 11:23:20 2021

@author: Lorraine.Heilman
"""
# %matplotlib notebook
# imports
import matplotlib.pyplot as plt
import numpy, pandas, requests
from copy import deepcopy
## Elim's utilities for downloading and massaging data.
#  Since our focus is plotting, I embedded all my data handling in a separate script. 
#  If you have any questions on my script, feel free to contact me (Elim Thompson).
import myUtils

#%% get data from a station 
# Change the station or the date
station = '9410840'
begin_date, end_date = '20200625', '20200701'
content = myUtils.pull_obs (station, begin_date, end_date)

#%% get the data into a dataframe
dataframe = myUtils.massage_data (content, doPred=False)

#%% plot the data

# When you run this cell, it should generate a plot if you follow my previous steps.
dataframe.plot()
plt.close()

#%% Add labels and a title to the plot

axis = dataframe.plot ()
axis.set_xlabel ("Date time")
axis.set_ylabel ("Observed water level MLLW [meters]")
axis.set_title ('Water level at Santa Monica 9410840')

plt.close()

#%% reset tick labels
axis = dataframe.plot ()
axis.set_xlabel ("Date time")
axis.set_ylabel ("Observed water level MLLW [meters]")
axis.set_title ('Water level at Santa Monica 9410840')

## Remove the default x ticks
axis.set_xticks([],minor=True)

## Find the 12:00 index and set it as x ticks
is1200 = numpy.logical_and (dataframe.index.hour == 12, dataframe.index.minute == 0)
xticks = dataframe.index[numpy.where(is1200)]
axis.set_xticks (xticks)
plt.close()

#%% Modify the date-time in the x-axis

axis = dataframe.plot ()
axis.set_xlabel ("Date time")
axis.set_ylabel ("Observed water level MLLW [meters]")
axis.set_title ('Water level at Santa Monica 9410840')

## Remove the default x ticks and tick labels
axis.set_xticks([],minor=True)
axis.set_xticklabels([],minor=True)

## Set x ticks
is1200 = numpy.logical_and (dataframe.index.hour == 12, dataframe.index.minute == 0)
xticks = dataframe.index[numpy.where(is1200)]
axis.set_xticks (xticks)

## Set x tick labels
xticklabels = [dt.strftime ('%m-%d\n%H:%M') for dt in xticks]
axis.set_xticklabels (xticklabels, rotation=10)
plt.close()

#%% Add gridlines
axis = dataframe.plot (grid=True)
axis.set_xlabel ("Date time")
axis.set_ylabel ("Observed water level MLLW [meters]")
axis.set_title ('Water level at Santa Monica 9410840')

## Remove the default x ticks and tick labels
axis.set_xticks([],minor=True)
axis.set_xticklabels([],minor=True)

## Set x ticks
is1200 = numpy.logical_and (dataframe.index.hour == 12, dataframe.index.minute == 0)
xticks = dataframe.index[numpy.where(is1200)]
axis.set_xticks (xticks)

## Set x tick labels
xticklabels = [dt.strftime ('%m-%d\n%H:%M') for dt in xticks]
axis.set_xticklabels (xticklabels, rotation=10)
plt.close()

#%% Adjust figure size
axis = dataframe.plot (figsize=(10, 4), grid=True)
axis.set_xlabel ("Date time")
axis.set_ylabel ("Observed water level MLLW [meters]")
axis.set_title ('Water level at Santa Monica 9410840')

## Remove the default x ticks and tick labels
axis.set_xticks([],minor=True)
axis.set_xticklabels([],minor=True)

## Set x ticks
is1200 = numpy.logical_and (dataframe.index.hour == 12, dataframe.index.minute == 0)
xticks = dataframe.index[numpy.where(is1200)]
axis.set_xticks (xticks)

## Set x tick labels
xticklabels = [dt.strftime ('%m-%d\n%H:%M') for dt in xticks]
axis.set_xticklabels (xticklabels, rotation=10)
plt.close()

#%% Add a vertical line
axis = dataframe.plot (figsize=(10, 4), grid=True)
axis.set_xlabel ("Date time")
axis.set_ylabel ("Observed water level MLLW [meters]")
axis.set_title ('Water level at Santa Monica 9410840')

## Remove the default x ticks and tick labels
axis.set_xticks([],minor=True)
axis.set_xticklabels([],minor=True)

## Set x ticks
is1200 = numpy.logical_and (dataframe.index.hour == 12, dataframe.index.minute == 0)
xticks = dataframe.index[numpy.where(is1200)]
axis.set_xticks (xticks)

## Set x tick labels
xticklabels = [dt.strftime ('%m-%d\n%H:%M') for dt in xticks]
axis.set_xticklabels (xticklabels, rotation=10)

## Add a vertical line 
axis.axvline (x=pandas.to_datetime ('2020-06-28 00:00'), color='red', linewidth=2.0, alpha=0.7, linestyle='--')
plt.close()

#%%  Zoom in to a specific time range

start, end = '2020-06-27 19:26', '2020-06-28 06:22'
subframe = dataframe.loc[start:end,:]

axis = subframe.plot (figsize=(8, 4), grid=True)
axis.set_xlabel ("Date time")
axis.set_ylabel ("Observed water level MLLW [meters]")
axis.set_title ('Water level at Santa Monica 9410840')

## Remove the default x ticks and tick labels
axis.set_xticks([],minor=True)
axis.set_xticklabels([],minor=True)

## Set x ticks at XX:00
is00 = subframe.index.minute == 0
xticks = subframe.index[numpy.where(is00)]
axis.set_xticks (xticks)

## Set x tick labels
xticklabels = [dt.strftime ('%m-%d\n%H:%M') for dt in xticks]
axis.set_xticklabels (xticklabels, rotation=10)
plt.close()

#%% Switch from plotting a line to a scatter plot

subframe = deepcopy (dataframe.loc[start:end,:])
subframe['datetime'] = subframe.index

axis = subframe.plot (kind='scatter', figsize=(8, 4), grid=True, x='datetime', y='observed')
axis.set_xlabel ("Date time")
axis.set_ylabel ("Observed water level MLLW [meters]")
axis.set_title ('Water level at Santa Monica 9410840')

## Remove the default x ticks and tick labels
axis.set_xticks([],minor=True)
axis.set_xticklabels([],minor=True)

## Set x ticks at XX:00
is00 = subframe.index.minute == 0
xticks = subframe.index[numpy.where(is00)]
axis.set_xticks (xticks)

## Set x tick labels
xticklabels = [dt.strftime ('%m-%d\n%H:%M') for dt in xticks]
axis.set_xticklabels (xticklabels, rotation=10)
plt.close()

#%% Now get predictions

station = '9410840'
begin_date, end_date = '20200625', '20200701'
content = myUtils.pull_pred (station, begin_date, end_date)

pred_df = myUtils.massage_data (content, doPred=True)
dataframe = dataframe.merge (pred_df, how='outer', left_index=True, right_index=True)

#%% Plot both observed and predict time-series on the same plot

axis = dataframe.plot (figsize=(10, 4), grid=True)
axis.set_xlabel ("Date time")
axis.set_ylabel ("Observed water level MLLW [meters]")
axis.set_title ('Water level at Santa Monica 9410840')

## Remove the default x ticks and tick labels
axis.set_xticks([],minor=True)
axis.set_xticklabels([],minor=True)

## Set x ticks
is1200 = numpy.logical_and (dataframe.index.hour == 12, dataframe.index.minute == 0)
xticks = dataframe.index[numpy.where(is1200)]
axis.set_xticks (xticks)

## Set x tick labels
xticklabels = [dt.strftime ('%m-%d\n%H:%M') for dt in xticks]
axis.set_xticklabels (xticklabels, rotation=10)
plt.close()

#%% Change line styles

axis = dataframe.plot (figsize=(10, 4), grid=True, alpha=0.8, style=['-', '--'])
axis.set_xlabel ("Date time")
axis.set_ylabel ("Observed water level MLLW [meters]")
axis.set_title ('Water level at Santa Monica 9410840')

## Remove the default x ticks and tick labels
axis.set_xticks([],minor=True)
axis.set_xticklabels([],minor=True)

## Set x ticks
is1200 = numpy.logical_and (dataframe.index.hour == 12, dataframe.index.minute == 0)
xticks = dataframe.index[numpy.where(is1200)]
axis.set_xticks (xticks)

## Set x tick labels
xticklabels = [dt.strftime ('%m-%d\n%H:%M') for dt in xticks]
axis.set_xticklabels (xticklabels, rotation=10)
plt.close()

#%% Change the colors

axis = dataframe.plot (figsize=(10, 4), grid=True, style=['-', '--'], color=['#d8b365', '#5ab4ac'])
axis.set_xlabel ("Date time")
axis.set_ylabel ("Observed water level MLLW [meters]")
axis.set_title ('Water level at Santa Monica 9410840')

## Remove the default x ticks and tick labels
axis.set_xticks([],minor=True)
axis.set_xticklabels([],minor=True)

## Set x ticks
is1200 = numpy.logical_and (dataframe.index.hour == 12, dataframe.index.minute == 0)
xticks = dataframe.index[numpy.where(is1200)]
axis.set_xticks (xticks)

## Set x tick labels
xticklabels = [dt.strftime ('%m-%d\n%H:%M') for dt in xticks]
axis.set_xticklabels (xticklabels, rotation=10)
plt.close()
#%% Plot residuals

# Add a new column 'residual' to dataframe 
#   residual = observed - predicted
dataframe['residual'] = dataframe.observed - dataframe.predicted

# Plot 3 data in 3 plots
axes = dataframe.plot (subplots=True, figsize=(10, 6), grid=True, style=['-', '--'], color=['#d8b365', '#5ab4ac', 'gray'])

axes[0].set_title ('Water level at Santa Monica 9410840')
is1200 = numpy.logical_and (dataframe.index.hour == 12, dataframe.index.minute == 0)
xticks = dataframe.index[numpy.where(is1200)]
xticklabels = [dt.strftime ('%m-%d\n%H:%M') for dt in xticks]

for axis in axes:
    axis.set_ylabel ("Water Level\nMLLW [m]")

    ## Remove the default x ticks and tick labels
    axis.set_xticks([],minor=True)
    axis.set_xticklabels([],minor=True)

    ## Set x ticks
    axis.set_xticks (xticks)
    
## Set x tick labels
axes[-1].set_xticklabels (xticklabels, rotation=10)
axes[-1].set_xlabel ("Date time")

plt.close()
#%% plot 3 data in 2 plots
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 6), sharex=True)

## Top Plot: Time-series
subframe = dataframe.drop (axis=1, columns=['residual'])
axis = subframe.plot (ax=axes[0], grid=True, style=['-', '--'], color=['#d8b365', '#5ab4ac'])

axis.set_xlabel ("")
axis.set_ylabel ("Water level\nMLLW [meters]")
axis.set_title ('Water level at Santa Monica 9410840')

axis.set_xticks([],minor=True)
axis.set_xticklabels([],minor=True)

is1200 = numpy.logical_and (dataframe.index.hour == 12, dataframe.index.minute == 0)
xticks = dataframe.index[numpy.where(is1200)]
axis.set_xticks (xticks)
    
## Bottom Plot: Residual
axis = dataframe.residual.plot (ax=axes[1], grid=True)
axis.set_ylabel ("Obs - Pred [m]")
axis.set_xlabel ("Date time")

axis.set_xticks([],minor=True)
axis.set_xticklabels([],minor=True)

is1200 = numpy.logical_and (dataframe.index.hour == 12, dataframe.index.minute == 0)
xticks = dataframe.index[numpy.where(is1200)]
axis.set_xticks (xticks)

xticklabels = [dt.strftime ('%m-%d\n%H:%M') for dt in xticks]
axis.set_xticklabels (xticklabels, rotation=10)
plt.close()

#%% plot 3 data in 1 plot wiht dual axes

axis = dataframe.plot (figsize=(8, 4), secondary_y=['residual'], grid=True,
                       style=['-', '--', '-'], color=['#d8b365', '#5ab4ac', 'gray'])

axis.set_xlabel ("Date time")
axis.set_ylabel ("Water level\nMLLW [meters]")
axis.set_title ('Water level at Santa Monica 9410840')

axis.set_xticks([],minor=True)
axis.set_xticklabels([],minor=True)

is1200 = numpy.logical_and (dataframe.index.hour == 12, dataframe.index.minute == 0)
xticks = dataframe.index[numpy.where(is1200)]
axis.set_xticks (xticks)

xticklabels = [dt.strftime ('%m-%d\n%H:%M') for dt in xticks]
axis.set_xticklabels (xticklabels, rotation=10)
axis.legend (loc='upper center')

axis.right_ax.set_ylabel ('Obs - Pred [m]')
axis.right_ax.set_ylim (-0.05, 2.5)
plt.show()
#%% done with plotting

#show all plots

print('Done plotting')


