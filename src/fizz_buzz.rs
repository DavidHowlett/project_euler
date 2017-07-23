pub fn fizz_buzz(){
    for i in 1..101{
        if i%15 ==0{
            print!("fizzbuzz\n");
        }else if i%3 == 0 {
            print!("fizz\n")
        }else if i%5 == 0 {
            print!("buzz\n")
        }else{
            print!("{}\n", i);
        }
    }
}