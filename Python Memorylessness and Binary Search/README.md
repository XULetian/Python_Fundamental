# Problem 1: Avocados

Download the datafile named “avocados.csv” -- Retrieved from Kaggle (9/26/2018).  This data was downloaded from the Hass Avocado Board website in May of 2018 & compiled into a single CSV.

#### a)	Define a function that takes a variable name in the form of a string (e.g. “Total Volume”), reads into memory the values for that variable (but just that variable) and computes the mean using the statistics module.

mean_SM = readAndComputeMean_SM(“Total Volume”)

#### b)	Define a function that takes a variable name in the form of a string (e.g. “Total Volume”), reads into memory the values for that variable (but just that variable) and computes the standard deviation using the statistics module.

sd_SM = readAndComputeSD_SM(“Total Volume”)

#### c)	Define a function that takes a variable name in the form of a string (e.g. “Total Volume”), reads into memory the values for that variable (but just that variable) and computes the median using the statistics module.

median_SM = readAndComputeMedian_SM(“Total Volume”)

#### d)	Repeat a-c, but instead of using the statistics module write your own “homegrown” code to compute the mean, standard deviation and median.

mean_HG = readAndComputeMean_HG(“Total Volume”)
sd_HG = readAndComputeSD_HG(“Total Volume”)
median_HG = readAndComputeMedian_HG(“Total Volume”)

#### e)	Repeat a-c, but your functions must be memoryless – you can hold in memory only a single value from the file at any given time.   You may need to keep track of min, max, sum or a handful of counters.

mean_MML = readAndComputeMean_MML(“Total Volume”)
sd_MML = readAndComputeSD_MML(“Total Volume”)
median_MML = readAndComputeMedian_MML(“Total Volume”)

#### f)	Write test code to demonstrate that the means, standard deviations and medians are the same across all three techniques.
