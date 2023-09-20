## Table of Contents
1. [Project title](#project-title)
2. [Project introduction](#project-introduction)
   - 2.1. [Overview](#overview)
   - 2.2. [Context and Objectives](#context-and-objectives)
3. [Dataset description](#dataset-description)
   - 3.1. [Experiment Configuration](#experiment-configuration)
   - 3.2. [Recording Methodology](#recording-methodology)
   - 3.3. [Download the Dataset](#download-the-dataset)
   - 3.4. [Contributing](#contributing)
4. [Event Codes](#event-codes)
   - 4.1. [Each Class](#each-class)
   - 4.2. [Start and End of the Experiment](#start-and-end-of-the-experiment)
   - 4.3. [Channel Labels](#channel-labels)

## 1. Project title
Robust Decoding of Multi-class Imagined Classification

## 2. Project Introduction
### 2.1. **Overview**

EEG recordings captured the imagined vocalization of five distinct speech words/phrases. There's a total of 350 trials, with 70 trials for each class. Out of these, 60 trials per class are designated for training and 10 trials per class for validation. The testing data, comprising 10 trials for each class, will be disseminated in the future. The data has been segmented according to the cues provided (event markers).

### 2.2. **Context and Objectives**

The primary objective of this research is to **achieve reliable classification of multiple imagined speech classes**. The imagined vocalizations correspond to five essential communication words/phrases: ‘hello’, ‘help me’, ‘stop’, ‘thank you’, and ‘yes’. Throughout the study, participants were comfortably positioned in a chair, facing a 24-inch LCD display. They were guided to vividly imagine pronouncing the provided word as if they were actually verbalizing it, ensuring no physical movement or sound production. Participants were strictly advised to focus only on the given task and not engage in any other cognitive activities. Furthermore, they were cautioned to remain still and minimize eye blinks during both the imagination phase and cue reception. During all imagination trials, participants only saw a black screen, ensuring no external stimuli interfered with their brain activity.

## 3. Dataset description
### 3.1. **Experiment Configuration**

Auditory prompts of the five words/phrases played for 2 seconds, succeeded by a cross mark displayed for a duration between 0.8-1.2 seconds. As the cross mark vanished, participants commenced their imagined vocalization. This cycle of the cross mark display and imagined speech was repeated four times for each randomized cue. Following this, a 3-second relaxation period was allocated, allowing participants to reset before the next prompt.

### 3.2. **Recording Methodology**

EEG data collection was facilitated by a BrainAmp EEG signal amplifier, produced by BrainProduct GmbH, Germany. The data was captured using the BrainVision software and processed using MATLAB 2019a. Recording was done using 64 EEG electrodes based on the 10-20 international setup. The grounding and reference electrodes were situated at Fpz and FCz respectively, and the impedance between the sensors and the participants' scalp was consistently kept below 15 kΩ.

### 3.3. **Download the Dataset**

To obtain the EEG Imagined Speech Dataset, click on the link below:

[Download EEG Imagined Speech Dataset](https://drive.google.com/drive/folders/1SB5yMIoxsRS42cfKpZC3lXvxJNvGhn2k?usp=drive_link)

Please make sure to cite our work or give appropriate credits if you utilize the dataset for your research or any other purposes.

### 3.4. **Contributing**

If you'd like to contribute to this dataset or have any suggestions, please open an issue or submit a pull request.

## 4. Event Codes

### 4.1. Each Class

| Class     | Event Code |
|-----------|------------|
| Hello     | 1          |
| Help me   | 2          |
| Stop      | 3          |
| Thank you | 4          |
| Yes       | 5          |

### 4.2. Start and End of the Experiment (a Whole Session)

| Class | Event Code |
|-------|------------|
| Start | 13         |
| End   | 14         |

## 4.3. Channel Labels

| Channel No. | Channel Label | Channel No. | Channel Label | Channel No. | Channel Label | Channel No. | Channel Label |
|-------------|---------------|-------------|---------------|-------------|---------------|-------------|---------------|
| 1           | Fp1           | 16          | T8            | 31          | O2            | 46          | FT10          |
| 2           | Fp2           | 17          | TP9           | 32          | PO10          | 47          | C5            |
| 3           | F7            | 18          | CP5           | 33          | AF7           | 48          | C1            |
| 4           | F3            | 19          | CP1           | 34          | AF3           | 49          | C2            |
| 5           | Fz            | 20          | CP2           | 35          | AF4           | 50          | C6            |
| 6           | F4            | 21          | CP6           | 36          | AF8           | 51          | TP7           |
| 7           | F8            | 22          | TP10          | 37          | F5            | 52          | CP3           |
| 8           | FC5           | 23          | P7            | 38          | F1            | 53          | CPz           |
| 9           | FC1           | 24          | P3            | 39          | F2            | 54          | CP4           |
| 10          | FC2           | 25          | Pz            | 40          | F6            | 55          | TP8           |
| 11          | FC6           | 26          | P4            | 41          | FT9           | 56          | P5            |
| 12          | T7            | 27          | P8            | 42          | FT7           | 57          | P1            |
| 13          | C3            | 28          | PO9           | 43          | FC3           | 58          | P2            |
| 14          | Cz            | 29          | O1            | 44          | FC4           | 59          | P6            |
| 15          | C4            | 30          | Oz            | 45          | FT8           | 60          | PO7           |




