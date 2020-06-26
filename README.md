# KalimbaNoteToTabsConverter

## Input: kalimba notes to folder notes with formated name
### song_name-kalimba_type-kalimba_setting
#### Example:
- song_name: lavien_rose
- kalimba_type: K17CAS
- setting: 2
- we have a file_name: lavien_rose-K17CAS-2

## Settings: kalimba tab config in config folder
#### example: k17cas
### tab order
#### [9,8,10,7,11,6,12,5,13,4,14,3,15,2,16,1,17]
### tuned settings: you set the setting in songname by select the index of column here
### Ex: lavien_rose song use the key setting like 2°°.. so the option is 2
#### C6# D6  2°° 2'' 2"
#### A5# B5  7°  7'  7'
#### F5# G5  5°  5'  5'
#### D5# E5  3°  3'  3'
#### B4  C5  1°  1'  1'
#### G4# A4  6   6   6
#### E4  F4  4   5   5
#### C4# D4  2   2   2
#### B3  C4  1   1   1
#### D4# E4  3   3   3
#### F4# G4  5   5   5
#### A4# B4  7   7   7
#### C5# D5  2°  2'  2'
#### E5  F5  4°  4'  4'
#### G5# A5  6°  6'  6'
#### B5  C6  1°° 1'' 1"
#### D6# E6  3°° 3'' 3"

## RUN: just double click convert.py (just require python setup only)

## Output: tabs like map in text (i'm working on export image of tab, please wait for next improvement :p)
#### [0, 0, 0, 0, 0, 0, 0, 0, [0], 1, 0, 0, 0, 0, 0, 0, 0]
#### [0, 0, 0, 0, 0, 0, 0, 0, [0], 0, 1, 0, 0, 0, 0, 0, 0]
#### [0, 0, 0, 0, 0, 1, 0, 0, [1], 0, 0, 0, 0, 0, 0, 0, 0]
#### [0, 0, 0, 0, 0, 0, 0, 0, [0], 0, 0, 1, 0, 0, 0, 0, 0]
#### [0, 0, 0, 0, 0, 0, 0, 0, [0], 1, 0, 0, 0, 0, 0, 0, 0]
#### [0, 0, 0, 0, 1, 0, 0, 0, [1], 0, 0, 0, 0, 0, 0, 0, 0]

# Enjoy :p
