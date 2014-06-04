package Villagers;
/*
 * Villager Garth
 * author: weiqian wang<wangw>
 * */

import org.newdawn.slick.Image;
import org.newdawn.slick.SlickException;

import project2.Player;
import project2.Unit;


public class Garth extends Villager {

	/**
	 * Create farmer
	 * 
	 * @param x
	 *            The peasant's x coordinate
	 * @param y
	 *            The peasant's y coordinate
	 * @param name
	 *            The peasant's name
	 * @throws SlickException
	 */
	public Garth(double x, double y, String name) throws SlickException
	{
		super(x, y, name, new Image("assets/units/peasant.png"));
	}

	@Override
	public void interact(Unit target) {
		
		// Player interacting with this Villager
		if (target instanceof Player)
		{
			
			// Give amulet quest
			if (target.getInventory().hasItem("Amulet of Vitality") == null)
			{
				setDialogue("Find the Amulet of Vitality, across the river to the west.");
			}
			// Give sword quest
			else if (target.getInventory().hasItem("Sword of Strength") == null)
			{
				setDialogue("Find the Sword of Strength - cross the river and back, on the east side.");
			}
			// Give tome quest
			else if (target.getInventory().hasItem("Tome of Agility") == null)
			{
				setDialogue("Find the Tome of Agility, in the Land of Shadows.");
			}
			// Out of quests
			else
			{
				setDialogue("You have found all the treasure I know of.");
			}
		}
	}

		
}
