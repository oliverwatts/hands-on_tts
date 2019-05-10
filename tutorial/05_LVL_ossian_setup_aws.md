## Set up Ossian on AWS

Instructions from Alexander Moses for using his modified version of Ossian with Python 3 Icelandic lexicon & completed Keras integration.

Register to use AWS free tier, then start instance.

DO "create key pair" when prompted, download private key, store in a safe place and change permissions:

```
mv ~/Downloads/aws_test_2.pem.txt ~/Desktop/
chmod 400 ~/Desktop/aws_test_2.pem.txt
```


Create virtual machine in AWS: select "Ubuntu Server 16.04 LTS (HVM), SSD Volume Type - ami-0f49c6ee8f381746f". Choose t2.micro.

ssh into machine:

```

```




Start a screen session:

```
screen
```

Screen reference [here](http://aperiodic.net/screen/quick_reference)

Set up tools:

```
sudo apt-get update

sudo apt-get install unzip  --yes # 
sudo apt-get install sox  --yes
```

Alexander's improved LVL version has fixed most of the code to use Python 3, although there are a couple of exceptions: the g2p package used for handling out-of-vocabulary words is deeply integrated with 2.7 and difficult to convert (also there is a script used in alignment make_proto_hsmm.py which still uses Python 2). Normally I'd use virtual environments for handling these 2 versions, but won't bother with this when working on a virtual machine:


```
sudo apt-get install python2.7  --yes
## python3.5 already installed on AMI

#sudo apt install python2.7-dev
sudo apt install python3.5-dev  --yes
sudo apt-get install build-essential autoconf libtool pkg-config python-opengl  python-pyrex  --yes

curl -O https://bootstrap.pypa.io/get-pip.py
python2.7 get-pip.py --user
python3.5 get-pip.py --user
export PATH=$PATH:~/.local/bin

pip3.5 install future==0.17.1 --user
pip3.5 install sets==0.3.2 --user
pip3.5 install numpy==1.16.3 --user
pip3.5 install tensorflow==1.10.1 --user
pip3.5 install keras==2.2.3 --user    # (older versions will break the code)


pip3.5 install scipy --user
pip3.5 install configobj --user
pip3.5 install scikit-learn --user
pip3.5 install regex --user
pip3.5 install lxml --user
pip3.5 install argparse --user
#
pip3.5 install bandmat  --user
pip3.5 install matplotlib --user

```



For your python 2.7 environment:

```
pip2.7 install numpy==1.16.3 --user
pip2.7 install configobj --user 
```



Get LVL version of Ossian and set up tools, having registered with HTK and set environment variables `$HTK_USERNAME` and `$HTK_PASSWORD`:

```
git clone https://github.com/cadia-lvl/Ossian.git

alias python=python3  ## set up most things with python3
cd Ossian
./scripts/setup_tools.sh $HTK_USERNAME $HTK_PASSWORD
```




Installation of g2p  must be done with python 2 

```
sudo apt-get install swig --yes
alias python=python2.7
./scripts/setup_g2p.sh
alias python=python3.5

```


Set up the data
Place wav data in `./corpus/is/speakers/<speaker_ID>/wav`
Place txt data in `./corpus/is/speakers/<speaker_ID>/txt`

Run script to train all front-end processors

```
alias python=python3.5
python3.5 ./scripts/train.py -s <speaker> -l is lvl_lex_01_nn
```

Note that lvl_lex_01_nn recipe works and uses icelandic lexicon

Configure the backend processors (duration and acoustic neural networks)
Adjust the duration and acoustic config files to your liking:

```
./train/is/speakers/<speaker>/lvl_lex_01_nn/processors/duration_predictor/config.cfg
./train/is/speakers/<speaker>/lvl_lex_01_nn/processors/acoustic_predictor/config.cfg
```

You may have to adjust FRAME_BUFFER_SIZE in ./tools/merlin/src/keras_lib/data_utils.py to fit your available memory

On the t2.micro I needed to edit `./tools/merlin/src/keras_lib/data_utils.py` in order not to exhaust memory, defining FRAME_BUFFER_SIZE like this:

```
FRAME_BUFFER_SIZE = 100000
```


Train the duration and acoustic processors with merlin

```
export dur_config=./train/is/speakers/<speaker>/lvl_lex_01_nn/processors/duration_predictor/config.cfg
export ac_config=./train/is/speakers/<speaker>/lvl_lex_01_nn/processors/acoustic_predictor/config.cfg
python ./tools/merlin/src/run_keras_with_merlin_io.py $dur_config
python ./tools/merlin/src/run_keras_with_merlin_io.py $ac_config
```



Tensorboard can be used to view plots of training error
```
tensorboard --logdir <fullpath>/train/is/speakers/google_f_1041/lvl_lex_01_nn/dnn_training_DUR/plots/
tensorboard --logdir <fullpath>/train/is/speakers/google_f_1041/lvl_lex_01_nn/dnn_training_ACOUST/plots/ --port 6007
```

Note: you can train many networks and each is stored in 3 files:

- Json stores the architecture details
- H5 stores the network weights
- Pickle stores some extra hyperparameters in a python dictionary

Training data from each training session is stored in individual tensorboard files which can be plotted together with tensorboard





Train:
```
export dur_config=./train/is/speakers/<speaker>/lvl_lex_01_nn/processors/duration_predictor/config.cfg
python ./tools/merlin/src/run_keras_with_merlin_io.py $dur_config


export ac_config=./train/is/speakers/<speaker>/lvl_lex_01_nn/processors/acoustic_predictor/config.cfg
python ./tools/merlin/src/run_keras_with_merlin_io.py $ac_config
```


 Copy all files from the training directories (duration and acoustic) to the corresponding voice directories:


```
cp -r  train/is/speakers/<speaker>/lvl_lex_01_nn/processors/acoustic_predictor/* voices/is/HHj_123/lvl_lex_01_nn/processors/acoustic_predictor/

cp -r  train/is/speakers/<speaker>/lvl_lex_01_nn/processors/duration_predictor/* voices/is/HHj_123/lvl_lex_01_nn/processors/duration_predictor

```




Create a folder $OSSIAN/tmp    (some handling of the data streams is done here, we should maybe create and delete this directory somewhere in the code):

```
mkdir $OSSIAN/tmp 
```

Run the speak.py script


```
python3.5 ./scripts/speak.py -s <speaker> -l is -o test.wav lvl_lex_01_nn ./test.txt
```

On local machine, copy the synthesised wave file for listening:

```
scp -i ~/Desktop/aws_test_2.pem.txt ubuntu@ec2-35-178-76-154.eu-west-2.compute.amazonaws.com:/home/ubuntu/Ossian/test.wav ~/Desktop/
```

