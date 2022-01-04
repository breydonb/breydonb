public class Rover implements Critter{
    public Rover(){
        Snake s = new Snake();
    }

    @Override
    public char getChar() {
        return 0;
    }

    @Override
    public int getMove(int front, int back, int right, int left) {
        return 0;
    }
}