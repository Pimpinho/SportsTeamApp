package Model;

public class TeamModel {
    private int id;
    private String name;
    private String coach;
    private String stadium;
    private StatsTeamModel teamStats;
    private String[] playersTeam;


    public TeamModel(int id, String name, String coach, String stadium, StatsTeamModel teamStats, String[] playersTeam) {
        this.id = id;
        this.name = name;
        this.coach = coach;
        this.stadium = stadium;
        this.teamStats = teamStats;
        this.playersTeam = playersTeam;
    }

    public TeamModel(String[] playersTeam) {
        this.playersTeam = playersTeam;
    }

    public String[] getPlayersTeam() {
        return playersTeam;
    }

    public void setPlayersTeam(String[] playersTeam) {
        this.playersTeam = playersTeam;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCoach() {
        return coach;
    }

    public void setCoach(String coach) {
        this.coach = coach;
    }

    public String getStadium() {
        return stadium;
    }

    public void setStadium(String stadium) {
        this.stadium = stadium;
    }

    public StatsTeamModel getTeamStats() {
        return teamStats;
    }

    public void setTeamStats(StatsTeamModel teamStats) {
        this.teamStats = teamStats;
    }
}
