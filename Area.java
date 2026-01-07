public class Area{
    public static void main(String[] args) {
        System.out.println("Feature order change " + areaOfCircle(5));
    }
    public static double areaOfCircle(double radius) {
        int pi = 3;
        return Math.PI * radius;
    }
}