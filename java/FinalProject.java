// import javax.swing.JPanel;
// import javax.swing.JSlider;
// import javax.swing.JTextField;
// import javax.swing.JFrame;

import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

import java.awt.Dimension;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class FinalProject extends JFrame implements ActionListener, ChangeListener{
    
    private JTextField interestRateField;
    private JTextField principleField;
    private JTextField numberField;
    private JTextField totalField;
    private JTextField interestEarnedField;
    private JTextField yearField;

    private JLabel interestRateLabel;
    private JLabel principleLabel;
    private JLabel numberLabel;
    private JLabel yearLabel;
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
        principleLabel = new JLabel("Enter the principal: $");
        numberLabel = new JLabel("Compound Frequency per month(ex: .25, 1, 4): ");
        totalLabel = new JLabel("Total Money: $");
        interestEarnedLabel = new JLabel("Interest Earned: $");
        yearLabel = new JLabel("Number of years");

        convertButton = new JButton("Compute");
        convertButton.addActionListener(this);

        interestRateField = new JTextField(10);
        principleField = new JTextField(10);
        numberField = new JTextField(10);
        interestEarnedField = new JTextField(10);
        totalField = new JTextField(10);
        yearField = new JTextField(2);
        
        totalField.setEditable(false);
        interestEarnedField.setEditable(false);
        yearField.setEditable(false);

        yearSlider = new JSlider(yearMin, yearMax, yearInit);
        yearSlider.addChangeListener(this);
        yearSlider.setMajorTickSpacing(5);
        yearSlider.setMinorTickSpacing(1);
        yearSlider.setPaintLabels(true);
        yearSlider.setPaintTicks(true);

        setLayout(new GridBagLayout());

        lc = new GridBagConstraints();

        lc.insets = new Insets(10,10,1,1);
        lc.anchor = GridBagConstraints.LINE_START;
        lc.gridx = 1;
        lc.gridy = 0;
        lc.gridwidth = 1;
        add(principleLabel,lc);

        lc.insets = new Insets(10,10,1,1);
        lc.anchor = GridBagConstraints.LINE_START;
        lc.gridx = 2;
        lc.gridy = 0;
        lc.gridwidth = 1;
        add(principleField,lc);

        lc.insets = new Insets(10,10,1,1);
        lc.anchor = GridBagConstraints.LINE_START;
        lc.gridx = 1;
        lc.gridy = 1;
        lc.gridwidth = 1;
        add(interestRateLabel,lc);

        lc.insets = new Insets(10,10,1,1);
        lc.anchor = GridBagConstraints.LINE_START;
        lc.gridx = 2;
        lc.gridy = 1;
        lc.gridwidth = 1;
        add(interestRateField,lc);

        lc.insets = new Insets(10,10,1,1);
        lc.anchor = GridBagConstraints.LINE_START;
        lc.gridx = 1;
        lc.gridy = 2;
        lc.gridwidth = 1;
        add(numberLabel,lc);

        lc.insets = new Insets(10,10,1,1);
        lc.anchor = GridBagConstraints.LINE_START;
        lc.gridx = 2;
        lc.gridy = 2;
        lc.gridwidth = 1;
        add(numberField,lc);

        lc.insets = new Insets(10,10,1,1);
        lc.anchor = GridBagConstraints.LINE_START;
        lc.gridx = 3;
        lc.gridy = 0;
        lc.gridwidth = 1;
        add(yearLabel,lc);

        lc.insets = new Insets(10,130,1,1);
        lc.anchor = GridBagConstraints.LINE_START;
        lc.gridx = 3;
        lc.gridy = 0;
        lc.gridwidth = 1;
        add(yearField,lc);

        lc.insets = new Insets(10,1,10,1);
        lc.anchor = GridBagConstraints.LINE_START;
        lc.gridx = 3;
        lc.gridy = 1;
        lc.gridwidth = 1;
        add(yearSlider,lc);

        lc.insets = new Insets(10,10,1,1);
        lc.anchor = GridBagConstraints.LINE_START;
        lc.gridx = 3;
        lc.gridy = 2;
        lc.gridwidth = 1;
        add(convertButton,lc);

        lc.insets = new Insets(10,30,10,1);
        lc.anchor = GridBagConstraints.LINE_START;
        lc.gridx = 0;
        lc.gridy = 5;
        lc.gridwidth = 1;
        add(totalLabel,lc);

        lc.insets = new Insets(10,5,10,1);
        lc.anchor = GridBagConstraints.LINE_START;
        lc.gridx = 1;
        lc.gridy = 5;
        lc.gridwidth = 1;
        add(totalField,lc);

        lc.insets = new Insets(10,30,10,1);
        lc.anchor = GridBagConstraints.LINE_START;
        lc.gridx = 0;
        lc.gridy = 6;
        lc.gridwidth = 1;
        add(interestEarnedLabel,lc);

        lc.insets = new Insets(10,5,10,1);
        lc.anchor = GridBagConstraints.LINE_START;
        lc.gridx = 1;
        lc.gridy = 6;
        lc.gridwidth = 1;
        add(interestEarnedField,lc);



    }

    @Override
    public void stateChanged(ChangeEvent event){
        yearField.setText(Integer.toString(yearSlider.getValue()));
    }

    @Override
    public void actionPerformed(ActionEvent event){
        double dYears = yearSlider.getValue();
        double dPrinciple = Integer.parseInt(principleField.getText());
        double dRate = Double.parseDouble(interestRateField.getText());
        dRate = dRate / 100;
        double dFrequency = Double.parseDouble(numberField.getText());
        double dTotal = dPrinciple *  Math.pow((1 + (dRate / dFrequency)), (dFrequency * dYears));
        double dDifference = dTotal - dPrinciple;

        totalField.setText("$"+ Math.round(dTotal));
        interestEarnedField.setText("$" + Math.round(dDifference));
        
        
    }
    
    public static void main(String[] args){
        FinalProject myFrame = new FinalProject();
        myFrame.setMinimumSize(new Dimension(600,400));
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.pack();
        myFrame.setVisible(true);
    }
}