import java.io.*;
import java.util.*;

public class CreateItemFile {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Map<Integer, String> items = new HashMap<>();
        File file = new File("items.txt");

        try {
            if (!file.exists()) {
                file.createNewFile();
            }
            Scanner fileScanner = new Scanner(file);
            while (fileScanner.hasNextLine()) {
                String line = fileScanner.nextLine();
                String[] parts = line.split(",");
                int itemNumber = Integer.parseInt(parts[0]);
                String description = parts[1];
                items.put(itemNumber, description);
            }
            fileScanner.close();
        } catch (IOException e) {
            System.out.println("An error occurred while creating the file.");
            e.printStackTrace();
            System.exit(1);
        }

        while (true) {
            System.out.print("Enter item number (or 0 to quit): ");
            int itemNumber = scanner.nextInt();
            if (itemNumber == 0) {
                break;
            }
            if (items.containsKey(itemNumber)) {
                System.out.println("Item number already exists. Please try again.");
                continue;
            }
            System.out.print("Enter item description (up to 20 characters): ");
            scanner.nextLine(); // consume the newline character
            String description = scanner.nextLine();
            if (description.length() > 20) {
                description = description.substring(0, 20);
            }
            items.put(itemNumber, description);
            try {
                FileWriter fileWriter = new FileWriter(file, true);
                fileWriter.write(itemNumber + "," + description + "\n");
                fileWriter.close();
            } catch (IOException e) {
                System.out.println("An error occurred while writing to the file.");
                e.printStackTrace();
                System.exit(1);
            }
            System.out.println("Item added successfully.");
        }

        scanner.close();
    }
}
