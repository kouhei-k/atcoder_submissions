fun main(args: Array<String>) {
    var day = readLine()!!
    var weekdays = listOf("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    var ans = 5 - weekdays.indexOf(day)
    if(ans>5){
        ans = 0
    }
    println(ans)

}
