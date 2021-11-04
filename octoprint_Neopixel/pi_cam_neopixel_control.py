#!/usr/bin/env python3
# Simple test for NeoPixels on Raspberry Pi
import sys
import os
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 12 

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.25, auto_write=False,
                           pixel_order=ORDER)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def rainbow(wait):
    for i in range(num_pixels):
        pixel_index = (i * 256 // num_pixels)
        pixels[i] = wheel(pixel_index & 255)
    pixels.show()
    time.sleep(wait)


def colorWipe(color, wait_ms=50):
    pixels.fill(color)
    pixels.show()
    time.sleep(wait_ms/1000.0)

def theaterChase(color, wait_ms=50, iterations=100):
    for j in range(iterations):
        for q in range(3):
            for i in range(0, num_pixels, 3):
                pixels[i + q] = color
            pixels.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, num_pixels, 3):
                pixels[i+q] = 0

def theaterChaseRainbow(wait_ms=50):
    for j in range(256):
        for q in range(3):
            for i in range(0, num_pixels, 3):
                pixels[i + q] = wheel((i + j) % 255)
            pixels.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, num_pixels, 3):
                pixels[i + q] = 0

if __name__ == '__main__':
    runtype = os.path.basename(__file__)
    if runtype == 'lightoff':
        colorWipe((0, 0, 0), 0)
    elif runtype == 'lighton':  # Turn on WHITE for camera
        pixels.brightness = float(0.5)
        colorWipe((255, 255, 255), 0)
    elif runtype == 'heating':
        theaterChase((127, 0, 0))
    elif runtype == 'cooling':
        theaterChase((0, 0, 127))
    elif runtype == 'rainbow':
        rainbow(0.001)
    elif runtype == 'cycle':
        rainbow_cycle(0.001)
    elif runtype == 'chase':
        theaterChaseRainbow()
    elif runtype == 'color':
        colorWipe((int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])), 0)
