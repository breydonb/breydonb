package beckybot;

import com.sedmelluq.discord.lavaplayer.player.*;
//import com.sedmelluq.discord.lavaplayer.player.DefaultAudioPlayerManager;
import com.sedmelluq.discord.lavaplayer.source.AudioSourceManagers;
import com.sedmelluq.discord.lavaplayer.track.playback.NonAllocatingAudioFrameBuffer;

class PlayerCommand {
    public static final AudioPlayerManager apm;
    static{
        apm = new DefaultAudioPlayerManager();
        apm.getConfiguration().setFrameBufferFactory(NonAllocatingAudioFrameBuffer::new);
        AudioSourceManagers.registerRemoteSources(apm);
    }
}