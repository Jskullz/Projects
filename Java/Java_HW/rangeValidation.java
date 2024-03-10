package Java_HW;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
import java.util.Scanner;


public class rangeValidation {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
         Scanner scanner = new Scanner(System.in);
         System.out.println("Enter a number between 5 and 7");
         int number=0;
         while (number != 6){
            number = scanner.nextInt();
            if(number > 5 && number <7){
                System.out.println("You entered 6");
            } else {
                System.out.println("Invalid number. Try again.");
            }
         }
         scanner.close();
    }
}
