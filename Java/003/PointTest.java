class Point{
  double x, y, z;

  Point(double _x, double _y, double _z){
    x = _x;
    y = _y;
    z = _z;
  }

  void setX(double _x){
    x = _x;
  }

  double getDistance(Point p){
    return (x - p.x)*(x-p.x) + (y - p.y)*(y-p.y) + (z - p.z)*(z-p.z);
  }
}

public class PointTest{
  public static void main(String[] args){
    Point p = new Point(1.0, 2.0, 3.0);
    Point po = new Point(0.0, 0.0, 0.0);
    System.out.println(p.getDistance(po));

    p.setX(2.0);
    System.out.println(p.getDistance(po));

  }
}
