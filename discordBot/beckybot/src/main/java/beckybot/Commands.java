package beckybot;

import discord4j.core.GatewayDiscordClient;
import discord4j.core.event.domain.message.MessageCreateEvent;
import discord4j.core.object.entity.Message;
import discord4j.core.object.entity.channel.MessageChannel;
import discord4j.core.spec.Spec;

class Commands{

    public void init(GatewayDiscordClient gateway){
        
        gateway.on(MessageCreateEvent.class).subscribe(event ->{
            Message sMessage = event.getMessage();
            if(sMessage.getContent().equalsIgnoreCase("/ping")){
                try{
                    MessageChannel channel = sMessage.getChannel().block();
                    channel.createMessage("Pong!").block();
                }catch(NullPointerException npe){
                    System.err.println(npe.getMessage());
                }
            }

            else if(sMessage.getContent().equals("/help")){
                try{
                    MessageChannel channel = sMessage.getChannel().block();
                    channel.createEmbed(spec->
                        spec.setColor(Color.red)
                    ).block();

                }catch(NullPointerException npe){
                    System.err.println(npe.getMessage());
                }
            }

            else{
                System.err.println("Texting in bot chat");
                
            }
        });
    }
}