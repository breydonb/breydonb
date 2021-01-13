import SwiftUI

struct EventViewer: View {
    var events: Events

    var body: some View {
        HStack{
            events.image.resizable().aspectRatio(contentMode:.fit).frame(width: 200,height: 200)
            Text(events.name).foregroundColor(.green).font(.headline).padding()
            Spacer()
            if(events.isFavorite){
                Image(systemName: "star.fill").foregroundColor(.yellow).padding()
            }
        }
    }
}

struct EventViewer_Previews: PreviewProvider {
    static var events = ModelData().events
    static var previews: some View {
        Group{
            EventViewer(events: events[0])
            EventViewer(events: events[1])
        }.previewLayout(.fixed(width:500,height:100))
    }
}
