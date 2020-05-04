import 'dart:io';

main(List<String> args) {
  List ABCD = stdin.readLineSync().split(' ').map((x) => int.parse(x)).toList();
  if ((ABCD[0] / ABCD[3]).ceil() < (ABCD[2] / ABCD[1]).ceil())
    print("No");
  else
    print("Yes");
}
