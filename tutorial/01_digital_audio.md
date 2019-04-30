## Digital audio

```
import matplotlib.pyplot as plt
import numpy as np
import soundfile
```


### Generating sine waves

To create 1 cycle of a sine wave, we need to move a hand around 
a clock in small increments (whose size is determined by the 
sampling rate we are using) and evaluate the sine function of the 
angle between the moving hand and a fixed hand pointing to 3 o'clock,
as illustrated here:

 https://upload.wikimedia.org/wikipedia/commons/3/3b/Circle_cos_sin.gif

 (See also Peter Ladefoged "Elements of Acoustic Phonetics", 2nd ed., pp.152-4) 
 
The measure of angle we will use will be radians rather than degrees.
Instead of counting 1 cycle as 360 degrees, we will count it as 2π
radians. This is explained visually here:

https://en.wikipedia.org/wiki/Radian#/media/File:Circle_radians.gif

First we create array of 100 increments between 0 and 2π, 
i.e. 1 cycle expressed in radians sampled 100 times, then we take 
the sign of each of these angles to get our waveform values y:

```
x = np.linspace(0, 2*np.pi, 100) 
y = np.sin(x)
plt.plot(x, y) 
plt.show()    
```

Note that we don't need to wrap back to 0 to start a new cycle after this,
i.e. sin(2π + 0.1) = sin(0.1). So we can just keep increasing our x values.
So to make 2 cycles:


```
x = np.linspace(0, 2*np.pi * 2, 100) 
y = np.sin(x)
plt.plot(x, y) 
plt.show()    
```


So far the units on the x axis are position in cycle in radians. Let's 
start to think in terms of time values instead. Instead of plotting a 
given number of cycles, let's plot a given number of cycles per second (e.g. 50Hz)
for a certain number of seconds (e.g. 1), at a given sampling rate (e.g. 16000Hz):

```
x = np.linspace(0, 2*np.pi * 50 * 1, 16000*1) 
y = np.sin(x)
plt.plot(x, y) 
plt.show()    
```

Let's do the same again, this time adding times to the x axis, and adding variables
so we can start to generalise to different frequencies, sample rates and durations:

```
sine_hz = 50
sample_rate_hz = 16000
duration_seconds = 1

x_in_radians = np.linspace(0, 2*np.pi * sine_hz * duration_seconds, sample_rate_hz*duration_seconds) 
x_in_seconds = np.linspace(0, duration_seconds, sample_rate_hz*duration_seconds)
y = np.sin(x_in_radians)
plt.plot(x_in_seconds, y) 
plt.show()    
```

Make it into 2 functions:

```
def get_sine(sine_hz, duration_seconds, sample_rate_hz):
    x_in_radians = np.linspace(0, 2*np.pi * sine_hz * duration_seconds, sample_rate_hz*duration_seconds) 
    y = np.sin(x_in_radians)
    return y
    
def get_time_axis(sine_hz, duration_seconds, sample_rate_hz):
    x_in_seconds = np.linspace(0, length_in_seconds, sample_rate_hz*duration_seconds)
    return x_in_seconds
    
```

Generate a sine wave and write to file:

```
sinewave = get_sine(200, 5, 16000)
soundfile.write('/tmp/sine_100_5.wav', sinewave, 16000)
```

Generate a mixture of sine waves and write to file:

```
sinewave = get_sine(200, 5, 16000) + get_sine(300, 5, 16000)
soundfile.write('/tmp/sine_100_5.wav', sinewave, 16000)
```

Generate complex waveform with phantom fundamental and single tone with
same fundamental (see Ladefoged p.76):

```
sr = 16000
soundfile.write('/tmp/phantom.wav', get_sine(1800, 5, sr) + get_sine(2000, 5, sr) + get_sine(2200, 5, sr), sr)
soundfile.write('/tmp/singletone.wav', get_sine(200, 5, sr), sr)
```

Scale relative amplitudes of the components:
```
soundfile.write('/tmp/phantom2.wav', get_sine(1800, 5, sr)*1.0 + get_sine(2000, 5, sr)*0.5 + get_sine(2200, 5, sr)*0.1, sr)
```

Make a version with 2 components, with the first one fading in over time:

```
ramp = np.linspace(0,1,5*sr)
soundfile.write('/tmp/sine.wav', get_sine(1800, 5, sr)*ramp + get_sine(2000, 5, sr), sr)
```

### Loading data from files

Read the audio contained in this file to a Numpy array:

```
wave, samplerate = read('./data/hvd_181.wav')

```


The array containing the waveform samples can be manipulated like any other Numpy array. For example, we can find out how long the sentence is (in samples, i.e. array elements):

```
print len(wave)
```


Access samples 2000 - 2100:
```
print wave[2000:2100]
```


To manipulate the data in a more intuitive way, we need to use sampling rate metadata to convert from samples to e.g. times in seconds.   How long is the sentence in seconds?

```
print len(wave) / samplerate
```


Plot a 0.2 second section starting 1.5 seconds into the audio:

```
start = int(1.5 * samplerate)
end = int((1.5 + 0.2) * samplerate)
print wave[start:end]
```

Plot the waveform:

```
plt.plot(wave) 
plt.show()
```

Fade in and out over time (1 second each) by scaling the samples:

```
sr = samplerate
ramp_in = np.linspace(0,1,1.0*sr) 
ramp_out = np.linspace(1,0,1.0*sr) 
wave[:int(1.0*sr)] *= ramp_in
wave[int(-1.0*sr):] *= ramp_out
soundfile.write('/tmp/ramped_wave.wav', wave, sr)
```

What happens if we very naively try to double the length of the audio by
simply repeating each sample?

```
wave, sr = soundfile.read('./data/hvd_181.wav')
wave = np.repeat(wave, 2)
soundfile.write('/tmp/repeated_wave.wav', wave, sr)
```

How about taking every second, third, etc. sample?

<!--
wave, sr = soundfile.read('./data/hvd_181.wav')
wave = wave[::2]
soundfile.write('/tmp/decimated_wave.wav', wave, sr)
-->

Are these useful manipulations? If not, what are the problems with them?

What other interesting manipulations can you come up with?



