#include <iostream>
using namespace std;
class A
{
    public:
    int a,b=5;
    A(int a)
    {
        this->a = a+1;
        cout<<a<<" "<<this->a<<endl;
    }
    void add(int c)
    {
        cout<<a+b+c<<endl;
    }
};

class B : public A
{
    public:
    int c=100;
    B(int x) : A(x)
    {
    }
    void add()
    {
        cout<< c << " - " << a <<endl;
    }
};

int main()
{
    B a(5);
    a.add(3);
    a.sub();
    
    return 0;
}