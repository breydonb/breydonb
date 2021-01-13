//
//  MapView.swift
//  Testing SwiftUI
//
//  Created by Breydon Brennan on 12/19/20.
//

import SwiftUI
import MapKit

struct MapView: View {
    var coordinate: CLLocationCoordinate2D;
    @State private var region = MKCoordinateRegion()
    
    var body: some View {
        Map(coordinateRegion: $region).onAppear{
            setRegion(coordinate)
        }
    }
    
    private func setRegion(_ coordinate:CLLocationCoordinate2D){
        region = MKCoordinateRegion(
            center : coordinate,
            span : MKCoordinateSpan(latitudeDelta: 0.05, longitudeDelta: 0.05)
        )
    }
}

struct MapView_Previews: PreviewProvider {
    static var previews: some View {
        MapView(coordinate: CLLocationCoordinate2D(latitude:41.85051588227039,longitude:-87.61534316022318))
    }
}
