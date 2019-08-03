package jp;
class C extends Thread{
	public void run() {
		for(int i=1;i<=10;i++) {
			System.out.println("C "+i);
		}
	}
}

class D extends Thread{
	public void run() {
		for(int i=1;i<=10;i++) {
			System.out.println("D "+i);
		}
	}
}





public class Th2 {
	public static void main(String[] args) {
		C o1=new C();
		D o2=new D();
		o1.start();
		o2.start();
	}
}
