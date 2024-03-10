/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package stringmethods;
import java.util.Scanner;
/**
 *
 * @author julia
 */
public class StringMethods {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
    System.out.print("What is your first name?: ");
        String firstname= scanner.nextLine();
    System.out.print("What is your middle name?: ");
        String middlename= scanner.nextLine();
    System.out.print("What is your last name?: ");
        String lastname = scanner.nextLine();
        String initials = firstname.substring(0,1) + "." + middlename.substring(0,1) +"."+lastname.substring(0,1);
            System.out.println("Your name is: "+ firstname + " " +middlename+" "+ lastname);
            System.out.println("Your initials are: "+ initials);
            System.out.println("Your first name in all uppercase is: "+ firstname.toUpperCase());
            System.out.println("Your last name in all lowercase is: "+ lastname.toLowerCase());
        
    }
    
}
