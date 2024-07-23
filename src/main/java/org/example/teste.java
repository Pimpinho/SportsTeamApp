package org.example;

import Model.PlayerModel;
import Model.StatsPlayerModel;
import Model.StatsModel;
import java.util.ArrayList;
import java.util.Scanner;


public class Main {
    private static final ArrayList<PlayerModel> players = new ArrayList<>();
    private static int nextId = 1;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Management functionalities:");
            System.out.println("1. Players");
            System.out.println("2. Team");
            System.out.println("3. Statistics");
            System.out.println("5. Sair");
            System.out.print("Escolha uma opção: ");

            int option = scanner.nextInt();
            scanner.nextLine();  // Consome a nova linha

            switch (option) {
                case 1:
                    playerMenu(scanner);
                    break;
                case 2:
                    //teamMenu(scanner);
                    break;
                case 3:
                    //editPlayer(scanner);
                    break;
                case 4:
                    listPlayers();
                    break;
                case 5:
                    System.out.println("Exiting.");
                    scanner.close();
                    return;
                default:
                    System.out.println("Opção inválida, tente novamente.");
            }
        }
    }

    private  static void playerMenu(Scanner scanner){

    }

    private static void addPlayer(Scanner scanner) {
        System.out.print("Nome: ");
        String name = scanner.nextLine();
        System.out.print("Idade: ");
        int age = scanner.nextInt();
        scanner.nextLine(); // Consome a nova linha
        System.out.print("Nacionalidade: ");
        String nationality = scanner.nextLine();
        System.out.print("Posição: ");
        String position = scanner.nextLine();
        System.out.print("Número da camisa: ");
        int shirtNumber = scanner.nextInt();
        scanner.nextLine(); // Consome a nova linha
        System.out.print("Time: ");
        String team = scanner.nextLine();

        PlayerModel player = new PlayerModel(nextId++, name, age, nationality, position, shirtNumber, team);
        players.add(player);
        System.out.println("Jogador adicionado com sucesso!");
    }

    private static void removePlayer(Scanner scanner) {
        System.out.print("ID do jogador a ser removido: ");
        int id = scanner.nextInt();
        scanner.nextLine(); // Consome a nova linha

        players.removeIf(player -> player.getId() == id);
        System.out.println("Jogador removido com sucesso!");
    }

    private static void editPlayer(Scanner scanner) {
        System.out.print("ID do jogador a ser editado: ");
        int id = scanner.nextInt();
        scanner.nextLine(); // Consome a nova linha

        PlayerModel player = null;
        for (PlayerModel p : players) {
            if (p.getId() == id) {
                player = p;
                break;
            }
        }

        if (player == null) {
            System.out.println("Jogador não encontrado!");
            return;
        }

        System.out.print("Novo nome (atual: " + player.getName() + "): ");
        String name = scanner.nextLine();
        System.out.print("Nova idade (atual: " + player.getAge() + "): ");
        int age = scanner.nextInt();
        scanner.nextLine(); // Consome a nova linha
        System.out.print("Nova nacionalidade (atual: " + player.getNationality() + "): ");
        String nationality = scanner.nextLine();
        System.out.print("Nova posição (atual: " + player.getPosition() + "): ");
        String position = scanner.nextLine();
        System.out.print("Novo número da camisa (atual: " + player.getShirtNumber() + "): ");
        int shirtNumber = scanner.nextInt();
        scanner.nextLine(); // Consome a nova linha
        System.out.print("Novo time (atual: " + player.getTeam() + "): ");
        String team = scanner.nextLine();

        player.setName(name);
        player.setAge(age);
        player.setNationality(nationality);
        player.setPosition(position);
        player.setShirtNumber(shirtNumber);
        player.setTeam(team);

        System.out.println("Jogador editado com sucesso!");
    }

    private static void listPlayers() {
        if (players.isEmpty()) {
            System.out.println("Nenhum jogador cadastrado.");
        } else {
            for (PlayerModel player : players) {
                System.out.println(player.getName());
            }
        }
    }
}


