package Model;

public class StatsTeamModel extends StatsModel{
    public StatsTeamModel(int id, int matches, int victories, int defeats, double victoryPercent, int goals) {
        super(id, matches, victories, defeats, victoryPercent, goals);
    }
    private TeamModel team;
    private int concedeGoals;
    private double ballPossession;
    private int shotsOnGoal;
    private int completedPasses;
    private int corners;
    private int offsides;
    private int titles;
    private int foulsCommitted;


    public StatsTeamModel(int id, int matches, int victories, int defeats, double victoryPercent, int goals, TeamModel team, int concedeGoals, double ballPossession, int shotsOnGoal, int completedPasses, int corners, int offsides, int titles, int foulsCommitted) {
        super(id, matches, victories, defeats, victoryPercent, goals);
        this.team = team;
        this.concedeGoals = concedeGoals;
        this.ballPossession = ballPossession;
        this.shotsOnGoal = shotsOnGoal;
        this.completedPasses = completedPasses;
        this.corners = corners;
        this.offsides = offsides;
        this.titles = titles;
        this.foulsCommitted = foulsCommitted;
    }


    public TeamModel getTeam() {
        return team;
    }

    public void setTeam(TeamModel team) {
        this.team = team;
    }

    public int getConcedeGoals() {
        return concedeGoals;
    }

    public void setConcedeGoals(int concedeGoals) {
        this.concedeGoals = concedeGoals;
    }

    public double getBallPossession() {
        return ballPossession;
    }

    public void setBallPossession(double ballPossession) {
        this.ballPossession = ballPossession;
    }

    public int getShotsOnGoal() {
        return shotsOnGoal;
    }

    public void setShotsOnGoal(int shotsOnGoal) {
        this.shotsOnGoal = shotsOnGoal;
    }

    public int getCompletedPasses() {
        return completedPasses;
    }

    public void setCompletedPasses(int completedPasses) {
        this.completedPasses = completedPasses;
    }

    public int getCorners() {
        return corners;
    }

    public void setCorners(int corners) {
        this.corners = corners;
    }

    public int getOffsides() {
        return offsides;
    }

    public void setOffsides(int offsides) {
        this.offsides = offsides;
    }

    public int getTitles() {
        return titles;
    }

    public void setTitles(int titles) {
        this.titles = titles;
    }

    public int getFoulsCommitted() {
        return foulsCommitted;
    }

    public void setFoulsCommitted(int foulsCommitted) {
        this.foulsCommitted = foulsCommitted;
    }
}
