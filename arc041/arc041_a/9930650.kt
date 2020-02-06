//import kotlin.math.*
fun main(args: Array<String>) {
    val (x,y) = readLine()!!.split(" ").map(String::toInt)
    val k = readLine()!!.toInt()
    
    println(Math.min(y,k) + Math.min(0,y - k) + x)
}
