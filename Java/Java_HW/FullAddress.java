package Java_HW;

import java.util.Scanner;



public class FullAddress {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your street address: ");
        String street = input.nextLine();
        System.out.print("Enter your city: ");
        String city = input.nextLine();
        System.out.print("Enter your state: ");
        String state = input.nextLine();
        
        String fullAddress = getFullAddress(street, city, state); // Call getFullAddress once
        System.out.println("Your full address is: " + fullAddress); // Print the result
        
        input.close(); // Close the Scanner object
    }

    public static String getFullAddress(String street, String city, String state){
        return street + ", " + city + ", " + state;
    }
}