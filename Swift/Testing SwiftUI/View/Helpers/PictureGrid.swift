//
//  PictureGrid.swift
//  Testing SwiftUI
//
//  Created by Breydon Brennan on 12/21/20.
//

import SwiftUI

struct PictureGrid: View {
    var image: Image;
    var body: some View {
        image.resizable().aspectRatio(contentMode:.fit).cornerRadius(25).frame(width:210, height:200)
    }
}


struct PictureGrid_Previews: PreviewProvider {
    static var previews: some View {
        HStack{
            PictureGrid(image: Image("IMG_0645"))
            PictureGrid(image: Image("IMG_0645"))
        }
    }
}
