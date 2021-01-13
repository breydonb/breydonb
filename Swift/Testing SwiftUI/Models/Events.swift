//
//  File.swift
//  Testing SwiftUI
//
//  Created by Breydon Brennan on 12/20/20.
//

import Foundation
import SwiftUI
import CoreLocation

struct Events: Hashable, Codable, Identifiable{
    var id: Int;
    var name: String;
    var city: String;
    var state: String;
    //var month: String;
    var eventDate: String;
    var isFavorite: Bool;
    var eventDescription: String;
    
    var imageName: String;
    var image: Image{
        Image(imageName);
    }
    
    var imageGrid: String;
    var imageG: Image{
        Image(imageGrid);
    }
    
    private var coordinates: Coordinates
    
    var locationCoordinate: CLLocationCoordinate2D {
        CLLocationCoordinate2D(
            latitude: coordinates.latitude, longitude: coordinates.longitude)
    }
    
    struct Coordinates: Hashable, Codable{
        var latitude: Double;
        var longitude: Double;
    }
}
