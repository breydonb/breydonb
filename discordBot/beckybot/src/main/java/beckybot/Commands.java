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
                        spec.setColor(Color.red).setAuthor("setAuthor", "https://www.google.com/", "https://www.google.com/url?sa=i&url=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3AIcon_Bird_512x512.png&psig=AOvVaw3n3yUoXTJYD-B0e1H1bppw&ust=1612573008132000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOjc1NzE0e4CFQAAAAAdAAAAABAD").setImage(IMAGE_URL)
                        .setTitle("setTitle/setUrl")
                        .setUrl(ANY_URL)
                        .setDescription("setDescription\n" +
                          "big D: is setImage\n" +
                          "small D: is setThumbnail\n" +
                          "<-- setColor")
                        .addField("addField", "inline = true", true)
                        .addField("addFIeld", "inline = true", true)
                        .addField("addFile", "inline = false", false)
                        .setThumbnail(IMAGE_URL)
                        .setFooter("setFooter --> setTimestamp", https://www.google.com/url?sa=i&url=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3AIcon_Bird_512x512.png&psig=AOvVaw3n3yUoXTJYD-B0e1H1bppw&ust=1612573008132000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOjc1NzE0e4CFQAAAAAdAAAAABAD)
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
