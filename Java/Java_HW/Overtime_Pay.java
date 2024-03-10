package Java_HW;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
import java.util.Scanner;


public class TEST {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       Scanner scanner = new Scanner(System.in);
        System.out.println("How many hours did you work?");
        double hours = scanner.nextDouble();
        System.out.println("What is your hourly wage?");
        double wage= scanner.nextDouble();
        double pay;
        if (hours > 40) {
            double overtime= hours * wage * 1.5;
            pay = overtime;
        } else {
            pay = hours * wage;
        }
        String message= String.format("By working %.2f hours at a rate of $%.2f an hour, you earned $%.2f this week.", hours, wage, pay);
        System.out.println(message);
    }
}
