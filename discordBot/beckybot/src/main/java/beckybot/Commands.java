package beckybot;

import java.io.IOException;

import discord4j.core.GatewayDiscordClient;
import discord4j.core.event.domain.message.MessageCreateEvent;
import discord4j.core.object.entity.Message;
import discord4j.core.object.entity.User;
import discord4j.core.object.entity.channel.MessageChannel;
import discord4j.discordjson.json.UserData;
import discord4j.rest.util.Color;

class Commands {

    public void init(GatewayDiscordClient gateway) {

        gateway.on(MessageCreateEvent.class).subscribe(event -> {
            Message sMessage = event.getMessage();
            if(sMessage.getContent().startsWith("/")){
                if (sMessage.getContent().equalsIgnoreCase("/ping")) {
                    ping(sMessage);
                }
                else if (sMessage.getContent().equals("/help")) {
                    help(sMessage);
                }
                else if (sMessage.getContent().startsWith("/ud")) {
                    ud(sMessage);
                }
                else{
                    MessageChannel channel = sMessage.getChannel().block();
                    channel.createMessage("Unknown Command: Please feel free to use `/help to find all of the available commands!`").block();
                }
            }
            /*else if(sMessage.getContent().startsWith("[a-z]")){
                
            }*/
            else if(!sMessage.getContent().startsWith("/")){
                /*MessageChannel channel = sMessage.getChannel().block();
                System.err.println(sMessage.getAuthor());*/
                
            }
        });
    }

    public static void ping(Message sMessage){
        try {
            MessageChannel channel = sMessage.getChannel().block();
            long lTime = System.currentTimeMillis();
            channel.createMessage("Pong!").block();
            lTime = System.currentTimeMillis() - lTime;
            String sTime = Long.toString(lTime);
            channel.createMessage(sTime + " ms").block();
        } catch (NullPointerException npe) {
            System.err.println(npe.getMessage());
        }
    }

    public static void help(Message sMessage){
        try {
            MessageChannel channel = sMessage.getChannel().block();
            channel.createEmbed(spec -> spec.setColor(Color.RED)
                    .setAuthor("Becky Bot Let Me Smash", "https://www.google.com/",
                            "https://upload.wikimedia.org/wikipedia/commons/6/63/Icon_Bird_512x512.png")
                    .setTitle("Commands You Can Use").setUrl("https://www.google.com")
                    .setDescription("Based on your role, these are the commands that you have access to: ")
                    .addField("/help", "Provides the command you are reading right now!", true)
                    .addField("/ping", "Sends a response to the bot and ensures bot is actually working", true)
                    .addField("/p", "Allows you to play music in the preferred voice channel", true)
                    .addField("/s","Depending on the amount of people in your call, you can vote to skip a video/song",false)
                    .addField("/fs", "This is a force skip", true).addField("/ud", "Allows you to search for words on Urban Dictionary and get the definition for the item.", true)
                    .setThumbnail("https://www.google.com")).block();

        } catch (NullPointerException npe) {
            System.err.println(npe.getMessage());
        }
    }

    public static void ud(Message sMessage){
        MessageChannel channel = sMessage.getChannel().block();
        UrbanDictionaryQuery udQuery = new UrbanDictionaryQuery();
        //String[] aMessage = sMessage.getContent().toString().split(" ");
        String aMessage = sMessage.getContent().toString().replace("/ud","");
        String t = aMessage.replace(" ","%20");
        System.err.println(t);
        // channel.createMessage(udQuery.init(aMessage[1])).block();
        channel.createEmbed(spec -> {
            try {
                spec.setColor(Color.CYAN)
                        .setAuthor("Becky Bot Let Me Smash", "https://www.google.com",
                                "https://upload.wikimedia.org/wikipedia/commons/6/63/Icon_Bird_512x512.png")
                        .setTitle("Definition For: " + aMessage)
                        .setDescription(udQuery.init(t))
                        .addField("Test","test",true);
            } catch (IOException | InterruptedException e) {
                System.err.println(e.getMessage());
            }
        }
        ).block(); 
    }

}
