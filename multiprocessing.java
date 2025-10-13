import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.TimeUnit;
import java.util.Random;

public class MultiProcessSimulation {

    public static void main(String[] args) throws InterruptedException {
        BlockingQueue<String> queue = new LinkedBlockingQueue<>();

        Thread listenMicrophone = new Thread(() -> {
            Random random = new Random();
            String[] commands = {"turn on the light", "move forward", "stop"};
            try {
                while (true) {
                    double sleepTime = 0.5 + random.nextDouble(); // 0.5 to 1.5 seconds
                    TimeUnit.MILLISECONDS.sleep((long)(sleepTime * 1000));
                    String text = commands[random.nextInt(commands.length)];
                    System.out.println("[Mic] Heard: " + text);
                    queue.put(text);
                }
            } catch (InterruptedException e) {
                // Thread interrupted, exit gracefully
            }
        });

        Thread processCommand = new Thread(() -> {
            try {
                while (true) {
                    String text = queue.poll(100, TimeUnit.MILLISECONDS);
                    if (text != null) {
                        System.out.println("[Processor] Executing command for: " + text);
                        TimeUnit.MILLISECONDS.sleep(500);
                    }
                }
            } catch (InterruptedException e) {
                // Thread interrupted, exit gracefully
            }
        });

        Thread backgroundMonitor = new Thread(() -> {
            try {
                while (true) {
                    System.out.println("[Monitor] System OK");
                    TimeUnit.SECONDS.sleep(3);
                }
            } catch (InterruptedException e) {
                // Thread interrupted, exit gracefully
            }
        });

        listenMicrophone.start();
        processCommand.start();
        backgroundMonitor.start();

        try {
            TimeUnit.SECONDS.sleep(10);
        } finally {
            System.out.println("Terminating processes...");
            listenMicrophone.interrupt();
            processCommand.interrupt();
            backgroundMonitor.interrupt();

            listenMicrophone.join();
            processCommand.join();
            backgroundMonitor.join();
        }
    }
}
