import numpy as np

# video name / CHANGE EVERY TIME
a = "WIN20190302150545ProfromS34853aggressivestranger32weeksDLCresne"
# frames of the video
frames = a[:, 0]

# coordinates and likelihood of all dots
xn = a[:, 1]
yn = a[:, 2]
likenose = a[:, 3]

xc1 = a[:, 4]
yc1 = a[:, 5]
likec1 = a[:, 6]

xc2 = a[:, 7]
yc2 = a[:, 8]
likec2 = a[:, 9]

xc3 = a[:, 10]
yc3 = a[:, 11]
likec3 = a[:, 12]

xc4 = a[:, 13]
yc4 = a[:, 14]
likec4 = a[:, 15]

xc5 = a[:, 16]
yc5 = a[:, 17]
likec5 = a[:, 18]

xc6 = a[:, 19]
yc6 = a[:, 20]
likec6 = a[:, 21]

xc7 = a[:, 22]
yc7 = a[:, 23]
likec7 = a[:, 24]

xc8 = a[:, 25]
yc8 = a[:, 26]
likec8 = a[:, 27]

xtail = a[:, 28]
ytail = a[:, 29]
liketail = a[:, 30]

# distances from nose to circle
dnc1nose = np.sqrt((xn - xc1) ** 2 + (yn - yc1) ** 2)
dnc2nose = np.sqrt((xn - xc2) ** 2 + (yn - yc2) ** 2)
dnc3nose = np.sqrt((xn - xc3) ** 2 + (yn - yc3) ** 2)
dnc4nose = np.sqrt((xn - xc4) ** 2 + (yn - yc4) ** 2)
dnc5nose = np.sqrt((xn - xc5) ** 2 + (yn - yc5) ** 2)
dnc6nose = np.sqrt((xn - xc6) ** 2 + (yn - yc6) ** 2)
dnc7nose = np.sqrt((xn - xc7) ** 2 + (yn - yc7) ** 2)
dnc8nose = np.sqrt((xn - xc8) ** 2 + (yn - yc8) ** 2)

distancenose = np.column_stack((dnc1nose, dnc2nose, dnc3nose, dnc4nose, dnc5nose, dnc6nose, dnc7nose, dnc8nose))

# distance from tail to circle
dnc1tail = np.sqrt((xtail - xc1) ** 2 + (ytail - yc1) ** 2)
dnc2tail = np.sqrt((xtail - xc2) ** 2 + (ytail - yc2) ** 2)
dnc3tail = np.sqrt((xtail - xc3) ** 2 + (ytail - yc3) ** 2)
dnc4tail = np.sqrt((xtail - xc4) ** 2 + (ytail - yc4) ** 2)
dnc5tail = np.sqrt((xtail - xc5) ** 2 + (ytail - yc5) ** 2)
dnc6tail = np.sqrt((xtail - xc6) ** 2 + (ytail - yc6) ** 2)
dnc7tail = np.sqrt((xtail - xc7) ** 2 + (ytail - yc7) ** 2)
dnc8tail = np.sqrt((xtail - xc8) ** 2 + (ytail - yc8) ** 2)

distancetail = np.column_stack((dnc1tail, dnc2tail, dnc3tail, dnc4tail, dnc5tail, dnc6tail, dnc7tail, dnc8tail))

# minimum distance that is found between nose and a circle and plot
Mnose = np.min(distancenose, axis=1)
# plot(frames, Mnose)

# minimum distance that is found between tail and a circle and plot
Mtail = np.min(distancetail, axis=1)
# plot(frames, Mtail)

# removal of values we do not want while still keeping the original index
compact = np.column_stack((frames, Mnose, likenose))
compact2 = np.column_stack((frames, Mtail, liketail))

# Circle likelihoods all in one thing
circlelike = np.column_stack((frames, likec1, likec2, likec3, likec4, likec5, likec6, likec7, likec8))

# if nose distance is greater than tail distance make the distance zero
for i in range(frames.shape[0]):
    if compact[i, 1] > compact2[i, 1]:
        compact[i, 1] = 0
    if np.any(circlelike[:, 1:] < 0.1):
        compact[i, 1] = 0
    if np.any(compact2[:, 2] < 0.1):
        compact[i, 1] = 0

# removing labels that have low possibility of being there
Findnose = compact[:, 2] < 0.10  # find all cases where the nose likelihood is less than 0.1
compact = compact[~Findnose]  # remove rows where the nose likelihood is less than 0.1
# bar(compact[:, 0], compact[:, 1])  # plot of frames versus the minimum distance between nose and circle

FindThreshnose = compact[:, 1] > 30  # find values where the distance is greater than the value
compact = compact[~FindThreshnose]  # remove rows where the value is greater than the value
# bar(compact[:, 0], compact[:, 1])  # plot of frames versus minimum distance between nose and circle

takeawayzero = compact[:, 1] == 0
compact = compact[~takeawayzero]
# bar(compact[:, 0], compact[:, 1])

# turning remaining frames into a time in order to determine the amount of social time.
timeoftotalvidsec = 554  # NEEDS TO BE CHANGED EVERY TIME
interactStartSec = 50  # NEEDS TO BE CHANGED EVERY TIME
framespersec = frames.shape[0] / timeoftotalvidsec
socialtime = compact.shape[0] / framespersec

timetosec = compact[:, 0] / framespersec
beforeInteraction = timetosec < interactStartSec  # find values where the distance is greater than the value
compact = compact[~beforeInteraction]
timetosec = timetosec[~beforeInteraction]

import matplotlib.pyplot as plt

plt.figure(1)
plt.bar(timetosec, compact[:, 1])
plt.title("Interaction Distance")
plt.xlabel("Time (s)")
plt.ylabel("Distance (pixels)")

fig = plt.figure(3)
times = compact[:, 0]
prev = times[0]
bars = []
prevBlock = 0
counter = 0
for idx in range(1, len(times)):
    val = times[idx]
    if val - prev <= 1:
        counter += 1
        prev = val
        prevBlock = 0
    else:
        if counter > 0:
            bars.append(counter / framespersec)
        if prevBlock == 0:
            bars.append((val - prev) / framespersec)
            prevBlock = 1
        else:
            bars.extend([1 / framespersec, (val - prev) / framespersec])

        prev = val
        counter = 0

bars = [interactStartSec] + bars

plt.barh([1], bars, 'stacked', edgecolor='none')

colors = np.zeros((len(bars)-1, 3))
interactions = np.zeros(len(bars))

if times[2] - times[1] > 1:
    flipper = -1
else:
    flipper = 1

for idx in range(1, len(bars)):
    if flipper == 1:
        colors[idx-1] = [0, 0.4470, 0.7410]
        interactions[idx-1] = 1
    else:
        colors[idx-1] = [1, 1, 1]
        interactions[idx-1] = 0
    flipper *= -1

colors = np.concatenate(([1, 1, 1], colors))
colors = np.reshape(colors, (len(bars), 3))

plt.gca().set_ylim([0.6, 1.4])
plt.gca().set_xlim([interactStartSec, max(times) / framespersec])
fig.set_position([10, 10, 560, 125])
plt.gca().set_yticklabels([])
plt.gca().set_xticklabels([50 * round(interactStartSec / 50):50:(timeoftotalvidsec-50)])
plt.title("Interacting Time")
plt.xlabel("Time (s)")

timeStamps = np.zeros(len(bars)-1)
curTime = bars[0]
for idx in range(1, len(bars)):
    timeStamps[idx-1] = curTime
    curTime += bars[idx]

stampsAndInteractions = np.column_stack((timeStamps, interactions))
np.savetxt('interactions.csv', stampsAndInteractions, delimiter=',')

Results = np.column_stack((timetosec, compact[:, 1]))
