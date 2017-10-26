public class TypeConvert{
  public static void main(String[] arg){
    int i1 = 123;
    int i2 = 456;
    double d = (i1+i2)*1.2//系统将转换为double运算，浮点型系统默认为double
    float f = (float)((i1+i2)*1.2);//需要进行强制转换，因为浮点型系统默认为double

    float ff = 1.23f;//必须加f,因为浮点型系统默认为double，
    //double往float转换会有精度损失，错误，保证精度，要加f
    long l = 123;//int类型转换为long类型，可以
    long ll = 30000000000L;//必须加L，不加L,默认为int类型，但是超出int类型范围
    float fff = l + ll + ff;//系统会转换为float类型计算，

    float cf = (float)0.1;//double强制转换float
    float cff = 0.1f;//声明float变量并赋值

    float ffff = 123;//系统将int转换为float
    byte b1 = 1, b2 = 2, b3 = 127;//不超出范围就可以，-127~128
  }
}
