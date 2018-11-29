import subprocess32 as subprocess
import shlex
import sys

fonts = [
	"/Library/Fonts/Tahoma.ttf",
	"/Users/jason/Library/Fonts/FreeSans.ttf",
	"/Users/jason/Library/Fonts/FreeSansBold.ttf",
	"/Users/jason/Library/Fonts/FreeMono.ttf",
	"/Users/jason/Library/Fonts/FreeMonoBold.ttf",
	"/Users/jason/Library/Fonts/VCR_OSD_MONO_1.001.ttf",
	"/Users/jason/Library/Fonts/Retron2000.ttf",
	"/Users/jason/Library/Fonts/pt-mono.regular.ttf",
	"/Users/jason/Library/Fonts/pt-mono.bold.ttf",
]

sizes = [
	6,
	8,
	10,
	12,
	14,
	13,
	16,
	18,
	22,
	24,
	26,
	32,
	36,
	40,
	42,
	46,
	60
]

source = open("generate.py").read().replace("\n", "\n// ")
print("// Generated with generate.py:")
print("// " + source)
print()
sys.stdout.flush()
for font in fonts:
	for size in sizes:
		cmd = "./fontconvert %s %d 64 32 176" % (font, size)
		cmd = shlex.split(cmd)
		subprocess.call(cmd)