# encoding=utf-8
import wave
# import subprocess

aa = 'rain3_'
# for i in range(4):
#     i = i + 1
#     subprocess.call('ffmpeg -i C:\\Users\\Fongim\\Desktop\\Python_work\\wav_transfer\\noise\\'
#                     + aa + str(i) + '.wav -af volume=-12dB '
#                     + 'C:\\Users\\Fongim\\Desktop\\Python_work\\wav_transfer\\noise1\\'
#                     + aa + str(i) + '.wav -y')

fr = wave.open('C:\\Users\\Fongim\\Desktop\\Python_work\\wav_transfer\\noise\\cafe.wav', 'rb')
print(fr.getparams())


'''

        self.pitch_plus1(origin)
        self.pitch_plus2(origin)
        self.pitch_minus1(origin)
        self.pitch_minus2(origin)
        self.tempo_fast10(origin)
        self.tempo_fast20(origin)
        self.tempo_fast30(origin)
        self.tempo_slow10(origin)
        self.tempo_slow20(origin)
        self.tempo_slow30(origin)

        self.o_restaurant_dish = ['restaurant_dish_1.wav', 'restaurant_dish_2.wav', 'restaurant_dish_3.wav',
                                  'restaurant_dish_4.wav', 'restaurant_dish_5.wav', 'restaurant_dish_6.wav',
                                  'restaurant_dish_7.wav', 'restaurant_dish_8.wav', 'restaurant_dish_9.wav']
        self.o_restaurant_human = ['restaurant_human_1.wav', 'restaurant_human_2.wav', 'restaurant_human_3.wav',
                                   'restaurant_human_4.wav', 'restaurant_human_5.wav', 'restaurant_human_6.wav',
                                   'restaurant_human_7.wav', 'restaurant_human_8.wav', 'restaurant_human_9.wav',
                                   'restaurant_human_10.wav', 'restaurant_human_11.wav', 'restaurant_human_12.wav',
                                   'restaurant_human_13.wav', 'restaurant_human_14.wav', 'restaurant_human_15.wav',
                                   'restaurant_human_16.wav', 'restaurant_human_17.wav', 'restaurant_human_18.wav',
                                   'restaurant_human_19.wav']
                                   
    def mix_rain_pitch_plus3(self, origin):
        noise = random.choice(self.rain)
        db = self.volume['+3']
        tmp = origin + '_pitch_plus3_mix_rain.wav'
        sound_stretch_pitch(origin, db, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed

    def mix_rain_pitch_plus6(self, origin):
        noise = random.choice(self.rain)
        db = self.volume['+6']
        tmp = origin + '_pitch_plus6_mix_rain.wav'
        sound_stretch_pitch(origin, db, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed

    def mix_rain_pitch_minus3(self, origin):
        noise = random.choice(self.rain)
        db = self.volume['-3']
        tmp = origin + '_pitch_minus3_mix_rain.wav'
        sound_stretch_pitch(origin, db, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed

    def mix_rain_pitch_minus6(self, origin):
        noise = random.choice(self.rain)
        db = self.volume['-6']
        tmp = origin + '_pitch_minus6_mix_rain.wav'
        sound_stretch_pitch(origin, db, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed
    
    def mix_rain_tempo_fast10(self, origin):
        noise = random.choice(self.rain)
        percent = self.percent['+10']
        tmp = origin + '_tempo_fast10_mix_rain.wav'
        sound_stretch_tempo(origin, percent, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed

    def mix_rain_tempo_slow10(self, origin):
        noise = random.choice(self.rain)
        percent = self.percent['-10']
        tmp = origin + '_tempo_slow10_mix_rain.wav'
        sound_stretch_tempo(origin, percent, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed

    def mix_restaurant_human_pitch_plus3(self, origin):
        noise = random.choice(self.restaurant_human)
        db = self.volume['+3']
        tmp = origin + '_pitch_plus3_mix_restaurant_human.wav'
        sound_stretch_pitch(origin, db, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed
    
    def mix_restaurant_human_pitch_plus6(self, origin):
        noise = random.choice(self.restaurant_human)
        db = self.volume['+6']
        tmp = origin + '_pitch_plus6_mix_restaurant_human.wav'
        sound_stretch_pitch(origin, db, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed
    
    def mix_restaurant_human_pitch_minus3(self, origin):
        noise = random.choice(self.restaurant_human)
        db = self.volume['-3']
        tmp = origin + '_pitch_plus3_mix_restaurant_human.wav'
        sound_stretch_pitch(origin, db, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed
    
    def mix_restaurant_human_pitch_minus6(self, origin):
        noise = random.choice(self.restaurant_human)
        db = self.volume['-6']
        tmp = origin + '_pitch_minus6_mix_restaurant_human.wav'
        sound_stretch_pitch(origin, db, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed
    
    def mix_restaurant_human_tempo_fast10(self, origin):
        noise = random.choice(self.restaurant_human)
        percent = self.percent['+10']
        tmp = origin + '_tempo_fast10_mix_restaurant_human.wav'
        sound_stretch_tempo(origin, percent, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed

    def mix_restaurant_human_tempo_slow10(self, origin):
        noise = random.choice(self.restaurant_human)
        percent = self.percent['-10']
        tmp = origin + '_tempo_slow10_mix_restaurant_human.wav'
        sound_stretch_tempo(origin, percent, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed

    def mix_restaurant_dish_pitch_plus3(self, origin):
        noise = random.choice(self.restaurant_dish)
        db = self.volume['+3']
        tmp = origin + '_pitch_plus3_mix_restaurant_dish.wav'
        sound_stretch_pitch(origin, db, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed
    
    def mix_restaurant_dish_pitch_plus6(self, origin):
        noise = random.choice(self.restaurant_dish)
        db = self.volume['+6']
        tmp = origin + '_pitch_plus6_mix_restaurant_dish.wav'
        sound_stretch_pitch(origin, db, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed
    
    def mix_restaurant_dish_pitch_minus3(self, origin):
        noise = random.choice(self.restaurant_dish)
        db = self.volume['-3']
        tmp = origin + '_pitch_minus3_mix_restaurant_dish.wav'
        sound_stretch_pitch(origin, db, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed
    
    def mix_restaurant_dish_pitch_minus6(self, origin):
        noise = random.choice(self.restaurant_dish)
        db = self.volume['-6']
        tmp = origin + '_pitch_minus6_mix_restaurant_dish.wav'
        sound_stretch_pitch(origin, db, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed

    def mix_restaurant_dish_tempo_fast10(self, origin):
        noise = random.choice(self.restaurant_dish)
        percent = self.percent['+10']
        tmp = origin + '_tempo_fast10_mix_restaurant_dish.wav'
        sound_stretch_tempo(origin, percent, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed

    def mix_restaurant_dish_tempo_slow10(self, origin):
        noise = random.choice(self.restaurant_dish)
        percent = self.percent['-10']
        tmp = origin + '_tempo_slow10_mix_restaurant_dish.wav'
        sound_stretch_tempo(origin, percent, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed
    
    def mix_white_pitch_plus3(self, origin):
        noise = self.white
        db = self.volume['+3']
        tmp = origin + '_pitch_plus3_mix_white.wav'
        sound_stretch_pitch(origin, db, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed

    def mix_white_pitch_plus6(self, origin):
        noise = self.white
        db = self.volume['+6']
        tmp = origin + '_pitch_plus6_mix_white.wav'
        sound_stretch_pitch(origin, db, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed
    
    def mix_white_pitch_minus3(self, origin):
        noise = self.white
        db = self.volume['-3']
        tmp = origin + '_pitch_minus3_mix_white.wav'
        sound_stretch_pitch(origin, db, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed
    
    def mix_white_pitch_minus6(self, origin):
        noise = self.white
        db = self.volume['-6']
        tmp = origin + '_pitch_minus6_mix_white.wav'
        sound_stretch_pitch(origin, db, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed
    
    def mix_white_tempo_fast10(self, origin):
        noise = self.white
        percent = self.percent['+10']
        tmp = origin + '_tempo_fast10_mix_white.wav'
        sound_stretch_pitch(origin, percent, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed
    
    def mix_white_tempo_slow10(self, origin):
        noise = self.white
        percent = self.percent['-10']
        tmp = origin + '_tempo_slow10_mix_white.wav'
        sound_stretch_pitch(origin, percent, tmp)
        mixed = tmp
        combine_noise(tmp, noise, mixed)
        return mixed

    
def all_trans(file):
    mix = Mix()

    mix.pitch_plus3(file)
    mix.pitch_plus6(file)
    mix.pitch_minus3(file)
    mix.pitch_minus6(file)
    mix.tempo_fast10(file)
    mix.tempo_slow10(file)

    mix.mix_rain(file)
    mix.mix_restaurant_dish(file)
    mix.mix_restaurant_human(file)
    mix.mix_white(file)

    mix.mix_rain_pitch_plus3(file)
    mix.mix_rain_pitch_plus6(file)
    mix.mix_rain_pitch_minus3(file)
    mix.mix_rain_pitch_minus6(file)
    mix.mix_rain_tempo_fast10(file)
    mix.mix_rain_tempo_slow10(file)

    mix.mix_restaurant_dish_pitch_plus3(file)
    mix.mix_restaurant_dish_pitch_plus6(file)
    mix.mix_restaurant_dish_pitch_minus3(file)
    mix.mix_restaurant_dish_pitch_minus6(file)
    mix.mix_restaurant_dish_tempo_fast10(file)
    mix.mix_restaurant_dish_tempo_slow10(file)

    mix.mix_restaurant_human_pitch_plus3(file)
    mix.mix_restaurant_human_pitch_plus6(file)
    mix.mix_restaurant_human_pitch_minus3(file)
    mix.mix_restaurant_human_pitch_minus6(file)
    mix.mix_restaurant_human_tempo_fast10(file)
    mix.mix_restaurant_human_tempo_slow10(file)

    mix.mix_white_pitch_plus3(file)
    mix.mix_white_pitch_plus6(file)
    mix.mix_white_pitch_minus3(file)
    mix.mix_white_pitch_minus6(file)
    mix.mix_white_tempo_fast10(file)
    mix.mix_white_tempo_slow10(file)
'''