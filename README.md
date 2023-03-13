# Problem Description:
My roomates always ask me to stream my tinder account on the living room tv. However, the hdmi cord is really short and I don't like sitting so close to the tv.

# Solution:
Rather than my roomates telling me to swipe left or right, they can tell the computer. 

# tinder_swiper.py:
opens up tinder in browser and creates a gui using pysimplegui. The gui shows when the mic is listening for input and what the speech recognizer thinks the last input was.
The speech recognizer listens for phrases with a max duration of 3 seconds. Hearing a phrase with the word 'left' in it will make it dislike the profile, 'right' to like the profile, and 'more' to see more photos of the profile.

# size_change.py:
Used to resize photos for the simple gui


