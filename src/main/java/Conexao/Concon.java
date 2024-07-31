/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Conexao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 *
 * @author abraa
 */
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Concon {
    private static final String URL = "jdbc:mysql://localhost:3306/new_schema";
    private static final String USER = "root";
    private static final String PASSWORD = "root";

    public static Connection getConexao() {
        Connection conexao = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver"); // Certifique-se de que o driver está carregado
            conexao = DriverManager.getConnection(URL, USER, PASSWORD);
            System.out.println("Conexão estabelecida com sucesso!");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
            System.out.println("Driver não encontrado.");
        } catch (SQLException e) {
            e.printStackTrace();
            System.out.println("Erro na conexão: " + e.getMessage());
        }
        return conexao;
    }
}

