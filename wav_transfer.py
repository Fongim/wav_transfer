# coding = utf-8

from pydub import AudioSegment
import subprocess
import random
import codecs
import os
import re
import wave
import shutil
import multiprocessing

# 需要用到开源软件 soundstretch
# ubuntu: sudo apt-get install soundstretch
# windows: 把 soundstretch.exe 的路径加入到系统环境变量


# 变调不变速
def sound_stretch_pitch(origin, db, output):
    subprocess.call('soundstretch ' + origin + ' ' + output + ' -pitch=' + db + ' -speech >/dev/null 2>&1',
                    shell=True)


# 变速不变调
def sound_stretch_tempo(origin, percent, output):
    subprocess.call('soundstretch ' + origin + ' ' + output + ' -tempo=' + percent + ' -speech >/dev/null 2>&1',
                    shell=True)


# 叠加噪声
def combine_noise(wav, noise, output):
    sound1 = AudioSegment.from_file(wav)
    sound2 = AudioSegment.from_file(noise)
    combined = sound1.overlay(sound2)
    combined.export(output, format='wav')


# 重命名生成的音频
def rename_wav(origin):
    path = re.findall('.+/wav/', origin)[0]
    raw = re.findall('/wav/.+', origin)[0]
    tmp = re.sub('\.wav', '', raw)
    new_wav_name = path + tmp[5:] + '.wav'
    os.rename(origin, new_wav_name)
    return new_wav_name


# 读初始stm的中文内容
def read_stm(origin):
    file_name = re.findall('/wav/.+', origin)[0][5:-4]
    stm_path = re.findall('.+/wav/', origin)[0][:-5] + '/stm/'
    file_name_with_suffix = file_name + '.stm'
    stm_file = stm_path + file_name_with_suffix
    with codecs.open(stm_file, 'r', 'utf-8') as fr:
        content = re.findall('[^\x00-\xff].+', fr.read())[0]
    return stm_file, file_name_with_suffix, content


# 生成新的stm
def init_stm(origin, char):
    with wave.open(origin, 'rb') as wav_read:
        times = '%.3f' % (wav_read.getnframes() / wav_read.getframerate())

    file_name = re.findall('/wav/.+', origin)[0][5:-4]
    stm_path = re.findall('.+/wav/', origin)[0][:-5] + '/stm/'
    file_name_with_suffix = file_name + '.stm'
    stm_file = stm_path + file_name_with_suffix

    with codecs.open(stm_file, 'w') as stm_write:
        content = file_name + ' A ' + file_name + ' 0 ' + str(times) + ' <o,f0,female> ' + char
        stm_write.write(content)
    return stm_file, file_name_with_suffix


class Mix(object):
    def __init__(self):

        # 噪声路径
        self.noise_path = '/disk2/wav_transfer_tool/noise/'

        self.o_rain = ['rain1.wav', 'rain2.wav', 'rain3.wav']
        self.rain = [self.noise_path + i for i in self.o_rain]
        self.white = self.noise_path + 'white.wav'
        self.dish = self.noise_path + 'dish.wav'
        self.human = self.noise_path + 'human.wav'
        self.cafe = self.noise_path + 'cafe.wav'
        self.car = self.noise_path + 'car.wav'

        self.volume = {'+2': '+2', '+1': '+1', '-2': '-2', '-1': '-1'}
        self.percent = {'+5': '+5', '-5': '-5', '+10': '+10', '-10': '-10', '+15': '+15', '-15': '-15',
                        '+20': '+20', '-20': '-20', '+25': '+25', '-25': '-25', '+30': '+30', '-30': '-30'}

        self.mix_suffix = {'rain': '_mix_rain.wav',
                           'dish': '_mix_dish.wav',
                           'human': '_mix_human.wav',
                           'white': '_mix_white.wav',
                           'cafe': '_mix_cafe.wav',
                           'car': '_mix_car.wav'}
        self.transfer_suffix = {'p2': '_pitch_plus2.wav', 'p1': '_pitch_plus1.wav',
                                'm2': '_pitch_minus2.wav', 'm1': '_pitch_minus1.wav',
                                'f5': '_tempo_fast5.wav', 's5': '_tempo_slow5.wav',
                                'f10': '_tempo_fast10.wav', 's10': '_tempo_slow10.wav',
                                'f15': '_tempo_fast15.wav', 's15': '_tempo_slow15.wav',
                                'f20': '_tempo_fast20.wav', 's20': '_tempo_slow20.wav',
                                'f25': '_tempo_fast25.wav', 's25': '_tempo_slow25.wav',
                                'f30': '_tempo_fast30.wav', 's30': '_tempo_slow30.wav'}

    def mix_rain(self, origin, output):
        noise = random.choice(self.rain)
        mixed = output + self.mix_suffix['rain']
        combine_noise(origin, noise, mixed)
        return mixed

    def mix_dish(self, origin, output):
        noise = self.dish
        mixed = output + self.mix_suffix['dish']
        combine_noise(origin, noise, mixed)
        return mixed

    def mix_human(self, origin, output):
        noise = self.human
        mixed = output + self.mix_suffix['human']
        combine_noise(origin, noise, mixed)
        return mixed

    def mix_white(self, origin, output):
        noise = self.white
        mixed = output + self.mix_suffix['white']
        combine_noise(origin, noise, mixed)
        return mixed

    def mix_cafe(self, origin, output):
        noise = self.cafe
        mixed = output + self.mix_suffix['cafe']
        combine_noise(origin, noise, mixed)
        return mixed

    def mix_car(self, origin, output):
        noise = self.car
        mixed = output + self.mix_suffix['car']
        combine_noise(origin, noise, mixed)
        return mixed

    def pitch_plus2(self, origin, output):
        db = self.volume['+2']
        output = output + self.transfer_suffix['p2']
        sound_stretch_pitch(origin, db, output)
        return output

    def pitch_plus1(self, origin, output):
        db = self.volume['+1']
        output = output + self.transfer_suffix['p1']
        sound_stretch_pitch(origin, db, output)
        return output

    def pitch_minus2(self, origin, output):
        db = self.volume['-2']
        output = output + self.transfer_suffix['m2']
        sound_stretch_pitch(origin, db, output)
        return output

    def pitch_minus1(self, origin, output):
        db = self.volume['-1']
        output = output + self.transfer_suffix['m1']
        sound_stretch_pitch(origin, db, output)
        return output

    def tempo_fast5(self, origin, output):
        percent = self.percent['+5']
        output = output + self.transfer_suffix['f5']
        sound_stretch_tempo(origin, percent, output)
        return output

    def tempo_slow5(self, origin, output):
        percent = self.percent['-5']
        output = output + self.transfer_suffix['s5']
        sound_stretch_tempo(origin, percent, output)
        return output

    def tempo_fast10(self, origin, output):
        percent = self.percent['+10']
        output = output + self.transfer_suffix['f10']
        sound_stretch_tempo(origin, percent, output)
        return output

    def tempo_slow10(self, origin, output):
        percent = self.percent['-10']
        output = output + self.transfer_suffix['s10']
        sound_stretch_tempo(origin, percent, output)
        return output

    def tempo_fast15(self, origin, output):
        percent = self.percent['+15']
        output = output + self.transfer_suffix['f15']
        sound_stretch_tempo(origin, percent, output)
        return output

    def tempo_slow15(self, origin, output):
        percent = self.percent['-15']
        output = output + self.transfer_suffix['s15']
        sound_stretch_tempo(origin, percent, output)
        return output

    def tempo_fast20(self, origin, output):
        percent = self.percent['+20']
        output = output + self.transfer_suffix['f20']
        sound_stretch_tempo(origin, percent, output)
        return output

    def tempo_slow20(self, origin, output):
        percent = self.percent['-20']
        output = output + self.transfer_suffix['s20']
        sound_stretch_tempo(origin, percent, output)
        return output

    def tempo_fast25(self, origin, output):
        percent = self.percent['+25']
        output = output + self.transfer_suffix['f25']
        sound_stretch_tempo(origin, percent, output)
        return output

    def tempo_slow25(self, origin, output):
        percent = self.percent['-25']
        output = output + self.transfer_suffix['s25']
        sound_stretch_tempo(origin, percent, output)
        return output

    def tempo_fast30(self, origin, output):
        percent = self.percent['+30']
        output = output + self.transfer_suffix['f30']
        sound_stretch_tempo(origin, percent, output)
        return output

    def tempo_slow30(self, origin, output):
        percent = self.percent['-30']
        output = output + self.transfer_suffix['s30']
        sound_stretch_tempo(origin, percent, output)
        return output

    @staticmethod
    def tempo_fast_random_1_12(origin, output):
        percent = '+' + str(random.randint(1, 12))
        output = output + '_tempo_fast' + percent + '.wav'
        sound_stretch_tempo(origin, percent, output)
        return output

    @staticmethod
    def tempo_slow_random_1_12(origin, output):
        percent = '-' + str(random.randint(1, 12))
        output = output + '_tempo_slow' + percent + '.wav'
        sound_stretch_tempo(origin, percent, output)
        return output

    @staticmethod
    def pitch_plus_random_1_2(origin, output):
        db = '+' + str(random.randint(1, 2))
        output = output + '_pitch_plus' + db + '.wav'
        sound_stretch_pitch(origin, db, output)
        return output

    @staticmethod
    def pitch_minus_random_1_2(origin, output):
        db = '-' + str(random.randint(1, 2))
        output = output + '_pitch_minus' + db + '.wav'
        sound_stretch_pitch(origin, db, output)
        return output

    # 对原音频作升降调或者变速的变换
    def trans_pitch_and_tempo_random(self, origin, output):
        # 从func_list随机选择一种变换方式
        # func_list = [self.pitch_plus1, self.pitch_plus2, self.pitch_minus1, self.pitch_minus2,
        #              self.tempo_fast5, self.tempo_fast10, self.tempo_fast15, self.tempo_fast20,
        #              self.tempo_fast25, self.tempo_fast30, self.tempo_slow5, self.tempo_slow10,
        #              self.tempo_slow15, self.tempo_slow20, self.tempo_slow25, self.tempo_slow30]

        func_list = [self.tempo_fast_random_1_12, self.tempo_slow_random_1_12,
                     self.pitch_plus_random_1_2, self.pitch_minus_random_1_2]

        func = random.choice(func_list)
        trans_file = func(origin, output)

        # 删除生成的文件夹里的原音频
        # os.remove(origin)

        return trans_file

    # 然后将变换后的音频与噪声混合
    def mix_trans_random(self, origin, output):
        # 从mixed_list随机选择一种噪声与原音频混合
        # mixed_list = [self.mix_rain, self.mix_dish, self.mix_human,
        #              self.mix_white, self.mix_cafe, self.mix_car]

        mixed_list = [self.mix_rain, self.mix_dish, self.mix_human,
                      self.mix_white, self.mix_cafe, self.mix_car]

        mixed = random.choice(mixed_list)
        mixed_file = mixed(origin, output)
        final_file = self.trans_pitch_and_tempo_random(mixed_file, output)

        # 删除生成的文件夹里的原音频
        # os.remove(origin)

        return final_file


def put_file_in_queue():
    input_wav_path = init_path + '/wav/'
    wav_list = os.listdir(input_wav_path)
    for wav in wav_list:
        wav_queue.append(wav)
    print('\n\nPut list in queue ok\n\n')
    return len(wav_list)


def run():
    while True:
        if wav_queue:
            wav_file = wav_queue.pop(0)

            # 进度显示
            # done_num[0] = done_num[0] + 1
            # if done_num[0] % 1000 == 0:
            #     print(done_num[0], '/', list_length)

            in_wav_file = init_path + '/wav/' + wav_file
            out_wav_file = output_path + '/wav/' + wav_file

            in_stm_file, in_stm_file_name, stm_content = read_stm(in_wav_file)

            # 先变换，再加噪声
            # final_file = rename_wav(mix.mix_trans_random(wav_file))

            # 只作语速变换，不加噪声
            final_file = rename_wav(mix.trans_pitch_and_tempo_random(in_wav_file, out_wav_file))

            final_wav_file_name = re.findall('/wav/.+', final_file)[0][5:]
            out_stm_file, out_stm_file_name = init_stm(final_file, stm_content)

            new_in_wav_file = all_path_wav + wav_file
            new_out_wav_file = all_path_wav + final_wav_file_name
            new_in_stm_file = all_path_stm + in_stm_file_name
            new_out_stm_file = all_path_stm + out_stm_file_name

            shutil.copy(in_wav_file, new_in_wav_file)
            shutil.copy(in_stm_file, new_in_stm_file)
            shutil.copy(final_file, new_out_wav_file)
            shutil.copy(out_stm_file, new_out_stm_file)

            # print('\n\n\n   ', wav_file, ' >>>>> ' + final_wav_file_name + '\n\n\n')
        else:
            break


def start():
    processes = []
    for i in range(12):
        t = multiprocessing.Process(target=run, args=())
        t.start()
        processes.append(t)

    for t in processes:
        t.join()

if __name__ == '__main__':
    wav_queue = multiprocessing.Manager().list()

    # done_num = multiprocessing.Manager().list()
    # done_num.append(0)

    mix = Mix()

    # 要转换的路径
    init_path = '/disk2/novel_temp_data/novel_1100h'

    # 生成的路径
    output_path = '/disk4/novel/novel_1100h_tempo_transfer'

    # 全部混合的路径
    all_path = '/disk4/novel/novel_1100h_tempo_transfer_with_origin_data'
    all_path_wav = all_path + '/wav/'
    all_path_stm = all_path + '/stm/'

    if not os.path.exists(output_path):
        os.makedirs(output_path + '/wav/', exist_ok=True)
        os.makedirs(output_path + '/stm/', exist_ok=True)
        os.makedirs(all_path_wav, exist_ok=True)
        os.makedirs(all_path_stm, exist_ok=True)

    list_length = put_file_in_queue()
    start()
