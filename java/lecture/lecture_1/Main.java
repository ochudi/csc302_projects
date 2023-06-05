package lecture.lecture_1;
class Rectangle {
    private int length;
    private int breadth;

    public Rectangle(int length, int breadth) {
        this.length = length;
        this.breadth = breadth;
    }

    public String getFn() {
        return "Length: " + length + ", Breadth: " + breadth;
    }

    public int calcArea() {
        return length * breadth;
    }

    public void displayArea() {
        int area = calcArea();
        System.out.println("The area of the rectangle is: " + area);
    }
}

public class Main {
    public static void main(String[] args) {
        // Create an instance of the Rectangle class
        Rectangle rectangle = new Rectangle(5, 3);

        // Access the attributes and methods of the rectangle instance
        System.out.println(rectangle.getFn()); // Output: Length: 5, Breadth: 3
        rectangle.displayArea(); // Output: The area of the rectangle is: 15
    }
}
