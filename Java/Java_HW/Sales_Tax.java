package Java_HW;

import java.util.Scanner;



public class Sales_Tax {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        try {
            System.out.print("Enter the purchase amount: ");
            double purchaseAmount = input.nextDouble();
            System.out.print("What is the state tax rate? (Enter as a percentage): ");
            double stateTaxRate = input.nextDouble();
            double total = salesTaxTotal(purchaseAmount, stateTaxRate);
            System.out.printf("If the price is $%.2f and the state tax rate is %.2f%%, the sales tax is $%.2f%n", purchaseAmount, stateTaxRate, total);
        } finally {
            input.close();
        }
    }

    public static double salesTaxTotal(double purchaseAmount, double stateTaxRate) {
        return purchaseAmount * stateTaxRate/100;
    }
}