interface Shape {
    double getVolume();
    double getSurfaceArea();
}

class Sphere implements Shape{
    double r = 0;
    public Sphere(double radius){
        this.r = radius;
    }
    @Override
    public double getVolume() {
        return ((4 / 3) * (Math.PI) * (Math.pow(r, 3)));
    }

    @Override
    public double getSurfaceArea() {
        return (4 * Math.PI * (Math.pow(r, 2)));
    }

    public double getRadius(){
        return r;
    }
    
}

class Cones implements Shape{
    double r = 0;
    double h = 0;
    public Cones(double radius, double height){
        this.r = radius;
        this.h = height;
    }
    @Override
    public double getVolume() {
        return (Math.PI * (Math.pow(r, 2)) * (h / 3));
    }

    // πr(r+sqrt(h^2+r^2))
    @Override
    public double getSurfaceArea() {
        return (Math.PI * r) * (r + Math.sqrt((Math.pow(h, 2) + Math.pow(r, 2))));
    }

    public double getRadius(){
        return r;
    }
}

class Cylinder implements Shape{
    double r = 0;
    double h = 0;
    public Cylinder(double radius, double height){
        this.r = radius;
        this.h = height;
    }

    @Override
    public double getVolume() {
        return (h * Math.PI * Math.pow(r,2));
    }

    // 2πrh+2πr^2
    @Override
    public double getSurfaceArea() {
        return (2 * Math.PI * r * h)+(2 * Math.PI * Math.pow(r, 2));
    }

    public double getRadius(){
        return r;
    }

}

class Cube implements Shape{
    double e = 0;
    public Cube(double edge){
        this.e = edge;
    }

    @Override
    public double getVolume() {
        return Math.pow(e,3);
    }

    @Override
    public double getSurfaceArea() {
        return 6 * Math.pow(e, 2);
    }

}

class RectangularPrism implements Shape{
    double h = 0;
    double l = 0;
    double w = 0;

    public RectangularPrism(double length, double width, double height){
        this.l = length;
        this.w = width;
        this.h = height;
    }

    @Override
    public double getVolume(){
        return l * w * h;
    }

    @Override
    public double getSurfaceArea() {
        return 2 * ((w*l) + (h*l) + (h*w));
    }
}

class TriangularPrism implements Shape{
    double a = 0;
    double b = 0;
    double c = 0;
    double h = 0;


    public TriangularPrism(double sidea, double sideb, double sidec, double height){
        this.a = sidea;
        this.b = sideb;
        this.c = sidec;
        this.h = height;
    }

    @Override
    public double getVolume() {
        double temp = -1 * Math.pow(a,4)+(2 * Math.pow((a*b), 2)) + (2 * Math.pow((a * c), 2)) - Math.pow(b,4) + 2 * Math.pow((c*b), 2) + (-1 * Math.pow(c, 4));
        temp = (.25 * h) * temp;
        return temp;
    }

    @Override
    public double getSurfaceArea() {
        return 0;
    }

}

class DriverClass{
    public static void main(String[] args){
        Shape cone = new Cones(5.5, 4);
        Shape sphere = new Sphere(5.5);
        Shape cylinder = new Cylinder(5.5, 4);
        Shape cube = new Cube(5);
        Shape rp = new RectangularPrism(4, 5, 6);

        System.out.println("The volume of a cone is: " + cone.getVolume());
        System.out.println("The surface area of a cone with a radius of units is: " + cone.getSurfaceArea());
        System.out.println();
        System.out.println("The volume of a sphere is: " + sphere.getVolume());
        System.out.println("The surface area of a sphere with a radius of units is: " + sphere.getSurfaceArea());
        System.out.println();
        System.out.println("The volume of a cylinder is: " + cylinder.getVolume());
        System.out.println("The surface area of a cylinder with a radius of units is: " + cylinder.getSurfaceArea());
        System.out.println();
        System.out.println("The volume of a cube is: " + cube.getVolume());
        System.out.println("The surface area of a cube: " + cube.getSurfaceArea());
        System.out.println();
        System.out.println("The volume of a rectangular prism is: " + rp.getVolume());
        System.out.println("The surface area of a rectangular prism: " + rp.getSurfaceArea());
    }
}
