package Monsters;
/*
 * class for Passive Monsters
 * author: weiqian wang<wangw>
 * */


import org.newdawn.slick.Image;
import org.newdawn.slick.SlickException;


public class PassiveMonster extends Monster{

	public PassiveMonster(double x, double y, String name)
			throws SlickException {
		super(x, y);
		if (name.equalsIgnoreCase("Bat")){
			this.name = "Giant Bat";

			// Set up the monster's avatar
			this.avatar = new Image("assets/units/dreadbat.png");

			// Set the monster's stats
			this.maxHealth = 40;
			this.health = maxHealth;
			this.strength = 0;
			this.cooldown = 0;
			// Set up the monster's physical size
			this.physWidth = 35;
			this.physHeight = 45;
		}
	}
}
