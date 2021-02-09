package beckybot;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

import org.json.JSONArray;
import org.json.JSONObject;

class UrbanDictionaryQuery {
    public static String init(String s) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
		.uri(URI.create("https://mashape-community-urban-dictionary.p.rapidapi.com/define?term="+s))
		.header("x-rapidapi-key", "6a72219a16msh3734f02108b8544p1f2069jsnf4e0182985ed")
		.header("x-rapidapi-host", "mashape-community-urban-dictionary.p.rapidapi.com")
		.method("GET", HttpRequest.BodyPublishers.noBody())
		.build();
        HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
        
        JSONObject obj = new JSONObject(response.body());
        JSONArray arr = obj.getJSONArray("list");
        
        String sTerm = arr.getJSONObject(0).getString("definition");
        System.err.println(sTerm);
        return sTerm;
    }
}