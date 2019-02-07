public class Player {
	String player_name;
	int score;
	// Player() {

	// }
	Player(String player_name) {
		this.player_name = player_name;
		this.score = score;
	}
	public String getName() {
		return this.player_name;
	}
	public int getScore() {
		return this.score;
	}
	public void setName(String name) {
		this.player_name = name;
	}
	public void setScore(int score) {
		// System.out.println("score "+score);
		// System.out.println("name" +getName());
		// System.out.println(getName());
		// System.out.println("befor scoe" +this.score);
		this.score += score;
		// System.out.println("score");

		// System.out.println(this.score);
	}
}
