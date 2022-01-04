public abstract class Sport{
    public String name = "";
    public int playerNumber = 0;
    public long salary = 0;

    public Sport(String n, int p, long s){
        this.name = n;
        this.playerNumber = p;
        this.salary = s;
    }

    public String getName(){
        return name;
    }
    public int getPlayerNumber(){
        return playerNumber;
    }
    public long getSalary(){
        return salary;
    }
    public double getVertical() {
        return 0;
    }
    public double getPitchSpeed(){
        return 0;
    }
    public double getBattingAvg(){
        return 0;
    }
    public int getFieldGoals(){
        return 0;
    }
    public int getPassingYards(){
        return 0;
    }
}

class Basketball extends Sport{
    private double vertical = 0;

    public Basketball(String name, int playerNumber, long salary, double verticalJump){
        super(name, playerNumber, salary);
        this.vertical = verticalJump;
    }

    @Override
    public double getVertical(){
        return vertical;
    }
    
}

class Baseball extends Sport{
    private double pitchSpeed = 0.0;
    private double battingAvg = 0.0;
    
    public Baseball(String name, int playerNumber, long salary, double pitchSpeed, double battingAvg){
        super(name, playerNumber, salary);
        this.pitchSpeed = pitchSpeed;
        this.battingAvg = battingAvg;
    }
    public double getPitchSpeed(){
        return pitchSpeed;
    }
    public double getBattingAvg(){
        return battingAvg;
    }

}

class Football extends Sport{
    private int fieldGoals = 0;
    private int passingYards = 0;
    public Football(String name, int playerNumber, long salary, int fieldGoals, int passingYards){
        super(name, playerNumber, salary);
        this.fieldGoals = fieldGoals;
        this.passingYards = passingYards;
    }
    public int getFieldGoals(){
        return fieldGoals;
    }
    public int getPassingYards(){
        return passingYards;
    }
}

class ProblemThreeDriverClass{
    public static void main(String[] args){
        Sport basketballSport = new Basketball("Koby Bryant", 24, 25000000, 5.2);
        Sport baseballSport = new Baseball("Yadier Molina", 4, 9000000, 90, .252);
        Sport footballSport = new Football("Tom Brady", 12, 56000000, 0, 88000);

        System.out.println("The basketball player's name is "+basketballSport.getName()+". He is number "+basketballSport.getPlayerNumber()+" and he makes $"+basketballSport.getSalary()+" a year. His vertical is "+basketballSport.getVertical());
        System.out.println("The baseball player's name is "+baseballSport.getName()+". He is number "+baseballSport.getPlayerNumber()+" and he makes $"+baseballSport.getSalary()+" a year. His pitching speed is "+baseballSport.getPitchSpeed()+"mph and his batting average is "+baseballSport.getBattingAvg());
        System.out.println("The football player's name is "+footballSport.getName()+" number "+footballSport.getPlayerNumber()+" making $"+footballSport.getSalary()+" a year. He has kicked "+footballSport.getFieldGoals()+" field goals and passed "+footballSport.getPassingYards()+" yards.");
    }
}