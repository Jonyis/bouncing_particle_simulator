from expenvelope import Envelope
from pygame import mixer
from scamp import Session, NotePlaybackAdjustment

from music_lookup import volumes, lengths, pitches


class SoundSystem:
    def __init__(self, collision_sound_path: str = "default_path"):
        mixer.init()
        mixer.set_num_channels(1000)
        s = Session(tempo=60, max_threads=200).run_as_server()

        self.__piano = s.new_part("piano")
        self.__collision_sound = mixer.Sound(collision_sound_path)
        self.__music_index = 0
        self.__note__effect = NotePlaybackAdjustment.scale_params(volume=Envelope([1, 0.0], [0.75], offset=0.0))

    def play_collision_sound(self):
        channel = mixer.find_channel(force=True)
        channel.queue(self.__collision_sound)

    def play_collision_sound_from_music(self):
        self.__piano.play_note(
            pitches[self.__music_index],
            volumes[self.__music_index],
            lengths[self.__music_index],
            self.__note__effect,
            blocking=False)
        self.__music_index += 1
        self.__music_index %= len(pitches)
