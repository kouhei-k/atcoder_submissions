import 'dart:io';

main(List<String> args) {
  List SW = stdin.readLineSync().split(' ').map((x) => int.parse(x)).toList();
  if (SW[0] <= SW[1])
    print("unsafe");
  else
    print('safe');
}
