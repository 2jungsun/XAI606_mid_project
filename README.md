## Table of Contents
1. [Project title](#project-title)
2. [Project introduction](#project-introduction)
   - [Overview](#overview)
   - [Context and Objectives](#context-and-objectives)
3. [Dataset description](#dataset-description)
   - [Experiment Configuration](#experiment-configuration)
   - [Recording Methodology](#recording-methodology)
   - [Download the Dataset](#download-the-dataset)
   - [Contributing](#contributing)

## Project title
Robust Decoding of Multi-class Imagined Classification

## Project introduction
### **Overview**

EEG recordings captured the imagined vocalization of five distinct speech words/phrases. There's a total of 350 trials, with 70 trials for each class. Out of these, 60 trials per class are designated for training and 10 trials per class for validation. The testing data, comprising 10 trials for each class, will be disseminated in the future. The data has been segmented according to the cues provided (event markers).

### **Context and Objectives**

The primary objective of this research is to **achieve reliable classification of multiple imagined speech classes**. The imagined vocalizations correspond to five essential communication words/phrases: ‘hello’, ‘help me’, ‘stop’, ‘thank you’, and ‘yes’. Throughout the study, participants were comfortably positioned in a chair, facing a 24-inch LCD display. They were guided to vividly imagine pronouncing the provided word as if they were actually verbalizing it, ensuring no physical movement or sound production. Participants were strictly advised to focus only on the given task and not engage in any other cognitive activities. Furthermore, they were cautioned to remain still and minimize eye blinks during both the imagination phase and cue reception. During all imagination trials, participants only saw a black screen, ensuring no external stimuli interfered with their brain activity.

## Dataset description
### **Experiment Configuration**

**Auditory prompts** of the five words/phrases played for 2 seconds, succeeded by a cross mark displayed for a duration between 0.8-1.2 seconds. As the cross mark vanished, participants commenced their imagined vocalization. This cycle of the cross mark display and imagined speech was repeated four times for each randomized cue. Following this, a 3-second relaxation period was allocated, allowing participants to reset before the next prompt.

### **Recording Methodology**

**EEG data collection** was facilitated by a BrainAmp EEG signal amplifier, produced by BrainProduct GmbH, Germany. The data was captured using the BrainVision software and processed using MATLAB 2019a. Recording was done using 64 EEG electrodes based on the 10-20 international setup. The grounding and reference electrodes were situated at Fpz and FCz respectively, and the impedance between the sensors and the participants' scalp was consistently kept below 15 kΩ.

### **Download the Dataset**

To obtain the EEG Imagined Speech Dataset, click on the link below:

[Download EEG Imagined Speech Dataset](https://drive.google.com/drive/folders/1SB5yMIoxsRS42cfKpZC3lXvxJNvGhn2k?usp=drive_link)

Please make sure to cite our work or give appropriate credits if you utilize the dataset for your research or any other purposes.

### **Contributing**

If you'd like to contribute to this dataset or have any suggestions, please open an issue or submit a pull request.
