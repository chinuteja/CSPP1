// import java.util.Arrays;
public class Game {
	int count;
	Player[] p;
	int size;
	Player person = new Player();
	Game(int count) {
		this.count = count;
		p = new Player[count];
		size = 0;
	}
	Game() {
		p = new Player[count];
		size = 0;
	}
	public void addPlayer(Player obj) {
		for (int i = 0; i < p.length; i++) {
			if (p[i] == null) {
				p[i] = obj;
				size++;
				break;
			}
		}
	}
	public Player getp(int index) {
		return p[index];
	}
	public int indexOf(String name) {
		for (int i = 0; i < size; i++) {
			if (p[i].getName().equals(name)) {
				return i;
			}
		}
		return -1;
	}
	public void winner() {
		int temp;
		int i;
		// for (int i = 0; i < size; i++) {
		// 	if (p[i].getScore() >= 100) {
		// 		// System.out.println(p[i].getScore());
		// 		System.out.println(p[i].getName());
		// 		break;
		// 		// return p[i].getName();
		// 	}
		// 	// if (p[i].getScore() > max) {
		// 	// 	max = p[i].getScore();
		// 	// 	System.out.println(p[i].getName());
		// 	// 	break;
		// 	// }
		// }
		// return null;
		int j = 0;
	    temp = p[0].getScore();
	    // boolean flag = false;
	    for ( i = 0; i<size ; i++) {
	    	// System.out.println("name is "+p[i].getName());
	    	// System.out.println("score "+temp);
	    	// System.out.println("getScore"+p[i].getScore());
	    	if (p[i].getScore() > temp || p[i].getScore() == temp) {
	    		temp = p[i].getScore();
	    		j = i;
	    		
	    	} 
	    }
	    System.out.println(p[j].getName());
	    // if (flag) {
	    // 	System.out.println("Mark");
	    // }
	    for (int  k = 0; k<size -1; k++) {
	    	if (p[k].getScore() == p[k+1].getScore()) {
	    		System.out.println("hello");
	    		System.out.println(p[k].getName());
	    		
	    	}
	    }
	}
}