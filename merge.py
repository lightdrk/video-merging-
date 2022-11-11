from moviepy.editor import *
import argparse


if __name__=='__main__':
	argparser = argparse.ArgumentParser()
	argparser.add_argument("--file", required=True, help="location1,location2 (in this format)")
	argparser.add_argument("--option",help="performance --option high,low,mid",default=None)
	args = argparser.parse_args()
		
print(args.file)

location = args.file

print(location)

location = location.split(',')

print(location)

clips = [VideoFileClip(n) for n in location]

print(clips)

#clip1 =VideoFileClip("/home/arch/Desktop/video merge/video/video1.mp4")
#clip2 = VideoFileClip("/home/arch/Desktop/video merge/video/video2.mp4")
final_clip = concatenate_videoclips(clips)

final_clip.to_videofile("output1.mp4",remove_temp=False,threads=args.option)

