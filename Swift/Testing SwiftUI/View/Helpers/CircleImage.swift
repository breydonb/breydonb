//
//  CircleImage.swift
//  Testing SwiftUI
//
//  Created by Breydon Brennan on 12/19/20.
//

import SwiftUI

struct CircleImage: View {
    var image: Image;
    var body: some View {
        image
            .resizable()
            .aspectRatio(contentMode:.fit)
                .clipShape(Circle())
                    .overlay(Circle().stroke(Color.blue, lineWidth: 2))
                    .shadow(radius: 7);
    }
}

struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage(image: Image("St.LouisX2"))
    }
}
