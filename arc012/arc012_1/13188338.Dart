import "dart:io";

void main(List<String> args) {
  var day = stdin.readLineSync();
  List weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
  var ans = 5 - weekdays.indexOf(day);
  if (ans > 5) {
    ans = 0;
  }
  print(ans);
}
