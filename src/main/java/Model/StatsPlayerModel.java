package Model;

public class StatsPlayerModel extends StatsModel{
    public StatsPlayerModel(int id, int matches, int victories, int defeats, double victoryPercent, int goals) {
        super(id, matches, victories, defeats, victoryPercent, goals);
    }
    private PlayerModel player;
    private int assists;
    private int yellowCards;
    private int redCards;
    private int completedPasses;
    private int interception;
    private int disarms;
    private int sufferedFouls;
    private int commitedFouls;
    private String injuries;


    public StatsPlayerModel(int id, int matches, int victories, int defeats, double victoryPercent, int goals, PlayerModel player, int assists, int yellowCards, int redCards, int completedPasses, int interception, int disarms, int sufferedFouls, int commitedFouls, String injuries) {
        super(id, matches, victories, defeats, victoryPercent, goals);
        this.player = player;
        this.assists = assists;
        this.yellowCards = yellowCards;
        this.redCards = redCards;
        this.completedPasses = completedPasses;
        this.interception = interception;
        this.disarms = disarms;
        this.sufferedFouls = sufferedFouls;
        this.commitedFouls = commitedFouls;
        this.injuries = injuries;
    }

    public StatsPlayerModel() {
        super();
    }


    public PlayerModel getPlayer() {
        return player;
    }

    public void setPlayer(PlayerModel player) {
        this.player = player;
    }

    public int getAssists() {
        return assists;
    }

    public void setAssists(int assists) {
        this.assists = assists;
    }

    public int getYellowCards() {
        return yellowCards;
    }

    public void setYellowCards(int yellowCards) {
        this.yellowCards = yellowCards;
    }

    public int getRedCards() {
        return redCards;
    }

    public void setRedCards(int redCards) {
        this.redCards = redCards;
    }

    public int getCompletedPasses() {
        return completedPasses;
    }

    public void setCompletedPasses(int completedPasses) {
        this.completedPasses = completedPasses;
    }

    public int getInterception() {
        return interception;
    }

    public void setInterception(int interception) {
        this.interception = interception;
    }

    public int getDisarms() {
        return disarms;
    }

    public void setDisarms(int disarms) {
        this.disarms = disarms;
    }

    public int getSufferedFouls() {
        return sufferedFouls;
    }

    public void setSufferedFouls(int sufferedFouls) {
        this.sufferedFouls = sufferedFouls;
    }

    public int getCommitedFouls() {
        return commitedFouls;
    }

    public void setCommitedFouls(int commitedFouls) {
        this.commitedFouls = commitedFouls;
    }

    public String getInjuries() {
        return injuries;
    }

    public void setInjuries(String injuries) {
        this.injuries = injuries;
    }
}
