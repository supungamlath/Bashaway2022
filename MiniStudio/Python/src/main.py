import moviepy.editor as mp
import pylrc

def get_lyrics():
    with open('input/song.lrc') as lrc_file:
        lrc_string = ''.join(lrc_file.readlines())
        return pylrc.parse(lrc_string)

def task():
    audio = mp.AudioFileClip("input/song.mp3")
    image_clip =  mp.ImageClip("input/background.jpg")
    video_clip = image_clip.set_audio(audio)

    lyrics = get_lyrics()
    text_clips = []

    for i, lyric in enumerate(lyrics): 
        duration = 5
        if (lyric != lyrics[-1]):
            duration = lyrics[i+1].time - lyric.time

        text = mp.TextClip(lyric.text, font='Liberation-Sans', color="white", fontsize=100, size=(video_clip.size[0]-20, video_clip.size[1]-20), method="caption")
        text = text.set_duration(duration).set_start(lyric.time, change_end=True).set_position(("center","center"))
        text_clips.append(text)    

    video_clip = mp.CompositeVideoClip([video_clip, *text_clips]).set_duration(audio.duration)

    video_clip.write_videofile("output/music_video.mp4", fps=22)


if __name__ == "__main__":
    task()
