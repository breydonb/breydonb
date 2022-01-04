interface LibraryItem {
    int getID();
    String getTitle();
    String getAuthor();
}

class Book implements LibraryItem{
    
    private int bookID;
    private String title;
    private String author;

    public Book(int id, String title, String author){
        this.bookID = id;
        this.title = title;
        this.author = author;
    }

    @Override
    public int getID(){
        return bookID;
    }

    @Override
    public String getTitle(){
        return title;
    }

    @Override
    public String getAuthor() {
        return author;
    }
}

class Album implements LibraryItem{

    private int albumID;
    private String title;
    private String author;

    public Album(int id, String title, String author){
        this.albumID = id;
        this.title = title;
        this.author = author;
    }

    @Override
    public int getID() {
        return albumID;
    }

    @Override
    public String getTitle(){
        return title;
    }

    @Override
    public String getAuthor() {
        return author;
    }

}

class Magazine implements LibraryItem{

    private int albumID;
    private String title;
    private String author; 

    public Magazine(int id, String title, String author){
        this.albumID = id;
        this.title = title;
        this.author = author;
    }

    @Override
    public int getID() {
        return albumID;
    }

    @Override
    public String getTitle() {
        return title;
    }

    @Override
    public String getAuthor() {
        return author;
    }
}

public class Library{
    public static void main(String[] args){
        LibraryItem book = new Book(54321, "Building Java Programs", "Person");
        LibraryItem album = new Album(34021, "The Dark Side of the Moon", "Pink Floyd");
        LibraryItem magazine = new Magazine(63456, "KERRANG!", "Emily Carter");
        System.out.println(album.getAuthor()+ " "+ album.getTitle()+" ID: "+album.getID());
        System.out.println(book.getAuthor()+ " "+ book.getTitle()+" ID: "+book.getID());
        System.out.println(magazine.getAuthor()+ " "+ magazine.getTitle()+" ID: "+magazine.getID());
    }
}




