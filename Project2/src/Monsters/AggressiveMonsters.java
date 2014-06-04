package Monsters;
import org.newdawn.slick.Image;
import org.newdawn.slick.SlickException;


public class AggressiveMonsters extends Monster{

	public AggressiveMonsters(double x, double y, String name)
			throws SlickException {
		super(x, y);
		if (name.equalsIgnoreCase("Zombie")){
			this.name = "Zombie";

			// Set up the monster's avatar
			this.avatar = new Image("assets/units/zombie.png");

			// Set the monster's stats
			this.maxHealth = 60;
			this.health = maxHealth;
			this.strength = 10;
			this.cooldown = 800;

		}
		else if(name.equalsIgnoreCase("Skeleton")){
			this.name = "Skeleton";

			// Set up the monster's avatar
			this.avatar = new Image("assets/units/skeleton.png");

			// Set the monster's stats
			this.maxHealth = 100;
			this.health = maxHealth;
			this.strength = 16;
			this.cooldown = 500;
		}
		else if(name.equalsIgnoreCase("Draelic")){
			this.name = "Draelic";

			// Set up the monster's avatar
			this.avatar = new Image("assets/units/necromancer.png");

			// Set the monster's stats
			this.maxHealth = 140;
			this.health = maxHealth;
			this.strength = 30;
			this.cooldown = 400;
		}
		else if(name.equalsIgnoreCase("Bandit")){
			this.name = "Bandit";

			// Set up the monster's avatar
			this.avatar = new Image("assets/units/bandit.png");

			// Set the monster's stats
			this.maxHealth = 40;
			this.health = maxHealth;
			this.strength = 8;
			this.cooldown = 200;
		}
	}

}
