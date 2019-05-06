## Set up Ossian on AWS

Register to use AWS free tier, then start instance.

DO "create key pair" when prompted, download private key, store in a safe place and change permissions:

```
mv ~/Downloads/aws_test_2.pem.txt ~/Desktop/
chmod 400 ~/Desktop/aws_test_2.pem.txt
```



ssh into machine:

```

```



Set up tools:

```
sudo apt-get install python

curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py --user
export PATH=$PATH:~/.local/bin
pip --version

sudo apt-get update
sudo apt install python2.7-dev

sudo apt-get install build-essential autoconf libtool pkg-config python-opengl  python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev

sudo apt install sox

pip install scipy --user
pip install scipy --user
pip install configobj --user
pip install scikit-learn --user
pip install regex --user
pip install lxml --user
pip install argparse --user
#We will use the Merlin toolkit to train neural networks, creating the following dependencies:

pip install bandmat  --user
pip install theano --user
pip install matplotlib --user
pip install regex --user        ### !!!!!

git clone -b rvk2019 https://github.com/CSTR-Edinburgh/Ossian.git
cd Ossian
OSSIAN=$PWD
./scripts/setup_tools.sh $HTK_USERNAME $HTK_PASSWORD

```
Toy voice build:
```
cd $OSSIAN
wget https://www.dropbox.com/s/uaz1ue2dked8fan/romanian_toy_demo_corpus_for_ossian.tar?dl=0
tar xvf romanian_toy_demo_corpus_for_ossian.tar\?dl\=0

python ./scripts/train.py -s rss_toy_demo -l rm naive_01_nn
```
