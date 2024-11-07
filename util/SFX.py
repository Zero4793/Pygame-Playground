import pygame
# import time
import numpy as np

# pygame.init()
pygame.mixer.init()

def note(frequency, duration, volume=1.0, earRatio=.5):
	sample_rate = 44100 # 44.1kHz is standard

	t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
	amplitude = 32767 * volume  # Max amplitude for 16-bit audio

	waveform = amplitude * np.sin(2 * np.pi * frequency * t)

	# Apply fade-in and fade-out to the waveform
	fade_duration = 0.01  # Fade duration in seconds (10 milliseconds)
	fade_samples = int(sample_rate * fade_duration)

	# Create fade-in and fade-out envelopes
	fade_in = np.linspace(0, 1, fade_samples)
	fade_out = np.linspace(1, 0, fade_samples)

	# Apply the fade-in envelope
	waveform[:fade_samples] *= fade_in

	# Apply the fade-out envelope
	waveform[-fade_samples:] *= fade_out

	waveform_left = waveform * earRatio
	waveform_right = waveform * (1 - earRatio)

	audio_data = np.stack((waveform_left, waveform_right), axis=-1)
	audio_data = audio_data.astype(np.int16)

	sound = pygame.sndarray.make_sound(audio_data)
	sound.play()
	# pygame.time.delay(int(duration * 1000))
	# sound.stop()


# for i in range(10):
# 	frequency = 300-i*2
# 	duration = 0.4
# 	note(frequency, duration,1,1-i/10)
# 	time.sleep(duration)

# pygame.quit()
