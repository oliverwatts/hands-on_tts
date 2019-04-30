## Digital audio


<!-- https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/ -->

<!-- ### Create 1 cycle of a sine wave -->

<!-- To create 1 cycle of a sine wave, we need to move a hand around 
a clock in small increments (whose size is determined by the 
sampling rate we are using) and evaluate the sine function of the 
angle between the moving hand and a fixed hand pointing to 3 o'clock,
as illustrated here:

 https://upload.wikimedia.org/wikipedia/commons/3/3b/Circle_cos_sin.gif

 (See also Peter Ladefoged "Elements of Acoustic Phonetics", 2nd ed., pp.152-4) 
 -->
<!-- The measure of angle we will use will be radians rather than degrees.
Instead of counting 1 cycle as 360 degrees, we will count it as 2*pi
radians. This is explained visually here:

https://en.wikipedia.org/wiki/Radian#/media/File:Circle_radians.gif

 -->


```
## create array of 100 increments between 0 and 2*pi, 
## i.e. 1 cycle expressed in radians sampled 100 times:
x = np.linspace(0, 2*np.pi, 100) 
plt.plot(x, np.sin(x)) 
#plt.plot(x, np.cos(x))
plt.show()    
```



Try this:

```
balh balh
```

And this:

```
etc etc
```


imp