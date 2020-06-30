import "dart:io";
void main(){
	List NAB=stdin.readLineSync().split(" ").map((x)=>int.parse(x)).toList();
	if(NAB[0] < 5){
    	print(NAB[0]*NAB[2]);
    }else{
    	NAB[0] -= 5;
    	print(NAB[0]*NAB[1] + 5*NAB[2]);
    }
}
