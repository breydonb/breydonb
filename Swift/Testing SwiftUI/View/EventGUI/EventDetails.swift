//
//  EventDetails.swift
//  Testing SwiftUI
//
//  Created by Breydon Brennan on 12/20/20.
//

import SwiftUI

struct EventDetails: View {
    @EnvironmentObject var modelData: ModelData;
    var events: Events;
    
    var eventIndex: Int{
        modelData.events.firstIndex(where: {$0.id == events.id})!
    }
    
    var body: some View {
        ScrollView(.vertical){
            
            MapView(coordinate: events.locationCoordinate).ignoresSafeArea(edges: .top).frame(height: 300)
            
            CircleImage(image: events.image).offset(y:-130).padding(.bottom, -130);
            
            VStack(alignment:.leading){
                HStack{
                    Text(events.name).font(.title).foregroundColor(.orange);
                    Spacer();
                    FavoriteButton(isSet: $modelData.events[eventIndex].isFavorite)
                }
        
                Spacer();
                
                HStack(){
                    Text(events.eventDate)
                        .font(.subheadline);
                    Spacer();
                    Text(events.city + ", "+events.state).font(.subheadline);
                }
                .font(.subheadline).foregroundColor(.secondary)
                
                Divider()
            
                Text("Description of Event").font(.title2).foregroundColor(.orange)
                Spacer();
                Text(events.eventDescription)
                
                
            }.padding() //padding goes here because it is for the entire set of items in the "grid"
        }.navigationTitle(events.name).navigationBarTitleDisplayMode(.inline)
        Spacer();
        //PictureGrid(image: events.imageG)
    }
}

struct EventDetails_Previews: PreviewProvider {
    static let modelData = ModelData();
    static var previews: some View {
        EventDetails(events : ModelData().events[0]).environmentObject(modelData)
    }
}
