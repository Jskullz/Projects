/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package calculatebmi;
import java.util.Scanner;

/**
 *
 * @author julia
 */
public class CalculateBMI {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("What is your height in ft/in? You can say for example 5\"7': ");
        String height = scanner.nextLine();
    System.out.print("What is your weight in pounds?: ");
        double weight = scanner.nextDouble();
        double height_in_inches= Double.parseDouble(height.substring(0,1))*12 + Double.parseDouble(height.substring(2,3));
        double bmi = round((weight/(height_in_inches*height_in_inches))*703);

        System.out.println("Your BMI is: "+ bmi);


    }
    
}
