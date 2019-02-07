import java.util.Arrays;
public class Game {
	int count;
	Player[] players;
	int size;
	Player person = new Player();
	Game(int count) {
		this.count = count;
		players = new Player[count];
		size = 0;
	}
	
	public void addPlayer(Player playerobj) {
		players[size++] = playerobj;
		// for (int i = 0; i < players.length; i++) {
		// 	if (players[i] == null) {
		// 		players[i] = playerobj;
		// 		size++;
		// 		break;
		// 	}
		// }
	}
	public Player getplayerobject(int index) {
		return players[index];
	}
	public int indexOf(String name) {
		for (int i = 0; i < size; i++) {
			// System.out.println(players[i].getName());
			if (players[i].getName().equals(name)) {
				return i;
			}
		}
		return -1;
	}
	public boolean winner1() {
		for (int i =0; i<size ; i++) {
			if (players[i].getScore() >= 100) {
				return true;
			}
		}
		return false;
	}
	public String winner() {
		String str = "";
		for (int i = 0; i < size; i++) {
			if (players[i].getScore() >= 100) {
				// System.out.println("hello");
				// System.out.println(players[i].getScore());
				str += players[i].getName();
				return str;
			}
			
		}
		return str;
	}
}