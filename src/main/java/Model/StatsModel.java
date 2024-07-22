package Model;

public class StatsModel {
    private int id;
    private int matches;
    private int victories;
    private int defeats;
    private double victoryPercent;
    private int goals;


    public StatsModel(int id, int matches, int victories, int defeats, double victoryPercent, int goals) {
        this.id = id;
        this.matches = matches;
        this.victories = victories;
        this.defeats = defeats;
        this.victoryPercent = victoryPercent;
        this.goals = goals;
    }

    public StatsModel() {

    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getMatches() {
        return matches;
    }

    public void setMatches(int matches) {
        this.matches = matches;
    }

    public int getVictories() {
        return victories;
    }

    public void setVictories(int victories) {
        this.victories = victories;
    }

    public int getDefeats() {
        return defeats;
    }

    public void setDefeats(int defeats) {
        this.defeats = defeats;
    }

    public double getVictoryPercent() {
        return victoryPercent;
    }

    public void setVictoryPercent(double victoryPercent) {
        this.victoryPercent = victoryPercent;
    }

    public int getGoals() {
        return goals;
    }

    public void setGoals(int goals) {
        this.goals = goals;
    }
}
