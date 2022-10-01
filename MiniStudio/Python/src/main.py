import moviepy.editor as mp
import pylrc

def get_lyrics():
    lrc_file = open('example.lrc')
lrc_string = ''.join(lrc_file.readlines())
lrc_file.close()

subs = pylrc.parse(lrc_string

def task():
    audio = mp.AudioFileClip("input/song.mp3")
    image_clip =  mp.ImageClip("input/background.jpg").set_duration(audio.duration)
    # w,h = moviesize = out_video.size
    text = mp.TextClip("The Art of Adding Text on Video", font='Liberation-Sans', color="white", fontsize=34)
    video_clip = image_clip.set_audio(audio)
    # txt_mov = txt_col.set_pos( lambda t: (max(w/30,int(w-0.5*w*t)),max(5*h/6,int(100*t))) )
    
    video_clip = mp.CompositeVideoClip([video_clip, text])

    video_clip.set_duration(audio.duration).write_videofile("output/music_video.mp4",fps=24,codec="libx264")



if __name__ == "__main__":
    task()
