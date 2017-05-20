fn main(){
    let mut a = 1;
    let mut b = 0;
    let mut tmp = 0;
    let mut total = 0;
    while i < 1000 {
        tmp = a;
        a = a+b;
        b = tmp;
        print(a)
        i = i + 1;

    }
    print(total)
}