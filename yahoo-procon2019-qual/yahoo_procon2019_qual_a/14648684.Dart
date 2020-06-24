import "dart:io";
void main(){
  List NK=stdin.readLineSync().split(" ").map((x)=>int.parse(x)).toList();
  if(NK[0]+1 >= NK[1]*2)print("YES");
  else print("NO");
}
