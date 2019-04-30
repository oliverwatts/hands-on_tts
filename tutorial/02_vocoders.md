## General audio


https://github.com/r9y9/nnmnkwii_gallery/tree/master/notebooks



pip install parselmouth


https://github.com/r9y9/pysptk/blob/master/examples/Speech%20analysis%20and%20re-synthesis.ipynb




phil garner vocoding: http://online.kitp.ucsb.edu/online/hearing17/garner/
phil garner prosody: http://online.kitp.ucsb.edu/online/hearing17/garner2/rm/jwvideo.html



Start a Python session:

<!-- source ~/tool/virtual_python/handson_tts/bin/activate -->

```
import pyworld
from playsound import playsound as play
import pyworld as pw
from soundfile import read, write
import pylab 
from __future__ import division  ## use floating point division by default
import numpy as np

def playwave(wave):
    play('')
```

The file ... contains a sentence which you can listen to like this:

```
play('./data/hvd_181.wav')
```

Read the audio contained in this file to a Numpy array:

```
waveform, samplerate = read('./data/hvd_181.wav')

```


The array containing the waveform samples can be manipulated like any other Numpy array. For example, we can find out how long is the sentence in samples?

```
print len(waveform)
```

SINGLE CHANNEL

Access samples 2000 - 2100:
```
print waveform[2000:2100]
```


To manipulate the data in a more intuitive way, we need to use sampling rate metadata to convert from samples to e.g. times in seconds.   How long is the sentence in seconds?

```
print len(waveform) / samplerate
```


Plot a 0.2 second section starting 1.5 seconds into the audio:

```
start = int(1.5 * samplerate)
end = int((1.5 + 0.2) * samplerate)
print waveform[start:end]
```






Plot the waveform:

```
pylab.plot(waveform)
pylab.show()
```

CUT AND PASTE - NOTE PERIOD

ECHO - CONVOLUTION, FIR, ROOM IR

WRITING

SINE WAVE

PULSE TRAIN FROM F0

## Vocoders

We will experiment with the open-source vocoder World [REF]. Specifically,
we will use a version of that tool with Python bindings, `pyworld`.

Extract vocoder features from an example audio file using default parameters:


f0, sp, ap = pw.wav2world(x, fs, frame_period=20)    # use default options
y = pw.synthesize(f0, sp, ap, fs, 20)
sf.write('/tmp/b.wav', y, 16000)
ps('/tmp/b.wav')



```
waveform, samplerate = read('./data/hvd_181.wav')
f0, sp, ap = pyworld.wav2world(waveform, samplerate)
y = pyworld.synthesize(f0, sp, ap, samplerate)
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')
```

Mismatched frame rates? Mismatched sample rates?


Manipulations: hoarse; F0 manip

```
y = pyworld.synthesize(np.ones_like(f0)*300, sp, ap, samplerate)
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')
```

```
y = pyworld.synthesize(np.ones_like(f0)*40, sp, ap, samplerate)
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')
```

```
y1 = pyworld.synthesize(np.ones_like(f0)*600, sp, ap, samplerate)
y2 = pyworld.synthesize(np.ones_like(f0)*280, sp, ap, samplerate)
y = y1+y2
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')

y1 = pyworld.synthesize(np.ones_like(f0)*600, sp, ap, samplerate)
y2 = pyworld.synthesize(np.ones_like(f0)*75, sp, ap, samplerate)
y = y1+y2
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')
```



<!-- In music, an interval ratio is a ratio of the frequencies of the pitches in a musical interval. For example, a just perfect fifth (for example C to G) is 3:2 ( Play (help. ... If the A above middle C is 440 Hz, the perfect fifth above it would be E, at (440*1.5=) 660 Hz, while the equal tempered E5 is 659.255 Hz.

    https://www.johndcook.com/blog/2016/02/10/musical-pitch-notation/

    https://newt.phys.unsw.edu.au/jw/notes.html
 -->

```
y1 = pyworld.synthesize(np.ones_like(f0)*100, sp, ap, samplerate)
y2 = pyworld.synthesize(np.ones_like(f0)*150, sp, ap, samplerate)
y = y1+y2
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')

y1 = pyworld.synthesize(np.ones_like(f0)*100/1.5, sp, ap, samplerate)
y2 = pyworld.synthesize(np.ones_like(f0)*150/1.5, sp, ap, samplerate)
y = y1+y2
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')
```






```
y1 = pyworld.synthesize(f0, sp, ap, samplerate)
y2 = pyworld.synthesize(f0*1.5, sp, ap, samplerate)
y = y1+y2
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')

y1 = pyworld.synthesize(f0 * 2.0, sp, ap, samplerate)
y2 = pyworld.synthesize((f0*1.5) * 2.0, sp, ap, samplerate)
y = y1+y2
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')

```


f0_sweep = np.linspace(20,500,len(f0))
f0_sweep[f0==0.0] = 0.0
y = pyworld.synthesize(f0_sweep, sp, ap, samplerate)
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')


f0_sweep = np.linspace(500,20,len(f0))
f0_sweep[f0==0.0] = 0.0
y = pyworld.synthesize(f0_sweep, sp, ap, samplerate)
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')



y = pyworld.synthesize(np.zeros_like(f0), sp, ap, samplerate)
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')


voiced_sp = sp[f0>0.0, :]
mean_sp = np.tile(voiced_sp.mean(axis=0), (len(sp), 1))
y = pyworld.synthesize(f0, mean_sp, ap, samplerate)
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')



repeat single sp frame:



rep_sp = np.tile(sp[200,:], (len(sp), 1))
y = pyworld.synthesize(f0, rep_sp, ap, samplerate)
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')


## no ap:

y = pyworld.synthesize(f0, sp, np.zeros_like(ap), samplerate)
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')


y = pyworld.synthesize(f0, sp, ap, samplerate)
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')




manip range of F0

mean_f0 = f0[f0>0.0].mean()
std_f0 = f0[f0>0.0].std()

f0_standardised = (f0 - mean_f0) / std_f0
f0_scaled = f0_standardised * 2
f0_scaled = (f0_scaled * std_f0) + mean_f0
y = pyworld.synthesize(f0_scaled, sp, ap, samplerate)
write('./data/resynth_01.wav', y, samplerate)
play('./data/resynth_01.wav')




Break pipeline down: --

```
_f0, t = pyworld.dio(waveform, samplerate, f0_floor=50.0, f0_ceil=600.0)
_sp = pw.cheaptrick(waveform, _f0, t, samplerate)
_ap = pw.d4c(waveform, _f0, t, samplerate)
_y = pw.synthesize(_f0, _sp, _ap, samplerate)
# librosa.output.write_wav('test/y_without_f0_refinement.wav', _y, fs)
write('./data/y_without_f0_refinement.wav', _y, samplerate)
play('./data/y_without_f0_refinement.wav')



_f0, t = pyworld.dio(waveform, samplerate, f0_floor=50.0, f0_ceil=600.0)
_f0_fix = np.ones_like(_f0) * 100


_sp = pw.cheaptrick(waveform, _f0_fix, t, samplerate)
_ap = pw.d4c(waveform, _f0_fix, t, samplerate)
_y = pw.synthesize(_f0, _sp, _ap, samplerate)
# librosa.output.write_wav('test/y_without_f0_refinement.wav', _y, fs)
write('./data/y_without_f0_refinement.wav', _y, samplerate)
play('./data/y_without_f0_refinement.wav')



_y = pw.synthesize(np.ones_like(_f0)*250, _sp, _ap, samplerate)
# librosa.output.write_wav('test/y_without_f0_refinement.wav', _y, fs)
write('./data/y_without_f0_refinement.wav', _y, samplerate)
play('./data/y_without_f0_refinement.wav')


```


### mel ceptrum

https://github.com/r9y9/nnmnkwii_gallery/blob/master/scripts/prepare_features.py





Why dependent on F0? Constant F0?






```






```

<!-- 

cd ~/tool/virtual_python/
virtualenv --distribute --python=/usr/bin/python2.7 handson_tts
source  ~/tool/virtual_python/handson_tts/bin/activate


pip install pyworld


(handson_tts) MacBook-Air:virtual_python owatts$ pip install pyworld
Collecting pyworld
  Could not fetch URL https://pypi.python.org/simple/pyworld/: There was a problem confirming the ssl certificate: [SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:590) - skipping

  # https://stackoverflow.com/questions/16370583/pip-issue-installing-almost-any-library
curl https://bootstrap.pypa.io/get-pip.py | python




pip install nnmnkwii

pip install soundfile
pip install matplotlib


pip install pyobjc  ## else playsound gives: ImportError: No module named AppKit
pip install playsound


from playsound import playsound -->



playsound('audio.mp3')

from playsound import playsound as ps
ps('/Users/owatts/data/cmu_us_awb_arctic/wav/arctic_a0007.wav')


import pyworld as pw
import soundfile as sf
sf.read('/Users/owatts/data/cmu_us_awb_arctic/wav/arctic_a0007.wav')
x, fs = sf.read('/Users/owatts/data/cmu_us_awb_arctic/wav/arctic_a0007.wav')


f0, sp, ap = pw.wav2world(x, fs)    # use default options
y = pw.synthesize(f0, sp, ap, fs, pw.default_frame_period)




>>> sf.write('/tmp/a.wav', y, 16000)
>>> f0 8 2
  File "<stdin>", line 1
    f0 8 2
       ^
SyntaxError: invalid syntax
>>> f0 *= 2
>>> y2 = pw.synthesize(f0, sp, ap, fs, pw.default_frame_period)
>>> sf.write('/tmp/b.wav', y2, 16000)
>>> ps('/tmp/a.wav')
>>> ps('/tmp/b.wav')








f0, sp, ap = pw.wav2world(x, fs, frame_period=12.5)    # use default options
y = pw.synthesize(f0, sp, ap, fs, 12.5)
sf.write('/tmp/b.wav', y, 16000)
ps('/tmp/b.wav')




    # 2. Step by step
    # 2-1 Without F0 refinement
    _f0, t = pw.dio(x, fs, f0_floor=50.0, f0_ceil=600.0,
                    channels_in_octave=2,
                    frame_period=args.frame_period,
                    speed=args.speed)
    _sp = pw.cheaptrick(x, _f0, t, fs)
    _ap = pw.d4c(x, _f0, t, fs)
    _y = pw.synthesize(_f0, _sp, _ap, fs, args.frame_period)
    # librosa.output.write_wav('test/y_without_f0_refinement.wav', _y, fs)
    sf.write('test/y_without_f0_refinement.wav', _y, fs)

    # 2-2 DIO with F0 refinement (using Stonemask)
    f0 = pw.stonemask(x, _f0, t, fs)
    sp = pw.cheaptrick(x, f0, t, fs)
    ap = pw.d4c(x, f0, t, fs)
    y = pw.synthesize(f0, sp, ap, fs, args.frame_period)
    # librosa.output.write_wav('test/y_with_f0_refinement.wav', y, fs)
    sf.write('test/y_with_f0_refinement.wav', y, fs)

    # 2-3 Harvest with F0 refinement (using Stonemask)
    _f0_h, t_h = pw.harvest(x, fs)
    f0_h = pw.stonemask(x, _f0_h, t_h, fs)
    sp_h = pw.cheaptrick(x, f0_h, t_h, fs)
    ap_h = pw.d4c(x, f0_h, t_h, fs)
    y_h = pw.synthesize(f0_h, sp_h, ap_h, fs, pw.default_frame_period)
    # librosa.output.write_wav('test/y_harvest_with_f0_refinement.wav', y_h, fs)
    sf.write('test/y_harvest_with_f0_refinement.wav', y_h, fs)

    # Comparison
    savefig('test/wavform.png', [x, _y, y])
    savefig('test/sp.png', [_sp, sp])
    savefig('test/ap.png', [_ap, ap], log=False)
    savefig('test/f0.png', [_f0, f0])

    print('Please check "test" directory for output files')
 -->






 ### Sequences of operations



import pyworld
from playsound import playsound as play
import pyworld as pw
from soundfile import read, write
import pylab 
from __future__ import division  ## use floating point division by default
import numpy as np
import librosa



play('./data/hvd_181.wav')

waveform, samplerate = read('./data/hvd_181.wav')

# linear spectrogram


<!-- from librosa.core.spectrum import power_to_db, _spectrogram


S, n_fft = _spectrogram(y=waveform, S=S, n_fft=n_fft, hop_length=hop_length,
                            power=power)

    # Build a Mel filter
    mel_basis = filters.mel(sr, n_fft, **kwargs)

    return np.dot(mel_basis, S)

 -->


# complex spectrum
linear = librosa.stft(y=waveform,
                      n_fft=2048,
                      hop_length=512,
                      win_length=2048)

# magnitude spectrogram
mag = np.abs(linear)  # (1+n_fft//2, T)

# mel spectrogram
mel_basis = librosa.filters.mel(samplerate, 2048, 1025)  # (n_mels, 1+n_fft//2)
mel = np.dot(mel_basis, mag)  # (n_mels, t)



# mel warped spectrogram


        S = power_to_db(melspectrogram(y=y, sr=sr, **kwargs))

    return scipy.fftpack.dct(S, axis=0, type=dct_type, norm=norm)[:n_mfcc]

# to cepstrum


https://w3.ual.es/~vruiz/Docencia/Apuntes/Coding/Image/00-Fundamentals/index.html#x1-100007



http://greenteapress.com/thinkdsp/thinkdsp.pdf
### DCT with matrix
http://greenteapress.com/thinkdsp/html/thinkdsp007.html