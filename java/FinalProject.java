// import javax.swing.JPanel;
// import javax.swing.JSlider;
// import javax.swing.JTextField;
// import javax.swing.JFrame;

import javax.swing.*;


public class FinalProject extends JFrame implements ActionListener, ChangeListener{
    
    private JTextField interestRateField;
    private JTextField principleField;
    private JTextField numberField;
    private JTextField totalField;
    private JTextField interestEarnedField;

    private JLabel interestRateLabel;
    private JLabel principalLabel;
    private JLabel numberLabel;
    private JLabel totalLabel;
    private JLabel interestEarnedLabel;

    private JSlider yearSlider;
    private JButton convertButton;

    FinalProject(){
        int yearMin = 0;
        int yearMax = 40;
        int yearInit = 10;
        GridBagConstraints lc = null;

        setTitle("Compunt Interest Calculator");

        interestRateLabel = new JLabel("Enter Interest Rate (ex 12.9):");
        principleLabel = new JLabel("Enter the Principle: $");
        numberLabel = new JLabel("Enter the number of times it compounds in a month(ex: .25, .5): ");
        totalLabel = new JLabel("Total Money: $");
        interestEarnedLabel = new JLabel("Interest Earned: $");
        convertButton = new JButton("Convert");
        convertButton.addActionListener(this);

        interestRateField = new JTextField(10);
        principleField = new JTextField(10);
        numberField = new JTextField(10);
        interestEarnedField = new JTextField(10);
        totalField = new JTextField(10);
        
        totalField.setEditable(false);
        interestEarnedField.setEditable(false);

        setLayout(new GridBagLayout());

    }

    public static double calculateInterest(int year){

    }

    @Override
    public void stateChanged(ChangeEvent event){

    }

    @Override
    public void actionPerformed(ActionEvent event){
        int iYears = yearSlider.getValue();
        
    }
    
    public static void main(String[] args){
        FinalProject myFrame = new FinalProject();

        myFrame.
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.pack();
        myFrame.setVisible(true);
    }
}