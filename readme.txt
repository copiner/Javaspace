javac hello.java
java Hello

基本数据类型 8位(bit)二进制信息称为一个字节(byte)

整数型 byte(8bit) short(2byte) int(4byte) long(8byte)
浮点型 float double
字符型 char(2byte)
布尔型 boolean

引用数据类型
class
interface
array

声明变量，就是内存中开辟一定空间。
byte类型变量占1字节(byte)   取值范围 -2的7次方到2的7次方-1  为什么是2的7次方，前面一位是个符号位，代表正负
short类型变量占2字节(byte)  取值范围 -2的15次方到2的15次方-1
int类型变量占4字节(byte)    取值范围 -2的31次方到2的31次方-1
long类型变量占8字节(byte)    取值范围  -2的63次方到2的63次方-1

float 占4字节(byte)double 占8字节(byte)
分配可能如下
float 1bit(符号位） 7（bit)指数位， 24bit(小数位）
double 1bit(符号位） 10（bit)指数位， 53bit(小数位）
float类型取值范围-2的128次方到2的127次方
double类型取值范围-2的1024次方到2的1023次方

强制类型转换