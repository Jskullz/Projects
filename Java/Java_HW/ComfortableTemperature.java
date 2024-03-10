package Java_HW;


import java.util.Scanner;
public class ComfortableTemperature {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("What is the temperature in the room?");
        int temperature = input.nextInt();

        if (temperature > 75) {
            System.out.println("It is too hot");
        } else if (temperature < 65) {
            System.out.println("It is too cold");
        } else {
            System.out.println("It is comfortable");
        }
        
        input.close();
    }
    
}