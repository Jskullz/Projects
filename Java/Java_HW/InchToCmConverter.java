package Java_HW;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
import java.util.Scanner;


public class InchToCmConverter {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("What is your height in inches?: ");
        double inches = scanner.nextDouble();
        double cm = inches * 2.54;
        System.out.println("Your height in centimeters is: "+ cm);
        
        scanner.close(); // Close the scanner to avoid resource leak
    }
    
}
