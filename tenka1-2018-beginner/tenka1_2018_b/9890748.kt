fun main(args: Array<String>) {
    var (a,b,k) = readLine()!!.split(" ").map(String::toInt)
    for(i in 1..k){
        if(i%2==1){
            a = a / 2
            b += a
        }else{
            b = b / 2
            a += b
        }

    }
    println("${a} ${b}")
}
