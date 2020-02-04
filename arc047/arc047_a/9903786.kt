fun main(args: Array<String>) {
    val(N,L) = readLine()!!.split(" ").map(String::toInt)
    val S = readLine()!!
    var count = 1
    var ans = 0
    for(i in 0..N-1){
        if(S[i] == '+'){
            count += 1
            if(count > L){
                ans += 1
                count = 1
            }
        }else{
            count -= 1
        }
    } 
    println(ans)
}
