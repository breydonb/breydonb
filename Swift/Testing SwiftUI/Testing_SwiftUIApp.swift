//
//  Testing_SwiftUIApp.swift
//  Testing SwiftUI
//
//  Created by Breydon Brennan on 12/19/20.
//

import SwiftUI

@main
struct Testing_SwiftUIApp: App {
    @StateObject private var modelData = ModelData()
    var body: some Scene {
        WindowGroup {
            ContentView().environmentObject(modelData)
        }
    }
}
