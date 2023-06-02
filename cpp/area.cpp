#include <iostream>
using namespace std;

class Rectangle
{
private:
    int length;
    int breadth;

public:
    Rectangle(int length, int breadth)
    {
        this->length = length;
        this->breadth = breadth;
    }

    string get_fn()
    {
        return "Length: " + to_string(length) + ", Breadth: " + to_string(breadth);
    }

    int calc_area()
    {
        return length * breadth;
    }

    void display_area()
    {
        int area = calc_area();
        cout << "The area of the rectangle is: " << area << endl;
    }
};

int main()
{
    // Create an instance of the Rectangle class
    Rectangle rectangle(5, 3);

    // Access the attributes and methods of the rectangle instance
    cout << rectangle.get_fn() << endl; // Output: Length: 5, Breadth: 3
    rectangle.display_area();           // Output: The area of the rectangle is: 15

    return 0;
}
