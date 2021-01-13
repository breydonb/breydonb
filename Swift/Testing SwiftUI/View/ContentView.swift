//
//  ContentView.swift
//  Testing SwiftUI
//
//  Created by Breydon Brennan on 12/19/20.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        //EventDetails();
        EventList();
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView().environmentObject(ModelData())
    }
}
