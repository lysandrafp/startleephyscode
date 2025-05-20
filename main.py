import Mock.GPIO as GPIO
import time
import random
from datetime import datetime
import pygame

# GPIO setup here
TTL_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(TTL_PIN, GPIO.OUT)
GPIO.output([TTL_PIN], GPIO.LOW)

# Initialize audio system
pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)
sound = pygame.mixer.Sound("/home/paul/Desktop/scientific_programming/white-noise-0.5s.wav")

# Log file
with open("ttl_pulse_log.txt", "w") as log_file:
    for i in range(30):
        # TTL pulse
        GPIO.output([TTL_PIN], GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output([TTL_PIN], GPIO.LOW)

        # Log timestamp
        now = datetime.now()
        log_msg = f"Pulse {i+1}: {now.strftime('%Y-%m-%d %H:%M:%S.%f')}"
        print(log_msg)
        log_file.write(log_msg + "\n")
        log_file.flush()

        # Play sound
        sound.play()
        time.sleep(0.5)  # Wait for sound to finish

        if i < 29:
            wait_time = random.uniform(10, 30)
            print(f"Waiting for {wait_time:.2f} seconds...\n")
            time.sleep(wait_time)

# Cleanup
GPIO.cleanup()
pygame.mixer.quit()
