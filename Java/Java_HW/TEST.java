package Java_HW;

import java.util.Random;



public class TEST {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Random rand = new Random();
        int picture;
        for (int i = 0; i < 10; i++) {
            picture = rand.nextInt(10)+1;
            for (int j = 0; j < picture; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}

