import os
import sys

command = """BUNDLE_PATH=~/Documents/music_gen/mag_models/lookback_rnn.mag
CONFIG=lookback_rnn

melody_rnn_generate \
--config=$CONFIG \
--bundle_file=$BUNDLE_PATH \
--output_dir=~/Documents/music_gen/generated \
--num_outputs=1 \
--num_steps=256 \
--primer_melody=[60]
--temperature=1.0
--qpm=180
--beam_size=5
--branch_factor=5
--steps_per_iteration=5"""

os.system(command)
os.system("timidity generated/*")
os.system("rm generated/*")