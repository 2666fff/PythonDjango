package Villagers;
/* 433-294 Object Oriented Software Development
 * Shaman 
 * Author:weiqian wang <wangw>
 */





import org.newdawn.slick.Image;
import org.newdawn.slick.SlickException;

import project2.Player;
import project2.Unit;


public class Shaman extends Villager
{
	// /** The completion status of the peasant's quest */
	// private boolean questComplete = false;
	private int messageGiven = 0;

	/**
	 * Create a shaman
	 * 
	 * @param x
	 *            The shaman's x coordinate
	 * @param y
	 *            The shaman's y coordinate
	 * @param name
	 *            The shaman's name
	 * @throws SlickException
	 */
	public Shaman(double x, double y, String name) throws SlickException
	{
		super(x, y, name, new Image("assets/units/shaman.png"));
	}

	@Override
	/** The action to take when interacting with another Unit (usually the player)
	 * 
	 * @param world The game world, acting as a facade
	 * @param target The target to interact with
	 */
	public void interact(Unit target)
	{
		// Player interacting with this Villager
		if (target instanceof Player)
		{
			if (messageGiven++ < 1)
			{
				setDialogue("Please help! My house is full of monsters!");
			}
			// Player is on full health, do nothing
			else if (target.getHealth() == target.getMaxHealth())
			{
				setDialogue("Return to me if you ever need healing.");
			}
			// Player is injured, heal to full health
			else
			{
				target.setHealth(target.getMaxHealth());
				setDialogue("You're looking much healthier now.");
			}
		}
	}

}
