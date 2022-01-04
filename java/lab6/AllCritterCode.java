/**
 * This file contains the Critter interface and several classes so it is easier to
 * start this project (down load one file rather than five).  
 * 
 * Place this file into a project, add public class Rover implements Critter and
 * you can run the simulation by running this class as a Java Application.  
 * Other new critters will require that you "un-comment" the model.add messages in 
 * order to get more Critters added to the simulation.  You can add more than five 
 * if you wish as long as each new class implement the Critter interface.
 *    
 * @author mercer
 */
import java.util.*;
import java.awt.*;
import javax.swing.*;
import javax.swing.event.*;
import java.awt.event.*;

public class AllCritterCode {

  public static void main(String[] args) {
    CritterModel model = new CritterModel(100, 50);

    /** Add critters here * */
    // This will not compile until you add a class named Rover that implements
    // the critters interface (initially an error without Rover.java)
    model.add(50, Rover.class);

    // Un-comment each line for each of the other four Critters
    // model.add(50, LandMine.class);
    // model.add(50, Food.class);
    // model.add(50, Wanderer.class);
    // model.add(50, FlyTrap.class);

    // Use the name of you unique Critter
    // model.add(50, MyCritterOrWhateverYouCalledIt.class);

    /** ******************** */
    /** Don't make any changes below here */
    /** ******************** */

    CritterFrame f = new CritterFrame(model);
    f.setVisible(true);
  }
}

// Michael Brooks
// 09/10/01
//
// The Critter interface specifies the methods a class must implement
// to be able to participate in the critter simulation, as well as defines
// various constants to be used throughout the Critter classes.
//
// The getChar method should return a character that will be used for
// displaying the Critter in the window, and the getMove method should
// return a legal move given the current surroundings.
//
// The move should be specified using the constants of this class
// {HOP, LEFT, RIGHT, INFECT}. The four parameters to getMove specify what is
// surrounding the critter using constants from the CritterModel class {WALL,
// EMPTY, SAME, OTHER}.
interface Critter {
  // The character that will represent this Critter in the GUI
  public char getChar();

  // The strategy employed for making a move
  public int getMove(int front, int back, int right, int left);

  // Surroundings constants passed as arguments
  // front == Critter.WALL is true if a wall is in front of this critter
  // front == Critter.OTHER is true, there is a Critter in front of
  //  this Critter object that is NOT of the same class. 
  public static final int WALL = 0;
  public static final int EMPTY = 1;
  public static final int SAME = 2;
  public static final int OTHER = 3;

  // move constants to be returned by getMove
  public static final int HOP = 0;
  public static final int LEFT = 1;
  public static final int RIGHT = 2;
  public static final int INFECT = 3;
}

// Stuart Reges
// 1/26/00
//
// Class CritterModel keeps track of the state of the critter simulation.

class CritterModel {
  public CritterModel(int width, int height) {
    myWidth = width;
    myHeight = height;
    myGrid = new Critter[width][height];
    myList = new Hashtable<Critter, Position>();
  }

  public void add(int number, Class critter) {
    if (myList.size() + number > myWidth * myHeight)
      throw new RuntimeException("adding too many critters");
    for (int i = 0; i < number; i++) {
      Critter next;
      try {
        next = (Critter) critter.newInstance();
      }
      catch (Exception e) {
        throw new RuntimeException("" + e);
      }
      int x, y;
      do {
        x = randomInt(0, myWidth - 1);
        y = randomInt(0, myHeight - 1);
      } while (myGrid[x][y] != null);
      myGrid[x][y] = next;
      myList.put(next, new Position(x, y, randomInt(0, 3)));
    }
  }

  private int randomInt(int low, int high) {
    return low + (int) (Math.random() * (high - low + 1));
  }

  public int getWidth() {
    return myWidth;
  }

  public int getHeight() {
    return myHeight;
  }

  public char getChar(int x, int y) {
    if (myGrid[x][y] == null)
      return '.';
    else
      return myGrid[x][y].getChar();
  }

  public Position getOther(Position p) {
    Position other = new Position(p.x, p.y, p.direction);
    if (p.direction == NORTH)
      other.y--;
    else if (p.direction == EAST)
      other.x++;
    else if (p.direction == SOUTH)
      other.y++;
    else if (p.direction == WEST)
      other.x--;
    else
      throw new RuntimeException("illegal direction");
    return other;

  }

  private boolean inBounds(int x, int y) {
    return (x >= 0 && x < myWidth && y >= 0 && y < myHeight);
  }

  private boolean inBounds(Position p) {
    return inBounds(p.x, p.y);
  }

  private int getStatus(int x, int y, Class original) {
    if (!inBounds(x, y))
      return Critter.WALL;
    else if (myGrid[x][y] == null)
      return Critter.EMPTY;
    else if (myGrid[x][y].getClass() == original)
      return Critter.SAME;
    else
      return Critter.OTHER;
  }

  public void update() {
    Object[] list = myList.keySet().toArray();
    shuffle(list);
    for (int i = 0; i < list.length; i++) {
      Critter next = (Critter) list[i];
      Position p = (Position) myList.get(next);
      if (p == null) // happens when creature was infected earlier in
        // this round
        continue;
      Position other = getOther(p);

      // the following tricky code gets the info about surrounding
      // neighbors
      // the xs and ys arrays along with the expressions involving % 4
      // handle
      // direction
      int xs[] = { p.x, p.x + 1, p.x, p.x - 1 };
      int ys[] = { p.y - 1, p.y, p.y + 1, p.y };
      Class mine = next.getClass();
      int move = next
          .getMove(getStatus(xs[p.direction], ys[p.direction], mine),
              getStatus(xs[(2 + p.direction) % 4], ys[(2 + p.direction) % 4],
                  mine), getStatus(xs[(1 + p.direction) % 4],
                  ys[(1 + p.direction) % 4], mine), getStatus(
                  xs[(3 + p.direction) % 4], ys[(3 + p.direction) % 4], mine));
      if (move == Critter.LEFT)
        p.direction = (p.direction + 3) % 4;
      else if (move == Critter.RIGHT)
        p.direction = (p.direction + 1) % 4;
      else if (move == Critter.HOP) {
        if (inBounds(other) && myGrid[other.x][other.y] == null) {
          myGrid[other.x][other.y] = myGrid[p.x][p.y];
          myGrid[p.x][p.y] = null;
          myList.put(next, other);
        }
      }
      else if (move == Critter.INFECT) {
        if (inBounds(other)
            && myGrid[other.x][other.y] != null
            && myGrid[other.x][other.y].getClass() != myGrid[p.x][p.y]
                .getClass()) {
          myList.remove(myGrid[other.x][other.y]);
          try {
            myGrid[other.x][other.y] = (Critter) myGrid[p.x][p.y].getClass()
                .newInstance();
          }
          catch (Exception e) {
            throw new RuntimeException("" + e);
          }
          myList.put(myGrid[other.x][other.y], other);
        }
      }
    }
  }

  private void shuffle(Object[] list) {
    for (int i = 0; i < list.length; i++) {
      int j = randomInt(0, list.length - 1);
      Object temp = list[i];
      list[i] = list[j];
      list[j] = temp;
    }
  }

  private int myHeight;

  private int myWidth;

  private Critter[][] myGrid;

  private Hashtable<Critter, Position> myList;

  private static final int NORTH = 0;

  private static final int EAST = 1;

  private static final int SOUTH = 2;

  private static final int WEST = 3;

  private class Position {
    public Position(int x, int y, int direction) {
      this.x = x;
      this.y = y;
      this.direction = direction;
    }

    public int x;

    public int y;

    public int direction;
  }
}

// Stuart Reges
// 1/26/00
// grader: self
//
// Class CritterPanel displays a grid of critters

class CritterPanel extends JPanel {

  public static final int FONT_SIZE = 10;

  private CritterModel myModel;

  private Font myFont;

  public CritterPanel(CritterModel model) {
    myModel = model;
    // construct font and compute char width once in constructor
    // for efficiency
    myFont = new Font("Monospaced", Font.BOLD, FONT_SIZE);
    setBackground(Color.cyan);
  }

  public void paintComponent(Graphics g) {
    super.paintComponent(g);
    g.setFont(myFont);
    int height = myModel.getHeight();
    int width = myModel.getWidth();
    // because font is monospaced, all widths should be the same;
    // so we can get char width from any char (in this case x)
    int charWidth = g.getFontMetrics().charWidth('x');
    int extraX = getWidth() - (width + 1) * charWidth;
    int extraY = getHeight() - (height - 1) * FONT_SIZE;
    for (int i = 0; i < width; i++)
      for (int j = 0; j < height; j++) {
        if (myModel.getChar(i, j) != '.')
          g.drawString("" + myModel.getChar(i, j), extraX / 2 + i * charWidth,
              extraY / 2 + j * FONT_SIZE);
      }
  }

}

// Stuart Reges
// 1/26/00
//
// Class CritterFrame provides the user interface for a simple simulation
// program.

class CritterFrame extends JFrame {
  public CritterFrame(CritterModel model) {
    // create frame and order list
    setTitle("CS227 critter simulation");
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    Container contentPane = getContentPane();
    myModel = model;

    // set up critter picture panel and set size
    myPicture = new CritterPanel(myModel);
    setSize(CritterPanel.FONT_SIZE * model.getWidth() / 2 + 150,
        CritterPanel.FONT_SIZE * model.getHeight() + 100);
    contentPane.add(myPicture, "Center");

    addTimer();

    // add timer controls to the south
    JPanel p = new JPanel();
    JButton b1 = new JButton("start");
    b1.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        myTimer.start();
      }
    });
    p.add(b1);
    JButton b2 = new JButton("stop");
    b2.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        myTimer.stop();
      }
    });
    p.add(b2);
    JButton b3 = new JButton("step");
    b3.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        myModel.update();
        myPicture.repaint();
      }
    });
    p.add(b3);

    final JSlider speedBar = new JSlider(1, MAX_DELAY);
    speedBar.addChangeListener(new ChangeListener() {
      public void stateChanged(ChangeEvent ce) {
        myTimer.setDelay(1000 / (speedBar.getValue()));
      }
    });

    p.add(new JLabel(" Slow"));
    p.add(speedBar);
    p.add(new JLabel("Fast "));

    contentPane.add(p, "South");
  }

  private void addTimer()
  // post: creates a timer that calls the model's update
  // method and repaints the display
  {
    ActionListener updater = new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        myModel.update();
        myPicture.repaint();
      }
    };
    myTimer = new javax.swing.Timer(MAX_DELAY / 2, updater);
  }

  private CritterModel myModel;

  private CritterPanel myPicture;

  private javax.swing.Timer myTimer;

  private static final int MAX_DELAY = 140;
}