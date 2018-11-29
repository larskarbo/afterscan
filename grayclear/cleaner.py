from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import sys
import click
import datetime
import os.path
from progress.bar import ChargingBar
import time
from art import *
import emoji

defaultThreshold = 100
@click.command()
@click.argument("filename")
@click.option('--threshold', default=defaultThreshold, help='Threshold value between 0 and 255. Default=100')
@click.option('--out', '-o', default='', help='Output path. Default afterscan-[filename] in pwd')
@click.option('--invert/--no-invert', '-i', default=False, help='Invert the image')
@click.option('--force/--no-force', '-f', default=False, help='Overwrite existing file without asking')
def main(filename, threshold, out, invert, force):
    Art = text2art("Afterscan")
    print(Art)
    print(emoji.emojize(
        ':thumbs_up: Turn sloppy photoscans into crisp black/white masterpieces :thumbs_up:'))
    print(' ')
    print('------------------')
    print(' ')
    if len(filename) is 0:
        sys.exit()
    # Read image
    im = Image.open(filename)

    # bar = ChargingBar('goiiinnng', fill='@',
    #                   suffix='%(percent)d%%')
    # time.sleep(3)
    text = 'Threshold (--threshold): '
    bar = ChargingBar(text, max=255, suffix=str(threshold) + '/255')
    for i in range(threshold):
        bar.next()
    bar.finish()



    transition = threshold + 20

    def ttt(value):
        if value < threshold:
            return 0
        elif value < transition:
            return (value - threshold) / (transition - threshold) * 255
        else:
            return 255

    im2 = im.convert('L').point(ttt)

    if invert:
        im2 = ImageOps.invert(im2)

    if len(out) == 0:
        out = os.getcwd() + '/afterscan-' + os.path.basename(filename)

    if os.path.exists(out) and not force:
        print(' ')
        print('ERROR!!!')
        print('File ' + out + ' already exists! Use --force to overwrite')
        print(' ')
        sys.exit()

    im2.save(out)
    print(' ')
    print(emoji.emojize(':heavy_check_mark:  Optimized image saved as ' + out))
    print(' ')

if __name__ == '__main__':
    main()
