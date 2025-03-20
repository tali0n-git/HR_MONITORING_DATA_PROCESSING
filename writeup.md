## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

[ANS: We may have missing values because of the device itself having trouble taking a detectable BPM. Filtering out these values risks showing an inaccurate distribution of the data because, instead of having data for every 5 minutes of wear, it will instead be shifted over an additional 5 minutes for every missing value. It may also result in odd jumps in the line graph when plotted!]

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

[ANS: Phase0 has a maximum of 93 BPM, the lowest of all 4 phases. However, it shows an average of 64.59 BPM which is higher than Phase3's (of 60.65 BPM). Looking at the plotted data it becomes more clear that Phase3 has a more consistent looking pattern of low BPMs. (The peaks in this graph may be due to movement during sleep). Therefore, I predict Phase3 to be the phase in which sleep is occuring.]

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings. 

[ANS: Phase2 has the highest maximum heart rate of all other phases. Its graph also hovers around its average value, 85.18 BPM which, although it is lower than Phase1's average, its higher standard deviation may contribute to this lower average. One possible reason for this widely varying spread of data in Phase2 could be that during exercise the device recording heart rates is having trouble getting an accurate reading. Therefore, Phase2 is most likely the phase in which exercise is occuring.]

## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

[ANS: Of the remaining phases (Phase0 and Phase1), Phase0 has the lowest average heartrate. However, Phase1 has the second lowest average heartrate and a higher standard deviation than Phase0, therefore the most likely phase where awake activity is occuring is in Phase1.]
