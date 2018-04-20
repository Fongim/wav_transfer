from pydub import AudioSegment

wav = "tt1.wav"
noise = "rain3_1.wav"
path = "C:\\Users\\Fongim\\Desktop\\Python_work\\wav_transfer\\wav\\"
sound1 = AudioSegment.from_file(path + wav)
sound2 = AudioSegment.from_file(path + noise)

combined = sound1.overlay(sound2)

combined.export(path + wav, format='wav')

rain = ['rain1_1.wav', 'rain1_2.wav', 'rain1_3.wav', 'rain1_4.wav', 'rain2_1.wav', 'rain2_2.wav',
        'rain2_3.wav', 'rain3_1.wav', 'rain3_2.wav', 'rain3_3.wav', 'rain3_4.wav']

path = '/disk3/noise/'

new_rain = [path + i for i in rain]

print(new_rain)