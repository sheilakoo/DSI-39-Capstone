# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Capstone: Mastering the Art of Spinning

### Problem Statement 
Spin is an increasingly popular workout across the globe. It is a great way to improve your physical and mental health, and to look and feel your best. However, some are resistant to try it as they find the complexity intimidating. For those who tried, or even those who have been spinning for years, it can be challenging to catch the beat while getting the choreography right.

On a sombre note, some who were unable to withstand the intensity of spin have experienced rhabdomyolysis, a breakdown of muscle from extreme physical exertion, which can cause kidney failure and death. In 2021, Khoo Teck Puat Hospital saw 27 cases of rhabdomyolysis in the first 4 months; in March the same year, 5 were admitted to Changi General Hospital for spin-induced rhabdomyolysis (SingHealth, 2021). This calls for the urgent need to address the issue.

Hence, I am embarking on this project to create a machine learning model that predicts:

1. Whether the rider is **doing the choreography correctly**
2. Whether the rider is **riding on the beat**

so as to:
* Help amateurs **get the moves right** and ensure they **ride on the beat**
* Alleviate risk of rhabdomyolysis by enabling riders to **practice at their own pace**
* **Encourage more people to spin** and maximise the plethora of benefits it offers

### Methodology
I recorded four videos of myself performing each choreography move respectively: regular, pulse, push, and sexy corners. Each class consists of each choreography move performed to a single verse and chorus of the Backstreet Boys song "I Want It That Way." This consistent structure minimises tempo variations and ensures similar data sizes between classes. 

Using Mediapipe, I captured the coordinates of the landmarks in these videos, enabling detailed analysis of my movements and performance. I also used Librosa to extract the tempo and beat times. 

The coordinates were used to determine the correctness of the choreography move while the timestamps of the moves and beat times were compared to determine whether the rider is cycling to the beat.

### Data Dictionary
| Column | Data type | Description
|:--------:|:-------:|:-------:|
| `prompts` | string | the choreo move prompted by the game |
| `choreo_results` | boolean | the binary outcome of whether `choreo` matches with `prompts` (0: correct, 1: incorrect)|
| `angle_RIGHT_SHOULDER` | float | the hip-shoulder-elbow angle |
| `angle_RIGHT_ELBOW` | float | the shoulder_elbow_wrist angle |
| `beat_times` | float | the timestamp of the audio beats |
| `time_diff` | float | the time difference between the right heel's minima/maxima and their closest beat_time |

### Conclusion
* Difficult to identify relative minima and maxima. More effective methods could be explored.
* The choreography portion was significantly more successful while the tempo portion was crippled by the lack of data and class imbalance.
* Despite high model scores, the predictions for choreo moves tend to be wrong in the deployment likely due to similar coordinate ranges.
* This study might be ‘one-sided’ as majority of datasets are coordinates.

### Recommendations
* Increase complexity (e.g. train model with different songs or longer duration of the same song, add more moves, film from different angles)
* Include more poor examples (e.g. more off-beat data to minimize class imbalance)
* Use sensors for more accurate movement readings
* Explore other features apart from coordinates (e.g. average speed of the rider, resistance of the bike)

