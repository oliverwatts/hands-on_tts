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




Start a screen session:

```
screen
```

Screen reference [here](http://aperiodic.net/screen/quick_reference)

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
pip install regex --user       

pip install soundfile --user   ### !!!!!
pip install librosa --user   ### !!!!!


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

Outputs a load of stuff like:

```
 -- Gather corpus
 -- Train voice
/home/ubuntu/Ossian/train//rm/speakers/rss_toy_demo/naive_01_nn
/home/ubuntu/Ossian/voices//rm/rss_toy_demo/naive_01_nn
try loading config from python...
/home/ubuntu/Ossian/recipes/naive_01_nn.cfg
{'state_contexts': [('start_time', './attribute::start'), ('end_time', './attribute::end'), ('htk_state', 'count(./preceding-sibling::state) + 1'), ('htk_monophone', './ancestor::segment/attribute::pronunciation'), ('ll_segment', './ancestor::segment/preceding::segment[2]/attribute::pronunciation'), ('l_segment', './ancestor::segment/preceding::segment[1]/attribute::pronunciation'), ('c_segment', './ancestor::segment/attribute::pronunciation'), ('r_segment', './ancestor::segment/following::segment[1]/attribute::pronunciation'), ('rr_segment', './ancestor::segment/following::segment[2]/attribute::pronunciation'), ('length_left_word', "count(ancestor::token/preceding::token[@token_class='word'][1]/descendant::segment)"), ('length_current_word', 'count(ancestor::token/descendant::segment)'), ('length_right_word', "count(ancestor::token/following::token[@token_class='word'][1]/descendant::segment)"), ('since_beginning_of_word', "count_Xs_since_start_Y('segment', 'token')"), ('till_end_of_word', "count_Xs_till_end_Y('segment', 'token')"), ('length_l_phrase_in_words', "count(ancestor::phrase/preceding::phrase[1]/descendant::token[@token_class='word'])"), ('length_c_phrase_in_words', "count(ancestor::phrase/descendant::token[@token_class='word'])"), ('length_r_phrase_in_words', "count(ancestor::phrase/following::phrase[1]/descendant::token[@token_class='word'])"), ('length_l_phrase_in_segments', 'count(ancestor::phrase/preceding::phrase[1]/descendant::segment)'), ('length_c_phrase_in_segments', 'count(ancestor::phrase/descendant::segment)'), ('length_r_phrase_in_segments', 'count(ancestor::phrase/following::phrase[1]/descendant::segment)'), ('since_phrase_start_in_segs', "count_Xs_since_start_Y('segment', 'phrase')"), ('till_phrase_end_in_segs', "count_Xs_till_end_Y('segment', 'phrase')"), ('since_phrase_start_in_words', 'count_Xs_since_start_Y(\'token[@token_class="word"]\', \'phrase\')'), ('till_phrase_end_in_words', 'count_Xs_till_end_Y(\'token[@token_class="word"]\', \'phrase\')'), ('since_start_sentence_in_segments', "count_Xs_since_start_Y('segment', 'utt')"), ('since_start_sentence_in_words', 'count_Xs_since_start_Y(\'token[@token_class="word"]\', \'utt\')'), ('since_start_sentence_in_phrases', "count_Xs_since_start_Y('phrase', 'utt')"), ('till_end_sentence_in_segments', "count_Xs_till_end_Y('segment', 'utt')"), ('till_end_sentence_in_words', 'count_Xs_till_end_Y(\'token[@token_class="word"]\', \'utt\')'), ('till_end_sentence_in_phrases', "count_Xs_till_end_Y('phrase', 'utt')"), ('length_sentence_in_segments', 'count(ancestor::utt/descendant::segment)'), ('length_sentence_in_words', "count(ancestor::utt/descendant::token[@token_class='word'])"), ('length_sentence_in_phrases', 'count(ancestor::utt/descendant::phrase)'), ('L_vsm_d1', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d1"), ('C_vsm_d1', './ancestor::token/attribute::vsm_d1'), ('R_vsm_d1', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d1"), ('L_vsm_d2', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d2"), ('C_vsm_d2', './ancestor::token/attribute::vsm_d2'), ('R_vsm_d2', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d2"), ('L_vsm_d3', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d3"), ('C_vsm_d3', './ancestor::token/attribute::vsm_d3'), ('R_vsm_d3', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d3"), ('L_vsm_d4', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d4"), ('C_vsm_d4', './ancestor::token/attribute::vsm_d4'), ('R_vsm_d4', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d4"), ('L_vsm_d5', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d5"), ('C_vsm_d5', './ancestor::token/attribute::vsm_d5'), ('R_vsm_d5', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d5"), ('L_vsm_d6', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d6"), ('C_vsm_d6', './ancestor::token/attribute::vsm_d6'), ('R_vsm_d6', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d6"), ('L_vsm_d7', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d7"), ('C_vsm_d7', './ancestor::token/attribute::vsm_d7'), ('R_vsm_d7', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d7"), ('L_vsm_d8', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d8"), ('C_vsm_d8', './ancestor::token/attribute::vsm_d8'), ('R_vsm_d8', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d8"), ('L_vsm_d9', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d9"), ('C_vsm_d9', './ancestor::token/attribute::vsm_d9'), ('R_vsm_d9', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d9"), ('L_vsm_d10', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d10"), ('C_vsm_d10', './ancestor::token/attribute::vsm_d10'), ('R_vsm_d10', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d10")], 'dur_label_maker': <FeatureDumper.FeatureDumper object at 0x7f58175c8090>, 'SKLDecisionTreePausePredictor': <class 'SKLProcessors.SKLDecisionTreePausePredictor'>, 'train_stages': [[<Tokenisers.RegexTokeniser object at 0x7f5818a98650>, <Phonetisers.NaivePhonetiser object at 0x7f58175b6e90>, <VSMTagger.VSMTagger object at 0x7f58175b6e50>], [<FeatureDumper.FeatureDumper object at 0x7f58175b6f50>, <FeatureExtractor.WorldExtractor object at 0x7f58175b6f10>, <Aligner.StateAligner object at 0x7f58175b6f90>, <SKLProcessors.SKLDecisionTreePausePredictor object at 0x7f58175c80d0>, <PhraseMaker.PhraseMaker object at 0x7f58175c8110>, <FeatureDumper.FeatureDumper object at 0x7f58175c8050>], [<FeatureDumper.FeatureDumper object at 0x7f58175c8090>, <NN.NNDurationPredictor object at 0x7f58175c8290>, <FeatureDumper.FeatureDumper object at 0x7f58175c82d0>, <NN.NNAcousticPredictor object at 0x7f58175c8310>]], 'PUNC_PATT': '[\\p{C}||\\p{P}||\\p{S}]', 'JUNCTURE_NODES': "//token[@token_class='space'] | //token[@token_class='punctuation']", 'WorldExtractor': <class 'FeatureExtractor.WorldExtractor'>, 'RegexTokeniser': <class 'Tokenisers.RegexTokeniser'>, 'current_dir': '/home/ubuntu/Ossian/recipes', 'phrase_adder': <PhraseMaker.PhraseMaker object at 0x7f58175c8110>, 'dur_data_maker': <FeatureDumper.FeatureDumper object at 0x7f58175c8050>, 'pause_predictor': <SKLProcessors.SKLDecisionTreePausePredictor object at 0x7f58175c80d0>, 'speech_generation': [<FeatureDumper.FeatureDumper object at 0x7f58175c8090>, <NN.NNDurationPredictor object at 0x7f58175c8290>, <FeatureDumper.FeatureDumper object at 0x7f58175c82d0>, <NN.NNAcousticPredictor object at 0x7f58175c8310>], 'runtime_stages': [[<Tokenisers.RegexTokeniser object at 0x7f5818a98650>, <Phonetisers.NaivePhonetiser object at 0x7f58175b6e90>, <VSMTagger.VSMTagger object at 0x7f58175b6e50>], [<SKLProcessors.SKLDecisionTreePausePredictor object at 0x7f58175c80d0>, <PhraseMaker.PhraseMaker object at 0x7f58175c8110>], [<FeatureDumper.FeatureDumper object at 0x7f58175c8090>, <NN.NNDurationPredictor object at 0x7f58175c8290>, <FeatureDumper.FeatureDumper object at 0x7f58175c82d0>, <NN.NNAcousticPredictor object at 0x7f58175c8310>]], 'text_proc': [<Tokenisers.RegexTokeniser object at 0x7f5818a98650>, <Phonetisers.NaivePhonetiser object at 0x7f58175b6e90>, <VSMTagger.VSMTagger object at 0x7f58175b6e50>], 'acoustic_predictor': <NN.NNAcousticPredictor object at 0x7f58175c8310>, 'duration_predictor': <NN.NNDurationPredictor object at 0x7f58175c8290>, 'NNAcousticPredictor': <class 'NN.NNAcousticPredictor'>, 'align_label_dumper': <FeatureDumper.FeatureDumper object at 0x7f58175b6f50>, 'pause_predictor_features': [('response', './attribute::has_silence="yes"'), ('token_is_punctuation', './attribute::token_class="punctuation"'), ('since_start_utterance_in_words', "count(preceding::token[@token_class='word'])"), ('till_end_utterance_in_words', "count(following::token[@token_class='word'])"), ('L_vsm_d1', "./preceding::token[@token_class='word'][1]/attribute::vsm_d1"), ('C_vsm_d1', './attribute::vsm_d1'), ('R_vsm_d1', "./following::token[@token_class='word'][1]/attribute::vsm_d1"), ('L_vsm_d2', "./preceding::token[@token_class='word'][1]/attribute::vsm_d2"), ('C_vsm_d2', './attribute::vsm_d2'), ('R_vsm_d2', "./following::token[@token_class='word'][1]/attribute::vsm_d2"), ('L_vsm_d3', "./preceding::token[@token_class='word'][1]/attribute::vsm_d3"), ('C_vsm_d3', './attribute::vsm_d3'), ('R_vsm_d3', "./following::token[@token_class='word'][1]/attribute::vsm_d3"), ('L_vsm_d4', "./preceding::token[@token_class='word'][1]/attribute::vsm_d4"), ('C_vsm_d4', './attribute::vsm_d4'), ('R_vsm_d4', "./following::token[@token_class='word'][1]/attribute::vsm_d4"), ('L_vsm_d5', "./preceding::token[@token_class='word'][1]/attribute::vsm_d5"), ('C_vsm_d5', './attribute::vsm_d5'), ('R_vsm_d5', "./following::token[@token_class='word'][1]/attribute::vsm_d5"), ('L_vsm_d6', "./preceding::token[@token_class='word'][1]/attribute::vsm_d6"), ('C_vsm_d6', './attribute::vsm_d6'), ('R_vsm_d6', "./following::token[@token_class='word'][1]/attribute::vsm_d6"), ('L_vsm_d7', "./preceding::token[@token_class='word'][1]/attribute::vsm_d7"), ('C_vsm_d7', './attribute::vsm_d7'), ('R_vsm_d7', "./following::token[@token_class='word'][1]/attribute::vsm_d7"), ('L_vsm_d8', "./preceding::token[@token_class='word'][1]/attribute::vsm_d8"), ('C_vsm_d8', './attribute::vsm_d8'), ('R_vsm_d8', "./following::token[@token_class='word'][1]/attribute::vsm_d8"), ('L_vsm_d9', "./preceding::token[@token_class='word'][1]/attribute::vsm_d9"), ('C_vsm_d9', './attribute::vsm_d9'), ('R_vsm_d9', "./following::token[@token_class='word'][1]/attribute::vsm_d9"), ('L_vsm_d10', "./preceding::token[@token_class='word'][1]/attribute::vsm_d10"), ('C_vsm_d10', './attribute::vsm_d10'), ('R_vsm_d10', "./following::token[@token_class='word'][1]/attribute::vsm_d10")], 'PhraseMaker': <class 'PhraseMaker.PhraseMaker'>, 'alignment': [<FeatureDumper.FeatureDumper object at 0x7f58175b6f50>, <FeatureExtractor.WorldExtractor object at 0x7f58175b6f10>, <Aligner.StateAligner object at 0x7f58175b6f90>, <SKLProcessors.SKLDecisionTreePausePredictor object at 0x7f58175c80d0>, <PhraseMaker.PhraseMaker object at 0x7f58175c8110>, <FeatureDumper.FeatureDumper object at 0x7f58175c8050>], 'VSMTagger': <class 'VSMTagger.VSMTagger'>, 'duration_data_contexts': [('state_1_nframes', '(./state[1]/attribute::end - ./state[1]/attribute::start) div 5'), ('state_2_nframes', '(./state[2]/attribute::end - ./state[2]/attribute::start) div 5'), ('state_3_nframes', '(./state[3]/attribute::end - ./state[3]/attribute::start) div 5'), ('state_4_nframes', '(./state[4]/attribute::end - ./state[4]/attribute::start) div 5'), ('state_5_nframes', '(./state[5]/attribute::end - ./state[5]/attribute::start) div 5')], 'phone_and_state_contexts': [('length_left_word', "count(ancestor::token/preceding::token[@token_class='word'][1]/descendant::segment)"), ('length_current_word', 'count(ancestor::token/descendant::segment)'), ('length_right_word', "count(ancestor::token/following::token[@token_class='word'][1]/descendant::segment)"), ('since_beginning_of_word', "count_Xs_since_start_Y('segment', 'token')"), ('till_end_of_word', "count_Xs_till_end_Y('segment', 'token')"), ('length_l_phrase_in_words', "count(ancestor::phrase/preceding::phrase[1]/descendant::token[@token_class='word'])"), ('length_c_phrase_in_words', "count(ancestor::phrase/descendant::token[@token_class='word'])"), ('length_r_phrase_in_words', "count(ancestor::phrase/following::phrase[1]/descendant::token[@token_class='word'])"), ('length_l_phrase_in_segments', 'count(ancestor::phrase/preceding::phrase[1]/descendant::segment)'), ('length_c_phrase_in_segments', 'count(ancestor::phrase/descendant::segment)'), ('length_r_phrase_in_segments', 'count(ancestor::phrase/following::phrase[1]/descendant::segment)'), ('since_phrase_start_in_segs', "count_Xs_since_start_Y('segment', 'phrase')"), ('till_phrase_end_in_segs', "count_Xs_till_end_Y('segment', 'phrase')"), ('since_phrase_start_in_words', 'count_Xs_since_start_Y(\'token[@token_class="word"]\', \'phrase\')'), ('till_phrase_end_in_words', 'count_Xs_till_end_Y(\'token[@token_class="word"]\', \'phrase\')'), ('since_start_sentence_in_segments', "count_Xs_since_start_Y('segment', 'utt')"), ('since_start_sentence_in_words', 'count_Xs_since_start_Y(\'token[@token_class="word"]\', \'utt\')'), ('since_start_sentence_in_phrases', "count_Xs_since_start_Y('phrase', 'utt')"), ('till_end_sentence_in_segments', "count_Xs_till_end_Y('segment', 'utt')"), ('till_end_sentence_in_words', 'count_Xs_till_end_Y(\'token[@token_class="word"]\', \'utt\')'), ('till_end_sentence_in_phrases', "count_Xs_till_end_Y('phrase', 'utt')"), ('length_sentence_in_segments', 'count(ancestor::utt/descendant::segment)'), ('length_sentence_in_words', "count(ancestor::utt/descendant::token[@token_class='word'])"), ('length_sentence_in_phrases', 'count(ancestor::utt/descendant::phrase)'), ('L_vsm_d1', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d1"), ('C_vsm_d1', './ancestor::token/attribute::vsm_d1'), ('R_vsm_d1', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d1"), ('L_vsm_d2', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d2"), ('C_vsm_d2', './ancestor::token/attribute::vsm_d2'), ('R_vsm_d2', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d2"), ('L_vsm_d3', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d3"), ('C_vsm_d3', './ancestor::token/attribute::vsm_d3'), ('R_vsm_d3', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d3"), ('L_vsm_d4', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d4"), ('C_vsm_d4', './ancestor::token/attribute::vsm_d4'), ('R_vsm_d4', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d4"), ('L_vsm_d5', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d5"), ('C_vsm_d5', './ancestor::token/attribute::vsm_d5'), ('R_vsm_d5', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d5"), ('L_vsm_d6', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d6"), ('C_vsm_d6', './ancestor::token/attribute::vsm_d6'), ('R_vsm_d6', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d6"), ('L_vsm_d7', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d7"), ('C_vsm_d7', './ancestor::token/attribute::vsm_d7'), ('R_vsm_d7', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d7"), ('L_vsm_d8', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d8"), ('C_vsm_d8', './ancestor::token/attribute::vsm_d8'), ('R_vsm_d8', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d8"), ('L_vsm_d9', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d9"), ('C_vsm_d9', './ancestor::token/attribute::vsm_d9'), ('R_vsm_d9', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d9"), ('L_vsm_d10', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d10"), ('C_vsm_d10', './ancestor::token/attribute::vsm_d10'), ('R_vsm_d10', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d10")], 'word_vector_tagger': <VSMTagger.VSMTagger object at 0x7f58175b6e50>, 'inspect': <module 'inspect' from '/usr/lib/python2.7/inspect.pyc'>, 'tokenisation_pattern': '(\\p{Z}*[\\p{C}||\\p{P}||\\p{S}]*\\p{Z}+|\\p{Z}*[\\p{C}||\\p{P}||\\p{S}]+\\Z)', 'aligner': <Aligner.StateAligner object at 0x7f58175b6f90>, 'sys': <module 'sys' (built-in)>, 'dnn_label_maker': <FeatureDumper.FeatureDumper object at 0x7f58175c82d0>, 'NaivePhonetiser': <class 'Phonetisers.NaivePhonetiser'>, 'tokeniser': <Tokenisers.RegexTokeniser object at 0x7f5818a98650>, 'LETTER_PATT': '[\\p{L}||\\p{N}||\\p{M}]', 'AcousticModelWorld': <class 'AcousticModel.AcousticModelWorld'>, 'speech_feature_extractor': <FeatureExtractor.WorldExtractor object at 0x7f58175b6f10>, 'dim': 10, 'c': <module 'default.const' from '/home/ubuntu/Ossian/scripts/default/const.py'>, 'FeatureDumper': <class 'FeatureDumper.FeatureDumper'>, 'word_vsm_dim': 10, 'speech_coding_config': {'delta_delta_window': '1.0 -2.0 1.0', 'static_window': '1', 'order': 59, 'delta_window': '-0.5 0.0 0.5'}, 'pause_prediction': [<SKLProcessors.SKLDecisionTreePausePredictor object at 0x7f58175c80d0>, <PhraseMaker.PhraseMaker object at 0x7f58175c8110>], 'i': 5, 'SPACE_PATT': '\\p{Z}', 'PUNC_OR_SPACE_PATT': '[\\p{Z}||\\p{C}||\\p{P}||\\p{S}]', 'phonetiser': <Phonetisers.NaivePhonetiser object at 0x7f58175b6e90>, 'NNDurationPredictor': <class 'NN.NNDurationPredictor'>, 'os': <module 'os' from '/usr/lib/python2.7/os.pyc'>, 'phone_contexts': [('htk_monophone', './attribute::pronunciation'), ('start_time', './attribute::start'), ('end_time', './attribute::end'), ('ll_segment', 'preceding::segment[2]/attribute::pronunciation'), ('l_segment', 'preceding::segment[1]/attribute::pronunciation'), ('c_segment', './attribute::pronunciation'), ('r_segment', 'following::segment[1]/attribute::pronunciation'), ('rr_segment', 'following::segment[2]/attribute::pronunciation'), ('length_left_word', "count(ancestor::token/preceding::token[@token_class='word'][1]/descendant::segment)"), ('length_current_word', 'count(ancestor::token/descendant::segment)'), ('length_right_word', "count(ancestor::token/following::token[@token_class='word'][1]/descendant::segment)"), ('since_beginning_of_word', "count_Xs_since_start_Y('segment', 'token')"), ('till_end_of_word', "count_Xs_till_end_Y('segment', 'token')"), ('length_l_phrase_in_words', "count(ancestor::phrase/preceding::phrase[1]/descendant::token[@token_class='word'])"), ('length_c_phrase_in_words', "count(ancestor::phrase/descendant::token[@token_class='word'])"), ('length_r_phrase_in_words', "count(ancestor::phrase/following::phrase[1]/descendant::token[@token_class='word'])"), ('length_l_phrase_in_segments', 'count(ancestor::phrase/preceding::phrase[1]/descendant::segment)'), ('length_c_phrase_in_segments', 'count(ancestor::phrase/descendant::segment)'), ('length_r_phrase_in_segments', 'count(ancestor::phrase/following::phrase[1]/descendant::segment)'), ('since_phrase_start_in_segs', "count_Xs_since_start_Y('segment', 'phrase')"), ('till_phrase_end_in_segs', "count_Xs_till_end_Y('segment', 'phrase')"), ('since_phrase_start_in_words', 'count_Xs_since_start_Y(\'token[@token_class="word"]\', \'phrase\')'), ('till_phrase_end_in_words', 'count_Xs_till_end_Y(\'token[@token_class="word"]\', \'phrase\')'), ('since_start_sentence_in_segments', "count_Xs_since_start_Y('segment', 'utt')"), ('since_start_sentence_in_words', 'count_Xs_since_start_Y(\'token[@token_class="word"]\', \'utt\')'), ('since_start_sentence_in_phrases', "count_Xs_since_start_Y('phrase', 'utt')"), ('till_end_sentence_in_segments', "count_Xs_till_end_Y('segment', 'utt')"), ('till_end_sentence_in_words', 'count_Xs_till_end_Y(\'token[@token_class="word"]\', \'utt\')'), ('till_end_sentence_in_phrases', "count_Xs_till_end_Y('phrase', 'utt')"), ('length_sentence_in_segments', 'count(ancestor::utt/descendant::segment)'), ('length_sentence_in_words', "count(ancestor::utt/descendant::token[@token_class='word'])"), ('length_sentence_in_phrases', 'count(ancestor::utt/descendant::phrase)'), ('L_vsm_d1', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d1"), ('C_vsm_d1', './ancestor::token/attribute::vsm_d1'), ('R_vsm_d1', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d1"), ('L_vsm_d2', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d2"), ('C_vsm_d2', './ancestor::token/attribute::vsm_d2'), ('R_vsm_d2', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d2"), ('L_vsm_d3', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d3"), ('C_vsm_d3', './ancestor::token/attribute::vsm_d3'), ('R_vsm_d3', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d3"), ('L_vsm_d4', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d4"), ('C_vsm_d4', './ancestor::token/attribute::vsm_d4'), ('R_vsm_d4', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d4"), ('L_vsm_d5', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d5"), ('C_vsm_d5', './ancestor::token/attribute::vsm_d5'), ('R_vsm_d5', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d5"), ('L_vsm_d6', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d6"), ('C_vsm_d6', './ancestor::token/attribute::vsm_d6'), ('R_vsm_d6', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d6"), ('L_vsm_d7', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d7"), ('C_vsm_d7', './ancestor::token/attribute::vsm_d7'), ('R_vsm_d7', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d7"), ('L_vsm_d8', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d8"), ('C_vsm_d8', './ancestor::token/attribute::vsm_d8'), ('R_vsm_d8', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d8"), ('L_vsm_d9', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d9"), ('C_vsm_d9', './ancestor::token/attribute::vsm_d9'), ('R_vsm_d9', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d9"), ('L_vsm_d10', "./ancestor::token/preceding::token[@token_class='word'][1]/attribute::vsm_d10"), ('C_vsm_d10', './ancestor::token/attribute::vsm_d10'), ('R_vsm_d10', "./ancestor::token/following::token[@token_class='word'][1]/attribute::vsm_d10")], 'StateAligner': <class 'Aligner.StateAligner'>}
train
Cannot load NN model from model_dir: /home/ubuntu/Ossian/train//rm/speakers/rss_toy_demo/naive_01_nn/processors/duration_predictor -- not trained yet
Cannot load NN model from model_dir: /home/ubuntu/Ossian/train//rm/speakers/rss_toy_demo/naive_01_nn/processors/acoustic_predictor -- not trained yet


== Train voice (proc no. 1 (word_splitter))  ==
Train processor word_splitter
RegexTokeniser requires no training
          Applying processor word_splitter
p p p p p p p p p p p p p p p p p p p p p p p p p p p p p

== Train voice (proc no. 2 (segment_adder))  ==
Train processor segment_adder
NaivePhonetiser requires no training
          Applying processor segment_adder
p p p p p p p p p p p p p p p p p p p p p p p p p p p p p

== Train voice (proc no. 3 (word_vector_tagger))  ==
Train processor word_vector_tagger
Count types...
Assemble cooccurance matrix...
Factorise cooccurance matrix...
Write output to /home/ubuntu/Ossian/train//rm/speakers/rss_toy_demo/naive_01_nn/processors/word_vector_tagger/table_file.table
          Applying processor word_vector_tagger
p p p p p p p p p p p p p p p p p p p p p p p p p p p p p

== Train voice (proc no. 4 (feature_dumper))  ==
Train processor feature_dumper
          Applying processor feature_dumper
p p p p p p p p p p p p p p p p p p p p p p p p p p p p p

== Train voice (proc no. 5 (acoustic_feature_extractor))  ==
Train processor acoustic_feature_extractor
          Applying processor acoustic_feature_extractor
p p p p p p p p p p p p p p p p p p p p p p p p p p p p p

== Train voice (proc no. 6 (aligner))  ==
Train processor aligner

          Training aligner -- see /home/ubuntu/Ossian/train//rm/speakers/rss_toy_demo/naive_01_nn/processors/aligner/training/log.txt

Aligner training took 0 minutes and 12 seconds to run.
          Applying processor aligner
p p p p p p p p p p p p p p p p p p p p p p p p p p p p p

== Train voice (proc no. 7 (pause_predictor))  ==
Train processor pause_predictor

 Trained classifier:
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
            max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=10, min_samples_split=2,
            min_weight_fraction_leaf=0.0, presort=False, random_state=None,
            splitter='best')

 Trained x vectoriser:
DictVectorizer(dtype=<type 'numpy.float64'>, separator='=', sort=True,
        sparse=True)
Feature names:
['C_vsm_d1', 'C_vsm_d10', 'C_vsm_d2', 'C_vsm_d3', 'C_vsm_d4', 'C_vsm_d5', 'C_vsm_d6', 'C_vsm_d7', 'C_vsm_d8', 'C_vsm_d9', 'L_vsm_d1', 'L_vsm_d10', 'L_vsm_d2', 'L_vsm_d3', 'L_vsm_d4', 'L_vsm_d5', 'L_vsm_d6', 'L_vsm_d7', 'L_vsm_d8', 'L_vsm_d9', 'R_vsm_d1', 'R_vsm_d10', 'R_vsm_d2', 'R_vsm_d3', 'R_vsm_d4', 'R_vsm_d5', 'R_vsm_d6', 'R_vsm_d7', 'R_vsm_d8', 'R_vsm_d9', 'since_start_utterance_in_words', 'till_end_utterance_in_words', 'token_is_punctuation']

 Trained y vectoriser:
DictVectorizer(dtype=<type 'numpy.float64'>, separator='=', sort=True,
        sparse=True)
Feature names:
['response']
          Applying processor pause_predictor
p p p p p p p p p p p p p p p p p p p p p p p p p p p p p

== Train voice (proc no. 8 (phrase_maker))  ==
Train processor phrase_maker
          (This processor requires no training)
          Applying processor phrase_maker
p p p p p p p p p p p p p p p p p p p p p p p p p p p p p

== Train voice (proc no. 9 (duration_data_maker))  ==
Train processor duration_data_maker
          Applying processor duration_data_maker
p p p p p p p p p p p p p p p p p p p p p p p p p p p p p

== Train voice (proc no. 10 (labelmaker))  ==
Train processor labelmaker
          Applying processor labelmaker
p p p p p p p p p p p p p p p p p p p p p p p p p p p p p

== Train voice (proc no. 11 (duration_predictor))  ==
Train processor duration_predictor
Training of NNDurationPredictor itself not supported within Ossian --
use Merlin to train on the prepared data
------------
Wrote config file to:
/home/ubuntu/Ossian/train//rm/speakers/rss_toy_demo/naive_01_nn/processors/duration_predictor/config.cfg
Edit this config file as appropriate and use for training with Merlin.
In particular, you will want to increase training_epochs to train real voices
You will also want to experiment with learning_rate, batch_size, hidden_layer_size, hidden_layer_type

To train with Merlin and then store the resulting model in a format suitable for Ossian, please do:

cd /home/ubuntu/Ossian
export THEANO_FLAGS=""; python ./tools/merlin/src/run_merlin.py /home/ubuntu/Ossian/train//rm/speakers/rss_toy_demo/naive_01_nn/processors/duration_predictor/config.cfg
python ./scripts/util/store_merlin_model.py /home/ubuntu/Ossian/train//rm/speakers/rss_toy_demo/naive_01_nn/processors/duration_predictor/config.cfg /home/ubuntu/Ossian/voices/rm/rss_toy_demo/naive_01_nn/processors/duration_predictor

------------
          Applying processor duration_predictor
p p p p p p p p p p p p p p p p p p p p p p p p p p p p p

== Train voice (proc no. 12 (dnn_labelmaker))  ==
Train processor dnn_labelmaker
          Applying processor dnn_labelmaker
p p p p p p p p p p p p p p p p p p p p p p p p p p p p p

== Train voice (proc no. 13 (acoustic_predictor))  ==
Train processor acoustic_predictor
Training of NNAcousticPredictor itself not supported within Ossian --
use Merlin to train on the prepared data
------------
Wrote config file to:
/home/ubuntu/Ossian/train//rm/speakers/rss_toy_demo/naive_01_nn/processors/acoustic_predictor/config.cfg
Edit this config file as appropriate and use for training with Merlin.
In particular, you will want to increase training_epochs to train real voices
You will also want to experiment with learning_rate, batch_size, hidden_layer_size, hidden_layer_type

To train with Merlin and then store the resulting model in a format suitable for Ossian, please do:

cd /home/ubuntu/Ossian
export THEANO_FLAGS= ; python ./tools/merlin/src/run_merlin.py /home/ubuntu/Ossian/train//rm/speakers/rss_toy_demo/naive_01_nn/processors/acoustic_predictor/config.cfg
python ./scripts/util/store_merlin_model.py /home/ubuntu/Ossian/train//rm/speakers/rss_toy_demo/naive_01_nn/processors/acoustic_predictor/config.cfg /home/ubuntu/Ossian/voices/rm/rss_toy_demo/naive_01_nn/processors/acoustic_predictor

------------
          Applying processor acoustic_predictor
p p p p p p p p p p p p p p p p p p p p p p p p p p p p p
ubuntu@ip-172-31-24-151:~/Ossian$
```

Train acoustic and duration models as explained in the notes printed out above.

Synthesise:

```
mkdir $OSSIAN/test/wav/

python ./scripts/speak.py -l rm -s rss_toy_demo -o ./test/wav/romanian_toy_HTS.wav naive_01_nn ./test/txt/romanian.txt

```

Copy generated waveform back to local machine with scp:
```
scp -i ~/Desktop/aws_test_2.pem.txt ubuntu@ec2-18-130-168-119.eu-west-2.compute.amazonaws.com:/home/ubuntu/Ossian/voices//rm/rss_toy_demo/naive_01_nn/output/wav/temp.wav ~/Desktop/
```
