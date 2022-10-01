import moviepy.editor as mp

def task():
    audioclip = mp.AudioFileClip("input/song.mp3")
    image_clip =  mp.ImageClip("input/background.jpg", duration=audioclip.duration)
    # w,h = moviesize = out_video.size
    my_text = mp.TextClip("The Art of Adding Text on Video", font="Amiri-regular", color="white", fontsize=34)
    # txt_col = my_text.on_color(size=(out_video.w + my_text.w, my_text.h+5), color=(0,0,0), pos=(6,’center’), col_opacity=0.6)
    # txt_mov = txt_col.set_pos( lambda t: (max(w/30,int(w-0.5*w*t)),max(5*h/6,int(100*t))) )
    final = mp.CompositeVideoClip([image_clip,my_text,audioclip])

    final.write_videofile("output/music_video.mp4",fps=24,codec="libx264")


if __name__ == "__main__":
    task()
