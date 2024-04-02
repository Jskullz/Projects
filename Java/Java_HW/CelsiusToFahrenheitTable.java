package Java_HW;



public class CelsiusToFahrenheitTable {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println("Celsius   Fahrenheit");
        System.out.println("--------------------");
        
        // Generate the table for temperatures from 0 to 100 in increments of 10
        for (int celsius = 0; celsius <= 100; celsius += 10) {
            double fahrenheit = celsiusToFahrenheit(celsius);
            System.out.printf("%-9d %.2f%n", celsius, fahrenheit);
        }
    }

    // Method to convert Celsius to Fahrenheit
    public static double celsiusToFahrenheit(int celsius) {
        return celsius * 1.8 + 32;
    }
}