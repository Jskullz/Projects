
import java.util.Scanner;
public class SecretWord 

    public static void main(String[] args) {
        {
            Scanner scanner = new Scanner(System.in);
            System.out.println("What is the secret word?: ");
            String secretWord = scanner.nextLine();
            if (secretWord.toLowerCase().equals("password1")) {
                System.out.println("You know the secret word.");
            } else {
                System.out.println("You don't know the secret word.");
            }
            scanner.close();
        }
    
}