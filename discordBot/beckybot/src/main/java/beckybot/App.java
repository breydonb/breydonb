package beckybot;

import discord4j.core.DiscordClient;
import discord4j.core.GatewayDiscordClient;

public class App 
{
    public static void main( String[] args ){
        
        String sToken = "MzE3MDcwMDUwOTkxMjc2MDMy.WSYMfw.jYZr1urYWXt20YjSYYyX5cgHkSs";
        DiscordClient client = DiscordClient.create(sToken);
        GatewayDiscordClient gateway = client.login().block();

        Commands command = new Commands();
        try{
            command.init(gateway);
            gateway.onDisconnect().block();
        }
        catch(NullPointerException npe){
            System.err.println(npe.getMessage());
        }     

    }
}
