# coding=utf-8

import re
import os
import codecs
import subprocess


def rename_wav(origin):
    pathwav = re.findall('.+/wav/', origin)[0]
    rawwav = re.findall('/wav/.+', origin)
    tmp = re.sub('\.wav', '', rawwav[0])
    new_wav_name = pathwav + tmp[5:] + '.wav'
    # os.rename(origin, new_wav_name)
    return new_wav_name


def read_stm(origin):
    file_name = re.findall('/wav/.+', origin)[0][5:-4]
    stm_path = re.findall('.+/wav/', origin)[0][:-5] + '/stm/'
    stm_file = stm_path + file_name + '.stm'
    # fr = codecs.open(origin, 'r', 'utf-8').read()
    # raw_content = re.findall('[^\x00-\xff].+', fr)
    # content = raw_content[0]
    # return content
    return file_name, stm_file

string = '/disk3/human_test_data_transfer3/wav/ZHANHUIYUAN517_010.wav_mix_white.wav_tempo_slow10.wav'


# raw = re.findall('/wav/.+', string)
# content = raw[0]
# new_content = re.sub('\.wav', '', content)
# path = re.findall('.+/wav/', string)[0]
# print(path, new_content[5:])

# print(rename_wav(string))

subprocess.call('soundstretch /disk2/wav_transfer_tool/noise/rain1.wav /disk2/wav_transfer_tool/rain1test.wav -pitch=+10 >/dev/null 2>&1', shell=True)

