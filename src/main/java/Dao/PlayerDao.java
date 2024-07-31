/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Dao;

import Conexao.Concon;
import Model.PlayerModel;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import javax.swing.JOptionPane;

/**
 *
 * @author abraa
 */
public class PlayerDao {
     public void cadastrarPlayer(PlayerModel player) {
        Connection conn = Concon.getConexao();
        if (conn == null) {
            System.out.println("Conexão é nula. Não é possível continuar.");
            JOptionPane.showMessageDialog(null, "Erro ao conectar ao banco de dados. Tente novamente mais tarde.", "Erro de Conexão", JOptionPane.ERROR_MESSAGE);
            return;
        }

        String sql = "INSERT INTO jogadores (name, age, nationality, position, shirtNumber, team) VALUES (?, ?, ?, ?, ?, ?)";
        try (PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, player.getName());
            ps.setInt(2, player.getAge());
            ps.setString(3, player.getNationality());
            ps.setString(4, player.getPosition());
            ps.setInt(5, player.getShirtNumber());
            ps.setString(6, player.getTeam());

            ps.executeUpdate();
            System.out.println("Jogador cadastrado com sucesso!");
        } catch (SQLException e) {
            e.printStackTrace();
            System.out.println("Erro ao cadastrar jogador: " + e.getMessage());
            JOptionPane.showMessageDialog(null, "Erro ao cadastrar jogador: " + e.getMessage(), "Erro", JOptionPane.ERROR_MESSAGE);
        }
    }
}

