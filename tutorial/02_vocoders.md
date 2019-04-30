

## Vocoders



We will experiment with the open-source vocoder [World](https://pdfs.semanticscholar.org/560a/be3b4482335a93df309cb6a0185ccc3ebd8e.pdf). The original code can be found [here](https://github.com/mmorise/World), but we will use a version of that tool with Python bindings, [`pyworld`](https://github.com/JeremyCCHsu/Python-Wrapper-for-World-Vocoder). Please install with `pip`.

```
import pyworld
import soundfile
import pylab 
import numpy as np
```


Extract vocoder features from an example audio file using default parameters:


```
waveform, samplerate = soundfile.read('./data/hvd_181.wav')
f0, sp, ap = pyworld.wav2world(waveform, samplerate)
y = pyworld.synthesize(f0, sp, ap, samplerate)
soundfile.write('/tmp/resynth_01.wav', y, samplerate)
```

Can you hear the difference between original and resynthesised versions?

### Manipulation of fundamental frequency

Try some manipulations, e.g.: 

```
y = pyworld.synthesize(np.ones_like(f0)*300, sp, ap, samplerate)
soundfile.write('/tmp/resynth_01.wav', y, samplerate)
```

```
y = pyworld.synthesize(np.ones_like(f0)*40, sp, ap, samplerate)
soundfile.write('/tmp/resynth_01.wav', y, samplerate)
```


From [Wikipedia](https://en.wikipedia.org/wiki/Interval_ratio):
"In music, an interval ratio is a ratio of the frequencies of the pitches in a musical interval. For example, a just perfect fifth (for example C to G) is 3:2. If the A above middle C is 440 Hz, the perfect fifth above it would be E, at (440\*1.5=) 660 Hz, while the equal tempered E5 is 659.255 Hz."

   
```
y1 = pyworld.synthesize(np.ones_like(f0)*100, sp, ap, samplerate)
y2 = pyworld.synthesize(np.ones_like(f0)*150, sp, ap, samplerate)
y = y1+y2

y1 = pyworld.synthesize(np.ones_like(f0)*100/1.5, sp, ap, samplerate)
y2 = pyworld.synthesize(np.ones_like(f0)*150/1.5, sp, ap, samplerate)
z = y1+y2

combined = np.concatenate([y,z])
soundfile.write('/tmp/resynth_01.wav', combined, samplerate)
```




```
f0_sweep = np.linspace(20,500,len(f0))
f0_sweep[f0==0.0] = 0.0
y = pyworld.synthesize(f0_sweep, sp, ap, samplerate)

f0_sweep_down = np.linspace(500,20,len(f0))
f0_sweep_down[f0==0.0] = 0.0
y2 = pyworld.synthesize(f0_sweep_down, sp, ap, samplerate)

combined = np.concatenate([y,y2])
soundfile.write('/tmp/resynth_01.wav', combined, samplerate)

```

What other effects can you produce by manipulating this stream? 

### Manipulation of other streams

What effects can you produce by manipulating the other streams? E.g., 
what happens when you corrupt certain frequency bands?

Let's slow the audio by repeating frames:

```
f0_slow = np.repeat(f0, 2)
sp_slow = np.repeat(sp, 2, axis=0)
ap_slow = np.repeat(ap, 2, axis=0)
y = pyworld.synthesize(f0_slow, sp_slow, ap_slow, samplerate)
soundfile.write('/tmp/resynth_01.wav', y, samplerate)
```

... or speed it up by skipping:

```
f0_quick = np.ascontiguousarray(f0[::2])
sp_quick = np.ascontiguousarray(sp[::2,:])
ap_quick = np.ascontiguousarray(sp[::2,:])
y = pyworld.synthesize(f0_quick, sp_quick, ap_quick, samplerate)
soundfile.write('/tmp/resynth_01.wav', y, samplerate)
```


### Format features for modelling

Analysis:

```
from world_features import *

nmelceps = 60

f0, sp, ap, sr = extract_world_features('./data/hvd_181.wav')

melcep = sp2mgc(sp, nmelceps, sr)
bap = ap2coarse(ap, sr)

interp_f0, vuv = interpolate_through_unvoiced(f0)
log_f0 = np.log(interp_f0)
```

Synthesis:

```
f0_2 = np.exp(log_f0)
f0_2[vuv<0.5] = 0.0
f0_2 = f0_2.flatten()

ap2 = coarse2ap(bap, sr, get_world_fftlen(sr))
sp2 = mgc2sp(melcep, sr)

sp2 = np.ascontiguousarray(sp2)
ap2 = np.ascontiguousarray(ap2)
y = pyworld.synthesize(f0_2, sp2, ap2, sr, 5)
soundfile.write('/tmp/b.wav', y, sr)
```

Things to try: vary number of cepstral coefficients used -- what is the effect?
What happens when you corrupt certain cepstral coefficients?



### Other things to try

Try breaking the analysis down into steps as explained [here](https://github.com/JeremyCCHsu/Python-Wrapper-for-World-Vocoder), and changing settings from the defaults.

Try other pitch extractors and vocoders, e.g.:

https://github.com/r9y9/pyreaper

https://github.com/CSTR-Edinburgh/magphase



