//
//  EventList.swift
//  Testing SwiftUI
//
//  Created by Breydon Brennan on 12/20/20.
//

import SwiftUI

struct EventList: View {
    @EnvironmentObject var modelData: ModelData
    @State private var showFavorite = false;
    
    var filteringEvents: [Events]{
        modelData.events.filter{ events in
            (!showFavorite || events.isFavorite)
        }
        
    }
    
    var body: some View {
        NavigationView{
            List{
                Toggle(isOn: $showFavorite, label: {
                    Text("Favorites")
                })
                ForEach(filteringEvents){events in
                    NavigationLink(destination:EventDetails(events:events)){
                        EventViewer(events: events)
                    }
                }
            }.navigationBarTitle(Text("Trips with the Boys"))
        }
    }
}

struct EventList_Previews: PreviewProvider {
    static var previews: some View {
        EventList()
    }
}
