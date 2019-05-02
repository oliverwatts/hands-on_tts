## Icelandic TTS resources

### Tools

Trained Ossian voices -- https://github.com/cadia-lvl/Ossian
Others at https://github.com/cadia-lvl/ -- e.g. lexicon, text norm, taggers...


espeak

```
  git clone https://github.com/espeak-ng/espeak-ng.git
  cd espeak-ng/
  ./autogen.sh
  ./configure --prefix=/disk/scratch/oliver/espeak/ --with-mbrola=no
  ### commented out line 2145 of Makefile!!!!
  make
  make install
```

```
 for RULES in ~/tool/espeak-ng/dictsource/*rules ; do wc -l $RULES ; done | sort
```

```
echo 'Ég mæli fyrir frumvarpi til nýrra upplýsingalaga' | ~/tool/espeak-ng/src/espeak-ng -v gmq/is -w /tmp/test.wav
```


### Data
http://www.malfong.is

- Hjal málheildin
- Þór-málheildin
- RÚV-málheildin
- Málrómur
- Alþingisræður til talgreiningar -- cleaned & segmented version from Inga?

- Others?
